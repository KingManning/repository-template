---
type: Standard
title: Documentation Standards
description: Requirements for authoring, organizing, maintaining, and reviewing the OKF knowledge bundle.
tags: [standards, documentation, governance, okf]
---

These rules govern documentation authored in `.okf/`. They supplement the format requirements in the [OKF specification](../references/okf-specification.md). `MUST` identifies a requirement; `SHOULD` identifies the expected default unless a documented reason justifies an exception.

# Current truth and planned work

* Everything outside `.okf/roadmap/` MUST describe facts, behavior, accepted decisions, and active constraints that are true and applicable on the default branch.
* Current truth includes implemented behavior, durable product purpose, and active product, security, safety, legal, and architectural constraints. It does not include an unimplemented design merely because that design has been discussed or accepted.
* Proposed, exploratory, candidate, target, contingent, or otherwise unimplemented content MUST live in one owning roadmap stage. Research, brainstorming, open questions, stage-specific risks, acceptance criteria, and target designs belong with that stage.
* A current-state concept MAY state that a capability is unsupported and point to its roadmap stage. It MUST NOT restate the proposed solution.
* When a stage is completed, its verified and enduring facts MUST be promoted to the appropriate current-state concepts. The completed stage SHOULD retain only a concise outcome and links rather than duplicate implementation detail.

# Authority by knowledge type

* Source code and executable artifacts such as tests, migrations, configuration, OpenAPI, and generated clients are authoritative for implemented mechanics and contracts.
* `.okf/` is authoritative for documented product scope, concepts, rationale, active risks and constraints, accepted decisions, and operational explanation that executable artifacts cannot express adequately.
* `.okf/roadmap/` is authoritative for planned work.
* Documentation SHOULD point to machine-readable contracts and source artifacts instead of copying material that can drift.
* A disagreement between documentation and implementation MUST be investigated. The intended behavior and its canonical documentation MUST be reconciled in the same change; implementation must not automatically override a requirement, decision, or safety constraint.

# Canonical ownership and pointers

* Every substantive fact MUST have one canonical owning concept.
* Other concepts SHOULD state only the context needed to explain the relationship and then use a descriptive pointer to the owner. Pages must not become unexplained link collections.
* Routine duplication is limited to short navigation metadata such as frontmatter descriptions, `index.md` entries, and repository README summaries. These summaries MUST NOT introduce unique requirements or implementation detail.
* A safety warning MAY be repeated when relying on a pointer would create a material risk.
* Superseded current-state copies MUST be removed. Git history preserves obsolete prose.

# Separation and consolidation

* Each concept SHOULD answer one coherent reader question and contain no more concerns than can be maintained as a single unit.
* Concepts SHOULD be combined only when they have the same audience, purpose, authority, owner, and update cadence. Similar names or a desire to reduce the file count are not sufficient reasons to merge.
* Stable principles and changing risk assessments SHOULD remain separate unless they satisfy the consolidation test. Risks specific to future work belong in the owning roadmap stage.
* Enduring product-level success measures MAY accompany product scope. Measures that determine whether a planned stage is complete belong in that stage.
* Decision records preserve the context, decision, rationale, consequences, and lifecycle status of an accepted choice. They MUST NOT become a second specification for future implementation; that detail belongs in the roadmap.
* Historical roadmap stages and decisions MAY remain when their status and successor are explicit. Other historical narrative SHOULD be removed unless it has continuing operational or provenance value.

# Navigation

* An `index.md` is a navigation surface, not a second documentation surface. It SHOULD list the directory's concepts and subdirectories with short descriptions.
* Every new concept SHOULD be discoverable from its nearest useful index.
* Link text SHOULD use the target document's title where it reads naturally. Where a target may be ambiguous, qualify the link text, for example `[Repository README](../../README.md)`.
* Internal Markdown links MUST be relative to the current file:
  * Use `./` for targets in the same directory or a child directory, for example `[Coding Standards](./coding.md)`.
  * Use `../` for targets in a parent or sibling directory, for example `[Type Vocabulary](../references/type-vocabulary.md)`.

  * Links from a repository-root Markdown file to a descendant MUST begin with `./`, for example:

    ```bash
    [Documentation Rules](./.okf/standards/documentation.md)
    ```

  * Do not use repository-root-relative paths such as `/.okf/standards/documentation.md`.

* Repository README references intended to direct the reader to an existing file, directory, or concept MUST use a Markdown link.
* Paths used only as commands, configuration values, examples, output locations, or implementation terminology MAY remain as inline code.
* Use the [Scripts README](../../scripts/README.md) for Markdown link validation and repair instructions.

# Writing and evidence

* Write concise, concrete, scannable Markdown in plain language. Lead with the conclusion, use present tense and active voice, and prefer meaningful headings, lists, and tables over dense prose.
* Current-state documentation SHOULD use timeless wording. Terms such as `eventually`, `later`, `planned`, `target`, `candidate`, `new`, `currently`, and `not yet` are review signals that content may belong in the roadmap or need more precise wording.
* Repository claims MUST be verified against their canonical artifacts. Commands and examples MUST be valid for the documented branch and environment.
* External factual claims SHOULD cite primary, authoritative sources. Do not copy external material when a durable pointer is sufficient.
* Documentation MUST NOT invent behavior, rationale, fields, commands, contracts, or commitments. Unresolved future questions belong in the relevant roadmap stage.

# Change discipline

* A change to documented behavior, contracts, commands, deployment, structure, or active constraints MUST update its canonical documentation in the same change.
* Removing or superseding behavior MUST also remove or update its current-state documentation and inbound navigation.
* Documentation changes SHOULD be reviewed like code, including checks for accuracy, duplication, valid links, scope placement, and readable structure.
* Human and AI authors follow the same rules. AI-authored content requires the same source inspection, verification, and review as human-authored content.

# Diagrams

* Use Mermaid when a flow, relationship, hierarchy, state, or system boundary is clearer visually than in prose.
* Do not create a diagram when a short paragraph, list, or table is clearer.
* Diagrams must add clarity, use canonical terminology, and be updated with the documentation they support.

# Markdown validation

After creating or modifying Markdown files, run the lint and link checks in the
[Scripts README](../../scripts/README.md). The repository's
[PyMarkdown configuration](../../.pymarkdown.json) defines the lint rules,
frontmatter handling, and path exclusions.

# Review checklist

Before accepting documentation, confirm that:

* the content is current truth or is placed in its owning roadmap stage;
* every substantive fact has one canonical owner;
* pointers replace repeated detail without removing necessary local context;
* claims, commands, and contracts are grounded in authoritative artifacts;
* the concept has one coherent purpose and is discoverable from an index;
* completed work has been promoted out of the roadmap without leaving duplicate detail; and
* related implementation and documentation changes travel together.

# Related concepts

These rules use the [controlled type vocabulary](../references/type-vocabulary.md).
