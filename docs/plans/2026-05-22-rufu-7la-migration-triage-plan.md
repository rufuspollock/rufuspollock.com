# Rufu-7la Migration Triage Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Produce a reviewed migration manifest for markdown files in `~/src/lifeitself/community`, classifying each file into `rufuspollock.com`, `tao.lifeitself.org`, `dds-course`, or `drop`.

**Architecture:** This is a content-analysis workflow. First create a complete source inventory, then fill a manifest in batches with descriptions, destinations, confidence, and blog-postability, then review low-confidence cases before any migration happens.

**Tech Stack:** Markdown, shell inventory commands, manual content review using `rg`, `find`, `sed`, and repo-local docs.

---

### Task 1: Confirm Inputs and Create Inventory

**Files:**
- Read: `README.md`
- Read: `info-architecture-for-this-site.md`
- Read: `docs/plans/2026-05-22-rufu-7la-migration-triage-design.md`
- Read: `/Users/rgrp/src/lifeitself/community/README.md`
- Read: `/Users/rgrp/src/lifeitself/tao/README.md`
- Read: `/Users/rgrp/src/lifeitself/dds-course/README.md`
- Create: `docs/plans/rufu-7la-source-inventory.txt`

**Step 1: Check the source directories exist**

Run:

```bash
test -d /Users/rgrp/src/lifeitself/community
test -d /Users/rgrp/src/lifeitself/tao
test -d /Users/rgrp/src/lifeitself/dds-course
```

Expected: all commands exit successfully.

**Step 2: Generate a complete markdown inventory**

Run:

```bash
find /Users/rgrp/src/lifeitself/community -type f -name '*.md' \
  | sed 's#^/Users/rgrp/src/lifeitself/community/##' \
  | sort > docs/plans/rufu-7la-source-inventory.txt
```

Expected: `docs/plans/rufu-7la-source-inventory.txt` contains one relative path per markdown file.

**Step 3: Count inventory entries**

Run:

```bash
wc -l docs/plans/rufu-7la-source-inventory.txt
```

Expected: count is greater than zero. Record the count in the manifest header in Task 2.

**Step 4: Commit inventory**

Run:

```bash
git add docs/plans/rufu-7la-source-inventory.txt
git commit -m "Add rufu-7la source inventory"
```

Expected: one commit containing only the inventory file.

### Task 2: Create Manifest Template

**Files:**
- Create: `docs/plans/rufu-7la-migration-manifest.md`
- Read: `docs/plans/rufu-7la-source-inventory.txt`

**Step 1: Create manifest header**

Create `docs/plans/rufu-7la-migration-manifest.md` with:

```markdown
---
title: Rufu-7la Migration Manifest
created: 2026-05-22
status: draft
source: /Users/rgrp/src/lifeitself/community
---

# Rufu-7la Migration Manifest

This manifest classifies markdown files from `notes.lifeitself.org` before any content migration.

Destination values:

- `rufuspollock.com`
- `tao.lifeitself.org`
- `dds-course`
- `drop`

Blog-postability values:

- `yes`
- `maybe`
- `no`

## Summary

- Total files:
- `rufuspollock.com`:
- `tao.lifeitself.org`:
- `dds-course`:
- `drop`:
- Low confidence:
- Blog postable `yes`:
- Blog postable `maybe`:

## Manifest

| Source | Title | Description | Destination | Target | Confidence | Blog | Metadata Needed | Notes |
|---|---|---|---|---|---|---|---|---|
```

**Step 2: Add one row per source file**

For every line in `docs/plans/rufu-7la-source-inventory.txt`, add a placeholder row:

```markdown
| `source/path.md` |  |  |  |  |  |  |  |  |
```

Expected: manifest has the same number of table rows as the inventory count.

**Step 3: Verify manifest coverage**

Run:

```bash
grep -c '^| `' docs/plans/rufu-7la-migration-manifest.md
wc -l docs/plans/rufu-7la-source-inventory.txt
```

Expected: row count equals inventory count.

**Step 4: Commit manifest template**

Run:

```bash
git add docs/plans/rufu-7la-migration-manifest.md
git commit -m "Add rufu-7la migration manifest template"
```

Expected: one commit containing the manifest template.

### Task 3: Classify Obvious Directory-Based Batches

**Files:**
- Modify: `docs/plans/rufu-7la-migration-manifest.md`
- Read: files under `/Users/rgrp/src/lifeitself/community/excalidraw/`
- Read: files under `/Users/rgrp/src/lifeitself/community/journal/`
- Read: files under `/Users/rgrp/src/lifeitself/community/projects/`
- Read: files under `/Users/rgrp/src/lifeitself/community/books/`

**Step 1: Classify Excalidraw files**

Read each Excalidraw file's `# Text Elements` section first. Classify:

- `tao.lifeitself.org` when about Life Itself org, spaces, money flows, comms, strategy, or operations.
- `rufuspollock.com` when about general intellectual maps like wisdom gap or research topology.
- `dds-course` only when directly about developmental spaces or course material.

Expected: each Excalidraw row has a 1-2 sentence description, destination, confidence, and `blog_postable: no`.

**Step 2: Classify journal files**

Read enough of each journal file to distinguish personal logs from Life Itself operational logs.

Expected:

- Personal/general journal entries usually destination `rufuspollock.com`, target `logs/YYYY-MM-DD.md`, blog `no`.
- Operational Life Itself logs usually destination `tao.lifeitself.org`, confidence `medium` unless clearly operational.

**Step 3: Classify project files**

Read each file in `projects/`.

Expected:

- Life Itself website, ecosystem, or community project work usually destination `tao.lifeitself.org`.
- General/public projects can remain `rufuspollock.com`.

**Step 4: Classify book files**

Read title/frontmatter and first section for each file in `books/`.

Expected:

- General book notes usually destination `rufuspollock.com`.
- DDS-specific readings destination `dds-course` when directly useful to course material.
- Blog-postability usually `maybe` for substantial reviews, `no` for raw notes.

**Step 5: Commit batch classification**

Run:

```bash
git add docs/plans/rufu-7la-migration-manifest.md
git commit -m "Classify rufu-7la directory batches"
```

Expected: one commit updating only the manifest.

### Task 4: Classify Root-Level Pages

**Files:**
- Modify: `docs/plans/rufu-7la-migration-manifest.md`
- Read: root-level markdown files in `/Users/rgrp/src/lifeitself/community`

**Step 1: Review each root-level source file**

For each root-level markdown file, read frontmatter, headings, and enough body text to summarize accurately.

Expected: each row has:

- `title`
- 1-2 sentence `description`
- destination
- proposed target path if obvious
- confidence
- blog-postability
- metadata notes

**Step 2: Apply default destination rules**

Use `rufuspollock.com` unless the page is clearly Life Itself operational, DDS course-specific, or disposable.

Expected examples:

- `cinesomatics.md`: likely `dds-course` or `drop`, low/medium confidence, blog `no`.
- `life-itself.md`: likely `tao.lifeitself.org`, confidence depends on content.
- General topic notes like `metacrisis.md`, `integral.md`, `spirituality.md`, `meditation.md`: likely `rufuspollock.com`.

**Step 3: Flag possible blog posts**

Mark `blog_postable: yes` only for already essay-like pieces.

Mark `blog_postable: maybe` for pieces that could become posts after synthesis.

Expected: blog-post candidates are visible by scanning the `Blog` column.

**Step 4: Commit root-level classification**

Run:

```bash
git add docs/plans/rufu-7la-migration-manifest.md
git commit -m "Classify rufu-7la root pages"
```

Expected: one commit updating only the manifest.

### Task 5: Review Low-Confidence and Cross-Repository Cases

**Files:**
- Modify: `docs/plans/rufu-7la-migration-manifest.md`
- Read as needed: `/Users/rgrp/src/lifeitself/tao`
- Read as needed: `/Users/rgrp/src/lifeitself/dds-course`

**Step 1: List low-confidence rows**

Run:

```bash
rg '\| low \|' docs/plans/rufu-7la-migration-manifest.md
```

Expected: output shows all rows needing review.

**Step 2: Compare against Tao and DDS repositories**

For each low-confidence row, search for related files in `tao` and `dds-course`.

Run examples:

```bash
rg -i "cinesomatics|somatic|developmental" /Users/rgrp/src/lifeitself/dds-course
rg -i "praxis|spaces|money flows|community" /Users/rgrp/src/lifeitself/tao
```

Expected: notes column records whether there is an obvious existing home, duplicate, or gap.

**Step 3: Update classifications**

Raise confidence where evidence is clear. Keep `low` where a human decision is still needed.

Expected: remaining `low` rows are genuinely ambiguous and have a clear question in `notes`.

**Step 4: Commit review updates**

Run:

```bash
git add docs/plans/rufu-7la-migration-manifest.md
git commit -m "Review rufu-7la ambiguous migration cases"
```

Expected: one commit updating only the manifest.

### Task 6: Add Summary Counts and Final Review Notes

**Files:**
- Modify: `docs/plans/rufu-7la-migration-manifest.md`

**Step 1: Count destination classifications**

Run:

```bash
rg -o '\| (rufuspollock.com|tao.lifeitself.org|dds-course|drop) \|' docs/plans/rufu-7la-migration-manifest.md
```

Count each destination and update the summary.

Expected: destination counts sum to total source files.

**Step 2: Count low-confidence and blog candidates**

Run:

```bash
rg '\| low \|' docs/plans/rufu-7la-migration-manifest.md
rg '\| yes \|' docs/plans/rufu-7la-migration-manifest.md
rg '\| maybe \|' docs/plans/rufu-7la-migration-manifest.md
```

Expected: summary fields are updated with counts.

**Step 3: Verify no placeholder rows remain**

Run:

```bash
rg '\| `[^`]+` \|  \|' docs/plans/rufu-7la-migration-manifest.md
```

Expected: no output. If output appears, complete those rows.

**Step 4: Add next-phase recommendations**

Add a section:

```markdown
## Recommended Migration Phases

1. Migrate high-confidence `rufuspollock.com` pages.
2. Review `blog_postable: yes` and `maybe` items for possible posts.
3. Move or sync Tao items into `~/src/lifeitself/tao`.
4. Move or sync DDS items into `~/src/lifeitself/dds-course`.
5. Decide remaining low-confidence and `drop` items.
```

**Step 5: Commit completed manifest**

Run:

```bash
git add docs/plans/rufu-7la-migration-manifest.md
git commit -m "Complete rufu-7la migration manifest"
```

Expected: one commit with the completed manifest.

### Task 7: Final Verification

**Files:**
- Read: `docs/plans/rufu-7la-source-inventory.txt`
- Read: `docs/plans/rufu-7la-migration-manifest.md`

**Step 1: Check worktree status**

Run:

```bash
git status --short
```

Expected: clean worktree.

**Step 2: Verify manifest coverage**

Run:

```bash
wc -l docs/plans/rufu-7la-source-inventory.txt
grep -c '^| `' docs/plans/rufu-7la-migration-manifest.md
```

Expected: counts match.

**Step 3: Verify no migration occurred**

Run:

```bash
git log --oneline --name-only -- docs/plans/rufu-7la-source-inventory.txt docs/plans/rufu-7la-migration-manifest.md
```

Expected: commits only add or modify planning/manifest files. No source content is moved in this phase.

