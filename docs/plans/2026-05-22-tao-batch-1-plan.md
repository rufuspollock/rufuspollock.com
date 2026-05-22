# Tao Batch 1 Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Move the first batch of Tao material into `~/src/lifeitself/tao`, including any referenced local assets, while keeping strategy/history content in `strategy/archive`.

**Architecture:** Update the migration manifest so archive-style Tao items are explicitly scoped to `strategy/archive/`. Then move the source markdown and Excalidraw files into the Tao repo, copying any local image/diagram assets they reference so internal embeds continue to resolve. Finish by deleting the source files from `community` and verifying that all touched repos are clean.

**Tech Stack:** Markdown, Excalidraw markdown+svg pairs, local asset files, git.

---

### Task 1: Reclassify the Tao batch in the manifest

**Files:**
- Modify: `docs/plans/rufu-7la-migration-manifest.md`

**Step 1: Update targets for archive-style Tao content**

- Route `art-earth-tech.md`, `strategy-macro-to-micro-2023.md`, and the selected strategy/history Excalidraws to `strategy/archive/`
- Keep culture/practice items pointed at `culture/`

**Step 2: Verify the Tao section still reads cleanly**

- No Tao row should still point at the old `community` source paths after the move

### Task 2: Move culture/practice Tao pages

**Files:**
- Create: `~/src/lifeitself/tao/culture/five-mindfulness-trainings.md`
- Create: `~/src/lifeitself/tao/culture/integrity.md`
- Create: `~/src/lifeitself/tao/culture/shining-light.md`
- Create: `~/src/lifeitself/tao/culture/triangles.md`
- Remove: the corresponding source files from `~/src/lifeitself/community`

**Step 1: Copy the markdown content**

- Preserve frontmatter where present
- Keep relative links working

**Step 2: Remove the source copies**

- Only delete the files that were moved

### Task 3: Move archive-style strategy/history pages

**Files:**
- Create: `~/src/lifeitself/tao/strategy/archive/art-earth-tech.md`
- Create: `~/src/lifeitself/tao/strategy/archive/strategy-macro-to-micro-2023.md`
- Create: `~/src/lifeitself/tao/strategy/archive/coliving-lakes-and-streams-2018.excalidraw.md`
- Create: `~/src/lifeitself/tao/strategy/archive/research-overview-oct-2023.excalidraw.md`
- Create: `~/src/lifeitself/tao/strategy/archive/strategy-macro-to-micro-2023-02-01.excalidraw.md`
- Create: `~/src/lifeitself/tao/strategy/archive/structuring-life-itself-offers-2022-11-12.excalidraw.md`
- Remove: the corresponding source files from `~/src/lifeitself/community`

**Step 1: Copy the markdown and diagram files**

- Keep each Excalidraw `.md` paired with its `.svg`
- Leave internal wiki links pointing to the moved filenames

**Step 2: Remove source copies once the Tao versions are in place**

- Do not remove unrelated files in `community`

### Task 4: Verify assets and links

**Files:**
- No new files

**Step 1: Check for referenced local assets**

- Copy any local image or diagram assets referenced by the moved notes

**Step 2: Verify git status in `community` and `tao`**

- Confirm only the intended moves remain

