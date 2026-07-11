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
| `Product Concept` | Vision, audience, principles, plans, capabilities, and product direction. |
| `Product Requirement` | Workspaces, acceptance criteria, success measures, and risks. |
| `Domain Entity` | Persisted or future entity with identity and fields. |
| `Domain Model` | Domain behavior, calculations, guidance, or conceptual models that are not entities. |
| `Domain Value Set` | Enumerated values, taxonomies, categories, and adjustment vocabularies. |
| `Data Contract` | Structured input, output, point, event, or summary shape. |
| `Architecture` | System, technology, security, testing, frontend, or evolution architecture. |
| `Implementation Guide` | Implemented backend/frontend behavior, engines, pipelines, read models, workflows, and configuration semantics. |
| `API Contract` | Current or target routes, compatibility, errors, OpenAPI, and fixtures. |
| `Operations Guide` | Deployment, delivery, security operations, observability, migrations, and readiness. |
| `Decision` | Product or architecture decision with date and lifecycle status. |
| `Roadmap` | Planned stage, completed phase, current state, roadmap principles, or backlog. |
| `Reference` | Specification, provenance, vocabulary, or other supporting reference. |
| `Standard` | Normative requirements governing repository practices, documentation, Git, coding, testing, and contribution workflows. |
| `Legacy Reference` | Historical FastAPI behavior, runtime, persistence, and parity evidence. |

# Role mapping


# Related concepts

The [OKF specification](/references/okf-specification.md) requires a non-empty type but permits producer-defined values.

