from __future__ import annotations

import argparse
import os
import re
from pathlib import Path
from urllib.parse import quote, unquote

INLINE_LINK_RE = re.compile(
    r'(?P<prefix>!?\[[^\]]*\]\()'
    r'(?P<destination><[^>]+>|[^)\s]+)'
    r'(?P<suffix>(?:\s+(?:"[^"]*"|\'[^\']*\'))?\))'
)

REFERENCE_LINK_RE = re.compile(
    r'^(?P<prefix>\s*\[[^\]]+\]:\s*)'
    r'(?P<destination><[^>]+>|\S+)'
    r'(?P<suffix>.*)$'
)

EXTERNAL_PREFIXES = (
    "http://",
    "https://",
    "mailto:",
    "tel:",
    "data:",
    "ftp://",
    "//",
    "#",
)

DEFAULT_EXCLUDES = (
    ".git",
    "frontend/node_modules",
    "frontend/.next",
    "node_modules",
)


def is_same_or_inside(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def build_excluded_paths(root: Path, excludes: list[str]) -> list[Path]:
    excluded_paths: list[Path] = []
    for value in excludes:
        candidate = Path(value)
        if not candidate.is_absolute():
            candidate = root / candidate
        excluded_paths.append(candidate.resolve())
    return excluded_paths


def is_excluded(path: Path, excluded_paths: list[Path]) -> bool:
    resolved = path.resolve()
    return any(is_same_or_inside(resolved, excluded) for excluded in excluded_paths)


def walk_repository(
    root: Path,
    excluded_paths: list[Path],
) -> tuple[list[Path], list[Path]]:
    markdown_files: list[Path] = []
    repository_paths: list[Path] = []

    for current_dir, directory_names, file_names in os.walk(root, followlinks=False):
        current = Path(current_dir)

        directory_names[:] = [
            name
            for name in directory_names
            if not is_excluded(current / name, excluded_paths)
        ]

        for name in directory_names:
            repository_paths.append((current / name).resolve())

        for name in file_names:
            path = (current / name).resolve()
            if is_excluded(path, excluded_paths):
                continue

            repository_paths.append(path)
            if path.suffix.lower() == ".md":
                markdown_files.append(path)

    return sorted(markdown_files), repository_paths


def split_path_and_suffix(destination: str) -> tuple[str, str]:
    positions = [
        position
        for position in (destination.find("?"), destination.find("#"))
        if position != -1
    ]
    if not positions:
        return destination, ""

    split_at = min(positions)
    return destination[:split_at], destination[split_at:]


def deduplicate(paths: list[Path]) -> list[Path]:
    unique: list[Path] = []
    for path in paths:
        resolved = path.resolve()
        if resolved not in unique:
            unique.append(resolved)
    return unique


def candidate_targets(
    raw_path: str,
    source_file: Path,
    root: Path,
    repository_paths: list[Path],
    excluded_paths: list[Path],
) -> list[Path]:
    decoded = unquote(raw_path.replace("\\", "/"))
    normalized = decoded.lstrip("/")
    if normalized.startswith("./"):
        normalized = normalized[2:]

    if decoded.startswith("/"):
        # Treat /path/to/file.md as repository-root-relative.
        repository_root_candidate = root / normalized
        if (
            repository_root_candidate.exists()
            and is_same_or_inside(repository_root_candidate.resolve(), root)
            and not is_excluded(repository_root_candidate, excluded_paths)
        ):
            return [repository_root_candidate.resolve()]
    else:
        # Standard Markdown behavior is authoritative when the source-relative
        # target exists. Repair fallbacks must not make a valid link ambiguous.
        source_relative_candidate = source_file.parent / decoded
        if (
            source_relative_candidate.exists()
            and is_same_or_inside(source_relative_candidate.resolve(), root)
            and not is_excluded(source_relative_candidate, excluded_paths)
        ):
            return [source_relative_candidate.resolve()]

        repair_candidates: list[Path] = []

        # Repair duplicated current-directory paths such as
        # ./standards/coding.md from a file already inside standards/.
        parts = Path(normalized).parts
        if parts and parts[0] == source_file.parent.name and len(parts) > 1:
            repair_candidates.append(
                source_file.parent.joinpath(*parts[1:])
            )

        # Also allow a broken path that was written as repository-root-relative
        # without a leading slash.
        repair_candidates.append(root / normalized)

        valid_repairs = deduplicate(
            [
                candidate
                for candidate in repair_candidates
                if candidate.exists()
                and is_same_or_inside(candidate.resolve(), root)
                and not is_excluded(candidate, excluded_paths)
            ]
        )

        if valid_repairs:
            return valid_repairs

    # Last-resort repair: find an exact, unique repository path suffix.
    # This fixes paths such as /architecture/technology-stack.md when the
    # actual target is .okf/architecture/technology-stack.md.
    suffix = normalized.rstrip("/")
    if not suffix:
        return []

    suffix_matches: list[Path] = []
    for candidate in repository_paths:
        if not is_same_or_inside(candidate.resolve(), root):
            continue
        relative = candidate.relative_to(root).as_posix()
        if relative == suffix or relative.endswith(f"/{suffix}"):
            suffix_matches.append(candidate)

    return deduplicate(suffix_matches)


def relative_link(target: Path, source_file: Path) -> str:
    relative = os.path.relpath(target, source_file.parent).replace(os.sep, "/")

    # Enforce explicit relative prefixes. Checking for a leading dot alone is
    # insufficient because hidden paths such as .okf/ and .github/ also begin
    # with a dot but still require an explicit ./ prefix.
    if relative == ".":
        relative = "./"
    elif relative == "..":
        relative = "../"
    elif not relative.startswith(("./", "../")):
        relative = f"./{relative}"

    return quote(relative, safe="/.@_-~")


def repair_destination(
    destination: str,
    source_file: Path,
    root: Path,
    repository_paths: list[Path],
    excluded_paths: list[Path],
) -> tuple[str | None, str]:
    wrapped = destination.startswith("<") and destination.endswith(">")
    plain = destination[1:-1] if wrapped else destination

    if not plain or plain.lower().startswith(EXTERNAL_PREFIXES):
        return None, "skipped"

    raw_path, suffix = split_path_and_suffix(plain)
    if not raw_path:
        return None, "skipped"

    matches = candidate_targets(
        raw_path,
        source_file,
        root,
        repository_paths,
        excluded_paths,
    )

    if not matches:
        return None, "missing"

    if len(matches) > 1:
        return None, "ambiguous"

    repaired = relative_link(matches[0], source_file) + suffix
    if wrapped:
        repaired = f"<{repaired}>"

    if repaired == destination:
        return None, "valid"

    return repaired, "repaired"


def process_line(
    line: str,
    source_file: Path,
    root: Path,
    repository_paths: list[Path],
    excluded_paths: list[Path],
    line_number: int,
    findings: list[tuple[str, int, str, str, str | None]],
) -> str:
    def replace_inline(match: re.Match[str]) -> str:
        destination = match.group("destination")
        replacement, status = repair_destination(
            destination,
            source_file,
            root,
            repository_paths,
            excluded_paths,
        )

        findings.append(
            (
                source_file.relative_to(root).as_posix(),
                line_number,
                status,
                destination,
                replacement,
            )
        )

        if replacement is None:
            return match.group(0)

        return (
            f"{match.group('prefix')}"
            f"{replacement}"
            f"{match.group('suffix')}"
        )

    updated = INLINE_LINK_RE.sub(replace_inline, line)

    reference_match = REFERENCE_LINK_RE.match(updated)
    if reference_match:
        destination = reference_match.group("destination")
        replacement, status = repair_destination(
            destination,
            source_file,
            root,
            repository_paths,
            excluded_paths,
        )

        findings.append(
            (
                source_file.relative_to(root).as_posix(),
                line_number,
                status,
                destination,
                replacement,
            )
        )

        if replacement is not None:
            updated = (
                f"{reference_match.group('prefix')}"
                f"{replacement}"
                f"{reference_match.group('suffix')}"
            )

    return updated


def process_file(
    path: Path,
    root: Path,
    repository_paths: list[Path],
    excluded_paths: list[Path],
    write_changes: bool,
    findings: list[tuple[str, int, str, str, str | None]],
) -> bool:
    try:
        original = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        findings.append(
            (
                path.relative_to(root).as_posix(),
                0,
                "unreadable",
                "File is not valid UTF-8",
                None,
            )
        )
        return False

    output: list[str] = []
    in_code_fence = False
    active_fence: str | None = None

    for line_number, line in enumerate(original.splitlines(keepends=True), start=1):
        stripped = line.lstrip()
        fence = "```" if stripped.startswith("```") else (
            "~~~" if stripped.startswith("~~~") else None
        )

        if fence:
            if not in_code_fence:
                in_code_fence = True
                active_fence = fence
            elif fence == active_fence:
                in_code_fence = False
                active_fence = None

            output.append(line)
            continue

        if in_code_fence:
            output.append(line)
            continue

        output.append(
            process_line(
                line,
                path,
                root,
                repository_paths,
                excluded_paths,
                line_number,
                findings,
            )
        )

    updated = "".join(output)
    changed = updated != original

    if changed and write_changes:
        with path.open("w", encoding="utf-8", newline="") as file:
            file.write(updated)

    return changed


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Repair internal Markdown links across a repository."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path("."),
        help="Repository root. Default: current directory",
    )
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help=(
            "Repository-relative path to exclude. May be supplied multiple times. "
            "Defaults already exclude .git and frontend/node_modules."
        ),
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Apply changes. Without this flag, only report proposed changes.",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    if not root.is_dir():
        raise SystemExit(f"Repository root not found: {root}")

    excludes = [*DEFAULT_EXCLUDES, *args.exclude]
    excluded_paths = build_excluded_paths(root, excludes)
    markdown_files, repository_paths = walk_repository(root, excluded_paths)

    findings: list[tuple[str, int, str, str, str | None]] = []
    changed_files = 0

    for markdown_file in markdown_files:
        if process_file(
            markdown_file,
            root,
            repository_paths,
            excluded_paths,
            args.write,
            findings,
        ):
            changed_files += 1

    counts: dict[str, int] = {}
    for _, _, status, _, _ in findings:
        counts[status] = counts.get(status, 0) + 1

    print(f"Mode: {'WRITE' if args.write else 'DRY RUN'}")
    print(f"Repository root: {root}")
    print(f"Excluded: {', '.join(excludes)}")
    print(f"Markdown files scanned: {len(markdown_files)}")
    print(f"{'Files changed' if args.write else 'Files that would change'}: {changed_files}")
    print(f"Links to repair: {counts.get('repaired', 0)}")
    print(f"Already valid: {counts.get('valid', 0)}")
    print(f"Missing targets: {counts.get('missing', 0)}")
    print(f"Ambiguous targets: {counts.get('ambiguous', 0)}")
    print(f"Unreadable files: {counts.get('unreadable', 0)}")
    print()

    repair_label = "REPAIRED" if args.write else "WOULD_REPAIR"

    for file_name, line_number, status, destination, replacement in findings:
        if status == "repaired":
            print(
                f"{repair_label:12} {file_name}:{line_number}  "
                f"{destination} -> {replacement}"
            )
        elif status in {"missing", "ambiguous", "unreadable"}:
            print(f"{status.upper():12} {file_name}:{line_number}  {destination}")

    if not args.write and counts.get("repaired", 0):
        print("\nDry run only. Re-run with --write to apply the repairs.")

    return 1 if (
        counts.get("missing", 0)
        or counts.get("ambiguous", 0)
        or counts.get("unreadable", 0)
    ) else 0


if __name__ == "__main__":
    raise SystemExit(main())
