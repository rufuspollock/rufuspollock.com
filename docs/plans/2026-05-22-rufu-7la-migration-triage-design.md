---
title: Rufu-7la Migration Triage Design
created: 2026-05-22
status: approved
task: rufu-7la
---

# Rufu-7la Migration Triage Design

## Goal

Analyze the markdown checkout of `notes.lifeitself.org` at `~/src/lifeitself/community` and produce a migration manifest before moving content.

This phase is classification only. It should decide what likely belongs on `rufuspollock.com`, what belongs in the Life Itself Tao, what belongs in the DDS course, and what should probably be dropped.

## Inputs

- Source content: `~/src/lifeitself/community`
- Life Itself Tao target/reference: `~/src/lifeitself/tao`
- DDS course target/reference: `~/src/lifeitself/dds-course`
- This site's IA reference: `info-architecture-for-this-site.md`
- Repo conventions: `README.md`

## Output

Create a migration manifest. The exact format can be markdown or CSV, but each source file should have these fields:

```yaml
source_path:
title:
description:
destination:
destination_path:
confidence:
blog_postable:
metadata_needed:
notes:
```

Field meanings:

- `source_path`: path relative to `~/src/lifeitself/community`.
- `title`: page title from frontmatter or inferred from filename/heading.
- `description`: 1-2 sentence summary of what the piece is about and why it may matter.
- `destination`: one of `rufuspollock.com`, `tao.lifeitself.org`, `dds-course`, or `drop`.
- `destination_path`: proposed target path, if obvious. Leave blank or mark `TBD` when uncertain.
- `confidence`: `high`, `medium`, or `low`.
- `blog_postable`: `yes`, `maybe`, or `no`.
- `metadata_needed`: missing or useful frontmatter such as `created`, `date`, `tags`, or `aliases`.
- `notes`: migration rationale, caveats, duplicates, link issues, or follow-up work.

## Description Rule

The `description` field should summarize the actual content, not just restate the filename.

It should be short enough to keep the manifest scannable, but specific enough to let a reviewer decide whether the classification is sensible without opening every file.

Example:

> A short reference note on Cinesomatics as a somatic inner-development practice. It may relate to developmental practices, but is thin and vendor-specific enough that it could be dropped unless it connects to a wider DDS/practices map.

## Destination Rules

Default to `rufuspollock.com` unless a file is clearly operational, course-specific, or disposable.

Use `rufuspollock.com` for:

- General or personal notes.
- Evergreen concepts, essays, and reference pages.
- Public digital garden material.
- Topics that can later be refactored into more specific homes.

Use `tao.lifeitself.org` for:

- Life Itself operations, strategy, governance, and management.
- People, initiatives, portfolio, handbooks, processes, and org-running material.
- Historical material about running Life Itself that remains useful as archive or context.
- Excalidraw files about org structure, money flows, spaces, comms, strategy, or operations.

Use `dds-course` for:

- Deliberately Developmental Spaces course material.
- Developmental practices and inner-development curriculum.
- Course scripts, readings, raw notes, diagrams, and theory directly serving the course.

Use `drop` for:

- Stale or low-value fragments.
- Duplicates.
- Source-only artifacts that do not make sense in any target.
- Thin vendor or method notes that are not worth preserving independently.

## Blog-Postability Rules

Mark `blog_postable: yes` when a piece is already essay-like or could become a public post with light cleanup.

Mark `blog_postable: maybe` when the material is promising but needs synthesis, rewriting, or merging with related notes.

Mark `blog_postable: no` for reference notes, operational documents, raw notes, diagrams, and archive material.

This decision is separate from destination. A file can belong on `rufuspollock.com` without being blog-postable.

## Metadata Rules

Metadata cleanup is secondary to destination classification. The manifest should flag likely needs rather than perform cleanup.

Common metadata needs:

- Add `created` or `date` when the source date can be inferred.
- Add `tags` for migrated notes only after destination is agreed.
- Preserve useful `aliases`.
- Note broken or source-local wiki links for later migration.

## Workflow

1. Inventory all markdown files in `~/src/lifeitself/community`.
2. Read enough of each file to classify it.
3. Produce the manifest with description, destination, confidence, and blog-postability.
4. Review uncertain or low-confidence entries.
5. Only after manifest review, implement migration phases for each destination.

## Non-Goals

- Do not move content in the triage phase.
- Do not rewrite notes during triage.
- Do not solve all metadata cleanup during triage.
- Do not redesign the site IA beyond applying the existing root-first model.

