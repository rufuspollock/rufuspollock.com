---
title: Research note recipe
created: 2026-10-22
---

# Research note recipe

Proto skill: how to write a note that assesses a person's or field's work
(first used for `Michael Levin.md`). Promote to a skill in the agent-skills
repo once stable.

## 1. Question tree first

Before drafting, agree the root question and sub-tree with Rufus. Default root:

> What is X claiming, how well does the evidence support it, and why does it
> matter (or why is it influential) now?

Keep **"how solid is it?"** as its own branch, separate from "what has been
shown" — merged, the note reads as hype. The tree's branches become the
note's sections. Optional last branch: "so what, for me / Life Itself" —
usually one "why I care" line in a stub.

## 2. Separate layers, tier the evidence

- **Layers:** science (results) → theory (frameworks built on them) →
  metaphysics (worldview). Say which layer each claim sits in.
- **Evidence tiers:** *solid* (peer-reviewed, independent support) · *real but
  limited* (true, but smaller than the headline) · *weak or contested* · plus
  overall caveats (replication concentrated in one lab, translation gap,
  framing inflation).

## 3. Draft from the tree

- Root at `<Full Name>.md`, `tags: [stub]`, 🌱 status line (see
  `docs/conventions.md`).
- Top: the question, a short answer, a "why I care" line.
- End with "Where to start": key paper, best talks, their own site/blog.

## 4. Fact-check before (or right after) publishing

Specific citations written from memory need checking. Hand the list of claims
(authors, year, journal, what the paper showed, titles, affiliations) to a
cheap subagent with web search; ask for CONFIRMED / WRONG / UNVERIFIED with a
source URL each. On Levin it found no outright errors but three overstatements
("his startup", gene-name case, how a result was described) — the usual
failure is overclaiming, not invention.

Record the depth of checking in the status line, e.g. "Citations checked
against abstracts, not full texts; judgements on strength of evidence are
mine."

## 5. Image

Portrait per the Images section of `docs/conventions.md`.

## 6. Publish

Push to `main` publishes the site — confirm with Rufus before each push.
