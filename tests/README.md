# Repository Tooling Tests

Focused tests for repository-maintenance scripts live here. Project-specific
tests should remain with their owning components.

## Structure

- [`test_fix_markdown_links.py`](./test_fix_markdown_links.py) - verifies
  source-relative link precedence, repository-root repair fallback, and
  repository-boundary enforcement for
  [`fix_markdown_links.py`](../scripts/fix_markdown_links.py).
- [`test_lint_markdown.py`](./test_lint_markdown.py) - verifies read-only scans,
  automatic fixes, lint rules, and file selection through the
  [lint script](../scripts/lint_markdown.py).

## Run the tests

Install the lint dependency as described in the [Scripts README](../scripts/README.md),
then run the tests from the repository root.

```powershell
py -m unittest discover -s tests
```
