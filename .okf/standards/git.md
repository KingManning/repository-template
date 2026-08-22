---
type: Standard
title: Git Standards
description: Repository-wide requirements for branches, commits, pull requests, tracked files, and GitHub workflows.
tags: [standards, git, github, repository]
---

These standards govern how humans and AI agents use Git and GitHub when contributing to this repository.

# Line endings

The root [`.gitattributes`](../../.gitattributes) defines the repository's line-ending policy:

* Git-recognized text is stored and checked out with LF on every operating system.
* Windows command scripts (`*.bat` and `*.cmd`) are checked out with CRLF.
* Repository attributes override personal `core.autocrlf` behavior for matching files.

Repositories generated from this template MUST adapt the binary patterns and `-text` exceptions to their own content. Add exceptions for unlisted binary formats, generated outputs, or byte-sensitive fixtures before normalization. A repository with independently maintained applications, such as backend, frontend, or mobile applications, MAY place additional `.gitattributes` files in those application roots.

## Renormalizing safely

Start from a clean working tree or isolate unrelated work. Stage the policy files first, then let Git re-evaluate every tracked path:

```bash
git add .gitattributes
git add --renormalize .
```

Review the entire staged change before committing:

```bash
git diff --cached --check
git diff --cached --stat
git diff --cached
git ls-files --eol
```

Treat changes to binary files, archives, generated output, and byte-sensitive fixtures as suspect. If Git stages an unintended path, unstage it with `git restore --staged -- <path>`, add the appropriate attribute rule, and rerun the normalization and review. Do not discard unrelated working-tree changes while correcting the index.
