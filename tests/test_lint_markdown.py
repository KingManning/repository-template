from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
LINTER = REPOSITORY_ROOT / "scripts" / "lint_markdown.py"


class MarkdownLinterTests(unittest.TestCase):
    def run_linter(self, root: Path, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(LINTER), *args],
            cwd=root,
            capture_output=True,
            check=False,
            text=True,
        )

    def test_scan_reports_violation_and_fix_repairs_it(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            document = root / "invalid.md"
            document.write_text("# Title", encoding="utf-8")

            result = self.run_linter(root)

            self.assertNotEqual(0, result.returncode)
            self.assertIn("MD047", result.stdout)
            self.assertEqual("# Title", document.read_text(encoding="utf-8"))

            fix = self.run_linter(root, "--fix")
            self.assertEqual(3, fix.returncode, fix.stdout + fix.stderr)
            self.assertEqual("# Title\n", document.read_text(encoding="utf-8"))
            self.assertEqual(0, self.run_linter(root).returncode)

    def test_md052_is_not_applied(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "reference.md").write_text(
                "[unresolved reference][missing]\n", encoding="utf-8"
            )

            result = self.run_linter(root)

            self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_markdown_extension_and_dependency_exclusions(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "guide.markdown").write_text("#Title\n", encoding="utf-8")
            dependency_directory = root / "node_modules"
            dependency_directory.mkdir()
            (dependency_directory / "vendor.md").write_text(
                "#Title\n", encoding="utf-8"
            )

            result = self.run_linter(root)

            self.assertNotEqual(0, result.returncode)
            self.assertIn("guide.markdown", result.stdout)
            self.assertNotIn("vendor.md", result.stdout)


if __name__ == "__main__":
    unittest.main()
