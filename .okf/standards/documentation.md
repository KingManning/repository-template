---
type: Standard
title: Documentation Standards
description: Requirements for authoring, organizing, maintaining, and reviewing the OKF knowledge bundle.
tags: [standards, documentation, governance, okf]
-------------------------------------------------


These rules govern documentation authored in `.okf/`. They supplement the format requirements in the [OKF specification](/references/okf-specification.md). `MUST` identifies a requirement; `SHOULD` identifies the expected default unless a documented reason justifies an exception.

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
* Links SHOULD use meaningful text and identify the relationship to the target. Avoid unnecessary repeat links and links that merely replace a short definition.
* Links should be in the format of [linked document's name]\(linked document's location\), e.g. [Documentation Rules](./documentation.md). Where a document has a name that may overlap, incorporate the document's location into the name e.g. [Backend README](../../backend/README.md).


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

These rules use the [controlled type vocabulary](/references/type-vocabulary.md).
