# Scripts

Contains repository scripts for various tasks, such as fixing markdown links, generating documentation, and more.

## Structure

- [`fix_markdown_links.py`](./fix_markdown_links.py) - validates and repairs
  repository Markdown links.

## Fix Markdown Links

Run the link validator from the repository root:

```powershell
# Preview changes
npm run lint:links

# Apply changes
npm run lint:links:fix
```

The root `npm run lint` command combines the link scan with Markdownlint.
`npm run lint:fix` runs both repair commands.

The focused link-resolver tests live in
[Repository Tooling Tests](../tests/README.md).
