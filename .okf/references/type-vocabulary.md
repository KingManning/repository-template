---
type: Reference
title: OKF Type Vocabulary
description: Normative controlled type values and role-based mapping rules for repository concepts.
tags: [references, okf, metadata, types]
---

Every non-reserved concept uses exactly one of the following type values. Tags, `status`, `date`, and other extension fields carry specialization and lifecycle; they must not create type synonyms.

# Controlled types

| Type | Use |
|---|---|
| `Roadmap` | Planned stage, completed phase, current state, roadmap principles, or backlog. |
| `Reference` | Specification, provenance, vocabulary, or other supporting reference. |
| `Standard` | Normative requirements governing repository practices, documentation, Git, coding, testing, and contribution workflows. |

# Related concepts

The [OKF specification](/references/okf-specification.md) requires a non-empty type but permits producer-defined values.
