import argparse
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check Markdown in the current directory and its subdirectories."
    )
    parser.add_argument("--fix", action="store_true", help="Apply available PyMarkdown fixes.")
    args = parser.parse_args()

    config = Path(__file__).resolve().parents[1] / ".pymarkdown.json"
    command = [
        sys.executable, "-m", "pymarkdown",
        "--config", str(config), "--strict-config",
        "fix" if args.fix else "scan",
        "--recurse", "--alternate-extensions", ".md,.markdown", ".",
    ]
    return subprocess.run(command, check=False).returncode


if __name__ == "__main__":
    sys.exit(main())
