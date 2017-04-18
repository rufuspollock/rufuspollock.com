---
title: >-
  Talks this Week: Open Data at ESTC in Vienna and TOP-IX Annual Conference in Turin
slug: talks-this-week-open-data-at-estc-in-vienna-and-top-ix-annual-conference-in-turin
date: 2010-12-02T10:59:17
themes: ['Information Economy']
tags: []
projects: ['Open Knowledge', 'Shuttleworth Fellowship']
posttypes: ['Updates']
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 777
---

This Thursday I'm in Vienna to participate in the [Linked Open Data workshop][estc-workshop] at [ESTC 2010][estc] talking about open data on the semantic web (putting the 'open' in linked open data!). **Update: [slides from talk at ESTC][estc-slides].**

[estc]: http://www.estc2010.com/
[estc-workshop]: http://www.estc2010.com/program-menu/workshops#Linked%20Enterprise%20Data%20Workshop
[estc-slides]: http://m.okfn.org/files/talks/estc_vienna_lod_20101202/

Then on Friday (3rd Dec) I'm at the [TOP-IX Open Data conference in Torino, Italy][topix-conf] to speak on Public Sector Information and Open Data (on the 2nd fellow OKFNer Friedrich Lindenberg will be coordinating a CKAN hack day in Turin as part of the run-up to the main event). **Update: [slides from TOP-IX talk][topix-slides].**

[topix-conf]: http://conferenza.top-ix.org/?lang=en
[topix-slides]: http://m.okfn.org/files/talks/topix_turin_20101203/

## Notes from ESTC

Live notes from LOD session (no guarantee of accuracy or completeness)

### Orri Errling, OpenLink Software

  * lod-cloud.net - lod cache
  * 18 billion triples
  * 8 x 8 core, 16GB servers
  * 350m geolocations

[ed]: What's the cost (if you weren't corporate)? On, e.g. EC2 (using high memory reserved extra large), this is 8 * ~3k = 24k per year.

Reserve 16GB RAM for every billion triples

Column wise compressed storage architecture

  * Columns better for analytics
  * Rows betters for lots of transactions
  * Virtuoso moves to column based architecture

Monetdb - what can we learn from them

NoSQL - in some ways a cultural thing, a rebellion against the authority of SQL

  * Get rid of (some parts) of ACID
  * Because google were doing it people thought they should too
  * Something of a reaction now


