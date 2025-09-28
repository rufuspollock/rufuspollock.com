# Plan

*Updated: 2025-09-28*

 Refactor from the original Hugo website to a digital garden, flowerhow setup. All content at the root or organized in subfolders.

## Tasks

### Refactor

Goal

- [ ] Remove hugo stuff and move all content into a natural structure at root

Analysis

- [x] Review the current content and triage e.g. move, delete, refactor etc **✅2025-09-28 done. created tasks below**

Removals

- [ ] `archetypes/**`, offthecuff.md (archive for re-adding), `layouts/**`
- [ ] Various `static` stuff that is for design e.g. `css, fonts, js, scss`
- [ ] `resources`
- [ ] build stuff for .gitlab (minor)

Home page

- [ ] Refactor current content
    - [ ] Move content/* to root
    - [ ] Rename `_index.md` to index.md in all folders
    - [ ] Review markdown for conversions needed
- [ ] Home page
    - [ ] Move README.md to CONTRIBUTING.md
    - [ ] Try and resurrect home page (crudely from `layouts/index.html`)

### Setup new site on flowershow

- [ ] Setup site on https://flowershow.app
- [ ] Setup a domain (test one first) e.g. new.rufuspollock.com

## Notes

Questions

- [x] Do i have everything in a subdirectory and keep README at root? **✅2025-06-05 No, we want this intuitive and everything at the root**
- [x] In that case, do I have a README for repo or use that as the landing page? **✅2025-06-05 just use that as a landing page for now. maybe in future can have Flowershow config to use e.g. index.md as the landing page and README for github users** 

### Asides

- [ ] Thoughts re how we process markdown vs mdx in 💐. atm we process everything as mdx. my sense is it would be good to default to md and only have mdx when we actually use components. or is this complicated because in the backend we are injecting mdx into the markdown pages??


# Stuff to reintegrate

- [ ] rename old `projects/` stuff to `ideas/` with redirects
## offthecuff.md (not showing anyway on old website)

```md
---
title: Aphorisms
date: 2017-04-30
---

Gibson's sprawl trilogy still the best vision of the #DigitalDystopia we are getting from a #Closed #DigitalEconomy

#Closed #DigitalEconomy and its inequality, dictatorship and stifled creativity are not inevitable #ChooseOpen

Gibson's dystopian visions of our cyber future are still our best guide to our #Digital fture if we stay #Closed - #ChooseOpen
```
