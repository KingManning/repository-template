# Repository Tooling Tests

Focused tests for repository-maintenance scripts live here. Project-specific
tests should remain with their owning components.

## Structure

- [`test_fix_markdown_links.py`](./test_fix_markdown_links.py) - verifies
  source-relative link precedence, repository-root repair fallback, and
  repository-boundary enforcement for
  [`fix_markdown_links.py`](../scripts/fix_markdown_links.py).

## Run the tests

From the repository root, run:

```powershell
py -m unittest discover -s .\tests -p "test_*.py"
```
