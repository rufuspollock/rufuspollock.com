---
created: 2025-05-12
completed:
pstatus: 🆕
priority:
kind: product
completion: 0
resolution:
est:
actual:
status_notes:
---


# Refactor to Digital Garden 2025

## Overview - 2025-05-12

Subject: updating rufuspollock.com

Question: what do i want my website to be? How do I do that? What do I start with?

Answer: i want a site that can live over the long-term as a home for my thinking and writing that is of the quality of gwern.net or similar. It is, in a perfect world, combination landing page, blog and digital garden. Most important is the digital garden. This is where i want to accumulate knowledge and insight.

- I want this to last years, maybe decades which means ...
    - i don't want to be locked into some fancy saas or other tooling that goes away or which i have to regularly upgrade.
    - => I want the underlying content to be in an open, structured format
        - =>  want to use structured text that I own and control
    - => If possible i want to be able to author the content directly with relatively mininal tools
- => I want to use markdown as the storage format, stored on my local disk in git and synced to e.g. github 
- And to publish I'm going to use Flowershow ...

Summary

- Long-term home for my thinking and especially a digital garden-esque blog experience
    - Blog
    - Ideas
    - Tao
- How do I do that?
    - Technically: use markdown + github + flowershow
    - Content wise: migrate incrementally. focus on new features i can include
- What do i start with?
    - Boot the site
    - Make a video about the project

## Video outputs


## Plan of work

## Tasks

### Converting old repo ...

- [x] Convert gitlab repo to github **✅2025-05-23 https://github.com/rufuspollock/old.rufuspollock.com**
    - [x] Switch off gitlfs
    - [x] Create repo
    - [x] Push to repo
    - [x] Branch old code and tag
- [ ] Refactor main/master for new website **🚧2025-08-25 reopened as working on this again. See REFACTOR.md** ~~**✅2025-08-25 ❌ wontfix as we doing the starting from scratch approach**~~

----

## Starting from scratch (2025-07-16 plan)

### 1. Repository & Basic Setup

- [x] Create a new git repository for the site (name TBD) **✅2025-07-16 https://github.com/rufuspollock/rufuspollock.com**
- [x] Add a README **✅2025-07-16**
- [x] Set up on Flowershow cloud **✅2025-07-16 https://my.flowershow.app/@rufuspollock/rufuspollock.com**

**⏸️2025-08-25 pausing on starting from scratch (see below) though this stuff will be useful again later**
### 2. Rough landing home page

- [ ] Sketch rough structure of homepage (can be just headings or notes)
- [ ] Decide on main sections to show on homepage (e.g. About, Ideas, Blog, TAO)
- [ ] Create placeholder content for homepage
  - [ ] Minimal title + welcome blurb
  - [ ] Basic navigation links (even if broken for now)

### 3. Ideas Catalog 🧠

- [ ] Create `ideas/` directory in content
- [ ] List current and past project ideas from Obsidian
  - [ ] Add 3–5 example ideas as Markdown files
  - [ ] Add basic frontmatter (e.g. title, status, tags)
- [ ] Create an index page for ideas
  - [ ] Use FlowerShow listing page or custom layout

### 4. Blog Setup 📝

- [ ] Create `blog/` directory
- [ ] Add 1–2 recent posts from Obsidian as test content
- [ ] Set up blog index page (chronological list)
- [ ] Create post template (or adapt from default)

## 🗂️ 5. Content Migration Planning

- [ ] Inventory old Hugo content (blog posts, pages)
- [ ] Decide what (if anything) to migrate now
- [ ] Postpone legacy migration until after launch
- [ ] Consider setting up redirect or archive link to old site

## 📬 6. Newsletter Integration (Optional for Now)

- [ ] Choose between Substack, Buttondown, or native integration
- [ ] Add placeholder signup form to homepage or footer
- [ ] Postpone full integration until rest of site is live

## 📌 7. General

- [ ] Maintain a `README.md` for the repo with goals and structure
- [ ] Keep notes in Obsidian for future tasks and ideas
- [ ] Define next milestone (e.g. public launch, content review)

# Notes

## 2025-08-25

- [x] Where have I got to?
    - [x] OK, let's look at previous videos and notes **✅2025-08-25**
- [ ] ⏭️ Brainstorm how i go about refactoring
    - [ ] Do i make repo public (does it matter??)
    - [ ] Do i record as i go along (yes i think so)
    - [ ] How do i begin e.g. do i publish it on flowershow, do i refactor a bit first?
    - [ ] How do i do the rework (do i use cursor?)

### 1. Transcript

So, to recap, where I’m at is that I had this idea to start a clean website from scratch. That’s what I did: I booted up a very basic clean website.

But then I’ve been reflecting: what would actually motivate me to do a new website? What would be exciting? What do I want it to do?

And what I realized is that I want a **digital garden aspect**. Not my whole private digital garden — I don’t want holiday notes with my partner up online — but in general I’d put as many of my ideas as possible into a public digital garden. More like open-notebook science: putting my intellectual work and notes out in the open.

The thing though is: I want some kind of **backbone** for that. Just putting up random notes doesn’t work for me. And the backbone I've wanted for a while is an **ideas catalog** to list the ideas and projects I'm working on -- or havce worked on or will work on. That would provide structure for the digital garden. Each item in the digital garden could link back to an idea. So instead of a morass of content, there’s a clear place to start and a way to orient new material.

That’s point one. It’s tied to who I am: I’m a sense-maker, and this is about making sense of the world and making my sense-making public.

Point two: when it comes to **Flower Show** and showing it off, actually refactoring my existing Hugo site into Flower Show is the better way to go. Because that’s what most people want to do — they already have a site and want to migrate, not start fresh. It’s simpler, I know what I’m doing, and I don’t need to reinvent the structure.

So I have these two things in parallel:

* On one hand, for speed and demoing, I’ll refactor my current website into Flower Show.
* On the other hand, I’ll explore the **ideas catalogue** as the backbone for my digital garden.

---

## 2. Brief Summary of the Two Points

* **Ideas Catalogue / Digital Garden Backbone**
  * Want a public digital garden, focused on intellectual/open-notebook work.
  * Needs a backbone → an **ideas catalogue** of projects, products, and hypotheses.
  * Each garden note ties back to an idea, giving coherence and orientation.

* **Refactoring Existing Website into Flower Show**

  * More practical and relatable for demoing Flower Show.
  * Easier than starting from scratch.
  * Aligns with the typical user story: migrating an existing site.

**Interrelation:**

Both approaches move toward a richer public web presence. The *ideas catalogue* provides the **long-term structural vision** (a coherent digital garden), while the *refactor* provides the **short-term pragmatic path** (quick demo and continuity). They can be pursued in parallel.

---

## 3. Scripts

### (a) Where I’m At — Turning Point

*"I’ve been reflecting on why I’m creating this new website. At first, I just spun up a clean site from scratch. But what I realized is I need to ask: what’s really motivating me? What do I want it to do? And the answer is: I want a public digital garden. A place to share my ideas openly, almost like open-notebook science."*

---

### (b) The Ideas Catalogue (YouTube Short Style)

*"Here’s the breakthrough: I don’t just want a random digital garden. I want a backbone. And for me, that’s an **ideas catalogue** — a catalogue of all the projects, products, and hypotheses I’ve worked on over time. Each note I add to the garden can tie back to an idea, so instead of a mess of notes, there’s coherence, orientation, and a place to start."*

---

### (c) Refactoring My Website (YouTube Short Style)

*"At the same time, for Flower Show, it actually makes more sense not to start from scratch but to **refactor my existing site**. That’s what most people want to do — migrate their current site into Flower Show. It’s simpler, more relatable, and a great way to quickly show what the platform can do."*
