# Research Reclassification Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Move the two research items out of Tao and into the correct site repos before continuing the Tao migration.

**Architecture:** Update the migration manifest first so the intended destination is explicit. Then move the existing content into the target site repos, preserving frontmatter and adjusting filenames only where needed to match each repo's conventions. Finish by verifying links and git status so the classification is consistent across repos.

**Tech Stack:** Markdown files, git, local repository edits.

---

### Task 1: Reclassify the manifest

**Files:**
- Modify: `docs/plans/rufu-7la-migration-manifest.md`

**Step 1: Update the two Tao research rows**

- Move `area/research.md` to `next.lifeitself.org`
- Move `research-at-life-itself-2023.md` to `research.lifeitself.org`

**Step 2: Verify the manifest reflects the new scope**

- Confirm those two rows no longer sit under `tao.lifeitself.org`
- Leave the rest of Tao unchanged for the next migration pass

### Task 2: Move `area/research.md`

**Files:**
- Create or modify: `/Users/rgrp/src/lifeitself/next.lifeitself.org/blog/community-research-initiative.md`
- Remove: `/Users/rgrp/src/lifeitself/community/area/research.md` or the equivalent source file

**Step 1: Copy the content into the target post**

- Preserve the existing frontmatter structure used by `next.lifeitself.org`
- Keep the canonical title `Community Research Initiative`

**Step 2: Remove the source copy only after the target is in place**

- Do not touch unrelated Excalidraw material

### Task 3: Move `research-at-life-itself-2023.md`

**Files:**
- Create or modify: `/Users/rgrp/src/lifeitself/research.lifeitself.org/...`
- Remove: the corresponding source file in `community`

**Step 1: Locate the target site convention**

- Use the existing research site structure and blog naming pattern

**Step 2: Move the note as a backdated post**

- Preserve content and metadata
- Ensure the post path matches the site’s blog convention

### Task 4: Verify

**Files:**
- No new files

**Step 1: Check git status in each touched repo**

- Confirm only the intended files changed

**Step 2: Confirm the manifest is internally consistent**

- The Tao bucket should no longer include the two research items

