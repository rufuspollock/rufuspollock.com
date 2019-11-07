---
title: "My Setup for Getting Things Done"
date: 2019-11-06
themes: ["Misc"]
posttype: notebook
featured: no
slug: getting-things-done-my-setup
tags: ["patterns"]
---

This post details my personal setup for implementing Getting Things Done. It follows on from [my post earlier this year summarizing the Getting Things Done process][gtd].

[gtd]: /2019/05/27/getting-things-done/

## Setup Infrastructure

This is how I set up all the "infrastructure". The three main things you need are:

1. A primary capture / inbox tool => Todoist
2. The main processing lists (Next, Projects, Someday Maybe, Tickler etc) => Todoist
    * Preferentially these would be in same location as the inbox for easy movement of tasks
3. A reference / filing system => files + git with some stuff in GDrive
    * I imagine most people would just use their hard disk plus sync to their cloud drive of choice. I used git as I prefer markdown files, a proper editor like vim and the command line.

### Inbox plus Primary Lists => Todoist

**Todoist is the primary app for personal capture and key lists**

*NB: If you want labels (context) you need to go premium. Todoist is great so I heartily recommend this.*

What lists go where?

* Inbox (personal) = Todoist Inbox
* Next = todoist
* Tickler = todoist with dates
* Someday maybe = todoist with date
  * Movies
  * Books

* Waiting for: ??  followupthen
  * Meeting agendas



#### Reasons for Choosing Todoist

Criteria

* offline and online
* phone and computer (and syncable)
* could handle at least personal inbox and probably next list (plus more)
* easy to add to from current inboxes e.g. gmail etc
* reasonable UI for fast use

Options considered vs todoist

* plain text files (+ git)
  * why not: sync problem
    * investigated git on phone but a bit of pain. Could use dropbox but yet another service
    * plus you have to commit every time
    * editing is not as convenient and especially moving things between lists
  * why: really simple tech, open source, etc etc
* google tasks
  * difficult to move lists
  * offline on desktop unclear
* android tasks (fork of astrid) - syncs with gtasks
* trello: desktop offline support does not work, proprietary and getting restrictive (i had moved off todoist to this 5m ago)
* other task apps: not really considered (checked some of them out when selecting todoist 7m ago)
* gdocs or similar - no advantages much over plain text files in synccing (maybe a bit better) but much to complex and don't like editor (want plain text as much as possible) and no easy set up for moving between stuff

### Setup Todoist with Lists as Projects

Use projects for key lists:

* Next
* Projects
* Waiting For
* Someday Maybe

I also added:

* Books
* Music
* Movies

Use labels for contexts e.g.

* @phone
* @computer
* @shopping

#### Discussion of use of projects vs labels for lists in todoist

Projects vs labels in todoist

* Projects can be shared (do i ever want to share)? Labels can't be?  => Answer no, i don't think so ...
* Item can be in one and only one project => you can't have something in two areas
* Am i using todoist to plan my projects? No i don't think so ...
* Things with labels don't move out of inbox but those with projects do ...
* Things with priority don't move out of inbox.

Options:

A. use projects as "projects" and actually do more task management in todoist. I then need something to designate lists, options:

  * labels: e.g. @next, @someday etc
  * p3 for next, p4 for someday
  * use dates (a la JoeMc) where anything with a due next in next 2w is in next, project wishlist for someday ...

B. Use projects for lists and labels for any project classification i want


I prefer B because I want to avoid starting to do PM in todoist. Project analysis and subtask analysis can happen elsewhere. Todoist is for GTD approach for now.


### For Reference (and Project Support) use Git (+ Gitlab) with GDrive for Personal

For notebook (reference) and projects => 

* main (computer): git repo with plain text
* phone: notebook = google keep (i'd prefer something with an API)
  * annoying things about keep: proprietary, no API, character limit, no markdown
  * great things: nice simple UX, add images etc very easily

For admin / private => personal gdrive

#### Analysis

Desiderata:

* E: Accessible on my laptop including offline
* E: synced to "cloud"
* E: quick to edit, quick to file
* D: Accesible on my phone (esp for book noting)
* NTH: Can save to it from email or from web
* NTH: can share easily (for some personal stuff e.g. finances?)

Options

* gdrive - proprietary, offline is painful (with multiple accounts)
* git(lab) - open source, will be around forever, great offline and online (not so good on phone but that is limited)


## First pass on Capture Process

### Capture locations

Incoming locations

* All emails ...
* github
* gitlab
* todoist
* All existing todo list, lists including for work
* All places on my hard disk ... 
* My mini-cupboard / desk at home

Going forward

* todoist
* email


## Continuing Process

* [ ] Set up locations
* [ ] Communicate to colleagues how to notify me
* [ ] Calendar regular review times

### Capture Locations

* todoist
* email

## FAQs

* How do you deal with physical stuff (letters etc)? Ans: Will usually scan or take a picture

