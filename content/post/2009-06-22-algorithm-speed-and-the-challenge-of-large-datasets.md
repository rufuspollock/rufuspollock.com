---
title: >-
  Algorithm Speed and the Challenge of Large Datasets
slug: algorithm-speed-and-the-challenge-of-large-datasets
date: 2009-06-22T17:30:52
themes: [u'Information Economy', u'Notebook']
tags: [u'Tech']
projects: [u'Academia', u'EUPD']
posttypes: [u'Own Work']
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 424
---

In doing research for the [EU Public Domain project][announce] (as [here][1] and [here][2]) we are often handling large datasets, for example one national library's list of pre-1960 books stretched to over 4 million items. In such a situation, an algorithm's speed (and space) can really matter. To illustrate, consider our 'loading' algorithm -- i.e. the algorithm to load MARC records into the DB, which had the following steps:

  1. Do a simple load: i.e. for each catalogue entry create a new Item *and* new Persons for any authors listed
  2. "Consolidate" all the duplicate Persons, i.e. a Person who is really the same but for whom we create duplicate DB entries in part 1 (we can do this because MARC cataloguers try to uniquely identify authors based on name + birth date + death date).
  3. [Not discussed here] Consolidate "items" to "works" (associate multiple items (i.e. distinct catalogue entries) of, say, a Christmas Carol, to a single "work")

The first part of this worked great: on a 1 million record load we averaged between 8s and 25s (depending on hardware, DB backend etc) per thousand records with speed fairly constant throughout (so that's between 2.5 and 7.5h to load the whole lot). Unfortunately, at the consolidate stage we ran into problems: for a 1 million item DB there were several 100 thousand consolidations and we were averaging only 900s per 1000 consolidations! (This also scaled significantly with DB size: a 35k records DB averaged 55s per 1000). This would mean a full run would require several days! Even worse, because of the form of the algorithm (all the consolidation for a given person were done as a batch) we ran into memory issues on big datasets with some machines.

To address this we switched to performing "consolidation" on load, i.e. when creating each Item for a catalogue entry we'd search for existing authors who matched the information we had on that record. Unfortunately this had a huge impact on the load: time grew superlinearly and had already reached 300s per 1000 records at the 100k mark having started at 40 -- Figure 1 plots this relationship. By extrapolation, 1M records would take 100 hours plus  -- almost a week!

At this point we went back to the original approach and tried optimizing the consolidation, first by switching to pure sql and then by adding some indexes on join tables (I'd always thought that foreign keys were auto indexed but it turned out not to be the case!). The first of these changes solved the memory issues, while the second resolved the speed problems providing a speedup of more than 30x (30s per 1000 rather 900s) and reduced the processing time from several days to a few hours.

Many more examples of this kind of issue could be provided. However, this one already serves to illustrate the two main points:

  * With large datasets speed really matters
  * Even with optimization algorithms can take a substantial time to run

Both of these have a significant impact on the speed, and form, of the development process. First, because one has to spend time optimizing and profiling -- which like all experimentation is time-consuming. Second because longer run-times directly impact the rate at which results are obtained and development can proceed -- often bugs or improvements only become obvious once one has run on a large dataset, plus any change to an algorithm that alters output requires that it be rerun.

<img src='http://www.rufuspollock.org/wp-content/uploads/2009/06/speed.png' alt='speed.png' class="medium" />

<p class="caption">Figure 1: Load time when doing consolidation on load</p>

[1]:http://www.rufuspollock.org/2009/06/12/the-size-of-the-public-domain/
[2]:http://www.rufuspollock.org/2009/06/09/estimating-information-production-and-the-size-of-the-public-domain/
[announce]:http://www.rufuspollock.org/2008/05/26/public-domain-in-europe-eupd-research-project/


