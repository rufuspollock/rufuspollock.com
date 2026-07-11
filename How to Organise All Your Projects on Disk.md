---
created: 2026-07-11
completed:
status: 🆕
priority:
kind: pattern
resolution:
status_notes:
  - 2026-07-11 wrote up the pattern after working it through.
start: "2026"
end:
---

# How to organise all your projects on disk: the `~/src/owner/project` pattern

Every project I have lives in one folder at `~/src/<owner>/<project>`. Nothing at the home root, no exceptions. That's the whole pattern — a single, predictable place for every project, grouped by who it belongs to, clean enough that I (and an AI agent) can always find things. This note is why.

One thing up front, because it's easy to misread: this isn't about code, and it isn't really about git. I organise all my _work_ this way — projects, planning, notes, knowledge, whatever I'm thinking about. My planning folder has no code in it; it's just where I think. Some of these folders sync to git and some don't — that's incidental. And `src` is only a name I kept out of habit (it once meant "source") — it could as well be `~/projects` or `~/work`. The name doesn't matter; the discipline does.

_Part of [[MOC Doing Work]]._

## The situation

I keep a lot of projects — my own things, client work, open-source I'm reading or hacking on, and a lot that's just writing and thinking. Over the years three habits piled up on top of each other:

- A good pattern that mirrors how I'm organised on GitHub: `~/src/me/`, `~/src/datopian/`, `~/src/lifeitself/`, each holding that owner's projects. This works and it runs deep.
- Flat folders in `~/src/` with no owner above them — `ckan`, `flowershow`, `ForumMagnum`, `rgrp`.
- Convenience dumps straight in `~/` — `planning`, `rufuspollock.com`, `collective-action`, `2r`. A few of these are duplicates of the copy already sitting under `~/src/me/`.

I did the home-root ones because they're quick: `cd ~`, then `cd planning`, done.

## The complication

The problem isn't that I have no pattern. I picked one years ago — group by owner, mirror GitHub — and then failed to apply it. That costs me three things.

First, ambiguity. When there are two copies of `rufuspollock.com`, which is the real one? They drift, and eventually I work in the wrong one.

Second, agents. I now run AI tooling that wants to reach across many projects at once — an orchestrator that enumerates what I'm working on. An inconsistent tree gives it nothing clean to point at.

Third, portability. I'm setting up projects on a VPS and working there with AI. If the layout on this Mac is a mess, there's no clean thing to reproduce on the next machine.

## The question

The tempting question is "owner-tier folders or flat?" — but I've already answered that; `me/datopian/lifeitself` proves I want the grouping. The one thing pulling me back toward flat folders and home-root dumps is keystrokes. So the real question is: can I make the owner tier universal without paying a typing tax every time I `cd`?

And underneath that, the one I kept snagging on: why put any of this inside `src/` at all? Why not drop the owner folders straight in my home directory and type `cd datopian`?

## The hypothesis

Yes — because layout and access are two different problems. Fix the layout with one strict rule, fix the keystrokes with tooling. Don't flatten the layout to save typing.

**The rule.** Every project lives at `~/src/<owner>/<project>`, where `owner` is whoever it belongs to (my own things go under `~/src/me/`; client and org work under `~/src/<org>/`). For anything that lives on GitHub, `owner` is just the GitHub org or user, so the two mirror each other. Nothing lives at the home root. Throwaway scratch goes in `~/scratch`, never `~`.

**Why the `src/` layer earns its place.** This was my real doubt, so let me be clear about it. `~/src` is a fence between _my projects_ and _everything else the machine owns_. My home directory isn't mine alone — it's shared with the OS and every app: `Library`, `Documents`, `Downloads`, `.config`, `.ssh`, `.cache`. Four things follow from the fence:

- a. **A clean glob.** `~/src/*/*` is every project and nothing else. Put owners at the home root and the glob becomes `~/*/*`, which also sweeps up `Documents/foo` and `Library/bar`. That's the one that matters most for the AI orchestrator — it needs a deterministic list of what I'm working on, and `~/src/*/*` is exactly that.
- b. **One root to point everything at** — backups, a `find`, a scan, an agent.
- c. **A portable anchor.** `~/src` is identical on my Mac and on a Linux VPS; the stuff below the home root differs wildly between them. Set-up on a new box targets one known path.
- d. **The keystroke cost is zero.** More on that next — which is what dissolves the whole objection.

**Access lives in tooling, not in the tree.** I set `CDPATH` so the depth is free:

```sh
export CDPATH=.:~/src/me:~/src
```

Now `cd datopian` or `cd rufuspollock.com` jumps there in one hop from anywhere. The `src/` layer costs me no keystrokes at all, so I get the cleanliness for nothing. For the three or four projects I touch daily I add plain aliases. If you have a deep or sprawling tree, [zoxide](https://github.com/ajeetdsouza/zoxide) does the same job by frecency — `z plan` — though it's an install on every machine, where `CDPATH` is already in every shell. I use `CDPATH`.

**Why this wins for agents and for new machines.** Because the tree is strict, `~/src/*/*` enumerates cleanly — owners then projects, no surprises — which is what an orchestrator needs. And because the anchor is portable, dotfiles carry the same `CDPATH` everywhere, and provisioning a new machine or VPS is just: put each project in the same `~/src/<owner>/<project>` path (clone the git ones, copy or sync the rest).

So: the layout is strict, the ergonomics live in tooling, and the machine gets something deterministic. The typing tax was never a reason to flatten — it was a reason to set `CDPATH`.

The criteria this optimises, if I name them: predictability, group-by-owner (mirroring the remote where there is one), low-friction access, cross-machine portability, and being parseable by an agent.

## Appendix: set up a new machine this way

Paste this into your favourite AI assistant on a fresh machine:

> I organise all my projects on disk as `~/src/<owner>/<project>`, where `owner` is whoever the project belongs to (my own things under `~/src/me/`, and for anything on GitHub `owner` is the GitHub org or user). Nothing lives at the home root; throwaway scratch goes in `~/scratch`. Set this machine up to match:
>
> 1. Create `~/src` and `~/scratch`.
> 2. Add `export CDPATH=.:~/src/me:~/src` to my shell rc (`~/.zshrc` or `~/.bashrc`) so I can `cd <project>` in one hop from anywhere. Tell me which file you edited.
> 3. Optionally install [zoxide](https://github.com/ajeetdsouza/zoxide) and wire it into my shell for frecency jumping.
> 4. When I ask you to add a project — cloning from git or otherwise — always put it at `~/src/<owner>/<project>`, never the home root, never a flat `~/src/<project>`.
>
> Confirm the layout rule back to me, then wait for the list of projects I want set up.
