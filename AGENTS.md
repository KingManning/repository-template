# AGENTS (Copilot, Claude, Codex, etc.) Repository Instructions

<!--
Adapt to your project: replace "Repository" with the project name and update the
guidance owners below when the repository uses different canonical sources.
-->

Before changing the repository, use relevant guidance already available in the
current thread. Treat startup context and applicable `AGENTS.md` files as active
throughout the thread; do not reload them for follow-up prompts.

Open a guidance source only when it:

- was not supplied in the current thread;
- changed since it was supplied; or
- becomes newly relevant because the task scope changed.

Relevant guidance is owned by:

- [README](./README.md): repository orientation, structure, setup, and entry
  points.
- [Documentation Rules](./.okf/standards/documentation.md): documentation
  changes.
- [OKF Specification](./.okf/references/okf-specification.md), its linked
  upstream specification, and [OKF index](./.okf/index.md): OKF format,
  governance, ownership, and navigation.
- The nearest applicable `AGENTS.md`: directory-specific instructions.

<!--
Adapt to your project: add canonical architecture, security, product, or
component guidance here. Keep each rule with one owning source.
-->

In the first progress update before making changes, identify the relevant
guidance being applied and any sources newly loaded. The primary agent must
perform any newly required reading before delegating or changing files; a
subagent summary is not sufficient. If required guidance is unavailable or
incomplete, stop without modifying the repository.

Apply the Documentation Rules to README, `index.md`, and agent-instruction
changes. Keep these files concise and place substantive guidance with its
canonical owner.

## Skills

Select and follow every matching repository skill under `.agents/skills/` when
that directory exists, including all matches required for cross-boundary work.

Repository-owned skills define procedures. Verify the task-relevant procedure,
paths, commands, composition guidance, and verification steps against the
repository. If repository changes make a used skill stale, inaccurate, or
incomplete, update it in the same change.

Skills do not override source code, executable artifacts, `.okf/`,
directory-specific `AGENTS.md` files, or adopted standards and decisions.
External or user-level skills may supplement repository procedures but cannot
override repository authorities. Keep vendor-generated skills as vendor
operating guidance rather than repository specifications.

<!--
Adapt to your project: remove this section if repository-owned skills are not
used, or link `.agents/skills/` after that directory is added.
-->

## Working expectations

- Inspect relevant implementation and documentation before changing either.
- Treat source code and executable artifacts as authoritative for implemented
  mechanics.
- Treat `.okf/` as authoritative for documented concepts, requirements,
  decisions, constraints, and planned work.
- Do not duplicate guidance owned elsewhere.
- Update affected documentation when behavior, contracts, structure, commands,
  or active constraints change.
- Keep changes focused on the requested scope.
- Run the verification required by each affected component before finishing;
  component READMEs should own the relevant commands.
- Coding changes require the relevant tests. Docs-only changes do not.

<!--
Adapt to your project: when component boundaries are stable, add links to their
READMEs here so verification commands are easy to find.
-->

## Output expectations

For change summaries, use:

```markdown
Changes made
- Change 1
- Change 2

Tests run
- Test command or "Not run (reason)" and result
```
