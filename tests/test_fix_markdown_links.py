from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

# Keep the test runnable both directly and through unittest discovery.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.fix_markdown_links import candidate_targets


class CandidateTargetsTests(unittest.TestCase):
    def test_source_relative_target_wins_over_repository_root_fallback(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            source_directory = root / "frontend"
            source_directory.mkdir()
            source_file = source_directory / "README.md"
            source_file.touch()
            source_target = source_directory / "AGENTS.md"
            source_target.touch()
            (root / "AGENTS.md").touch()

            matches = candidate_targets(
                "./AGENTS.md",
                source_file,
                root,
                list(root.rglob("*")),
                [],
            )

            self.assertEqual([source_target.resolve()], matches)

    def test_repository_root_fallback_repairs_missing_source_target(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            source_directory = root / ".okf"
            source_directory.mkdir()
            source_file = source_directory / "concept.md"
            source_file.touch()
            root_target = root / "README.md"
            root_target.touch()

            matches = candidate_targets(
                "README.md",
                source_file,
                root,
                list(root.rglob("*")),
                [],
            )

            self.assertEqual([root_target.resolve()], matches)

    def test_repository_root_target_cannot_escape_repository(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            root = temporary_root / "repository"
            root.mkdir()
            source_file = root / "concept.md"
            source_file.touch()
            (temporary_root / "outside.md").touch()

            matches = candidate_targets(
                "/../outside.md",
                source_file,
                root,
                list(temporary_root.rglob("*")),
                [],
            )

            self.assertEqual([], matches)


if __name__ == "__main__":
    unittest.main()
