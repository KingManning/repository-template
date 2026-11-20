# Scripts

## Markdown linting

Run these commands from the repository root. Install `pymarkdownlnt` once
using the pinned [requirements](../requirements.txt).

```powershell
py -m pip install -r requirements.txt
```

The [lint script](./lint_markdown.py) runs PyMarkdown with the repository's
[configuration](../.pymarkdown.json).

```powershell
# Report lint issues (read-only)
py scripts/lint_markdown.py

# Apply supported fixes in place
py scripts/lint_markdown.py --fix
```

The report lists the file, line, and rule for each issue. When PyMarkdown
applies a fix, it prints `Fixed:` with the filename and returns exit code 3.
Run the read-only command again to check for issues that need manual edits.

## Internal Markdown links

The [link checker](./fix_markdown_links.py) previews proposed link replacements
by default. Review the replacements before applying them.

```powershell
# Preview link repairs
py scripts/fix_markdown_links.py

# Apply link repairs
py scripts/fix_markdown_links.py --write
```
