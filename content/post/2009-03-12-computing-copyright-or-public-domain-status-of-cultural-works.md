---
title: >-
  Computing Copyright (or Public Domain) Status of Cultural Works
slug: computing-copyright-or-public-domain-status-of-cultural-works
date: 2009-03-12T12:50:20
themes: [u'Information Economy']
tags: [u'Tech']
projects: [u'Academia', u'EUPD']
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 396
---

### Background

I'm working on a EU funded project to look at the size and value of the Public Domain. This involves getting large datasets about cultural material and trying to answer questions like: How many of these items are in the public domain? What's the difference in price and availability of public domain versus non public domain items?

I've also been involved for several years in [Public Domain Works][pdw], a project to create a database of works which were in the public domain (especially recordings).

[pdw]:http://www.publicdomainworks.net/

### The Problem

Suppose we have data on cultural items such as books and recordings. For a given item we wish to:

1. Identify the underlying work(s) that item contains.
2. Identify the copyright status of that work, in particular whether it is Public Domain (PD)

Putting 1 and 2 together allows us to assign a 'copyright status' to a given item.

Aside: We have to be a bit careful here since the copyright status of an item and its work may not be exactly the same: for example, even books containing pure public domain texts may have copyright in their typesetting -- or there may be additional non-PD material such as an introduction or commentaries (though, in this case, at least theoretically, we should say the item contains 2 works a) the original PD text b) the non-PD introduction).

Note our terminology here (based off FRBR): by an 'item' we mean something like a publication be that book, recording or whatever. By a work we mean the underlying material (text, sounds etc) contained within that. So for example, Shakespeare's play "Hamlet" is a single work but there are many associated items (publications). (Note that we would count a translation of a work as a new work -- though one derived from the original work).

Almost all the data available on cultural material is about items. For example, library catalogues list items, databases listing sales (such as Nielsen) list items and online sites providing information on currently available material (along with prices) such as booksinprint, muze or even Amazon list items.


### Determining Copyright (or Public Domain) Status

With our terminology in place determining copyright status is, in theory, simple:

  1. Given information on an item match it to a work (or works).
  2. For each work obtain relevant information such as date *work* first *published* (as an *item*) and death dates of author(s)
  3. Compute copyright status based on the copyright laws for your jurisdiction.

While copyright law is not always simple, step three is generally fairly straightforward, especially if one is willing to accept something that almost but not quite 100% accurate (say 99.99% accurate).[^peterpan]

[^peterpan]: Not being 100% accurate means we can ignore some of the "special cases" and one-off exceptions in copyright law. For example, in the UK the Copyright Designs and Patents Act para 301 contains a special provision which mean that "Peter Pan" by J.M. Barrie will *never* enter the Public Domain (royalties will be payable in perpetuity for the benefit of Great Ormond Street Hospital).

What is not so straightforward are the first two steps especially step 1. This is because most datasets give only a limited amount of information on the items they contain.

Frequently information on authors will be limited or non-existent, and they certainly may not be unambiguously identified (this is especially true of datasets containing 'commercial' information such as prices and availability). Often the exact form of the title, even for the same item will vary between datasets and that leaves aside the possibility of varying titles for different titles related to the same work (is it "Hamlet" or "William Shakespeare's Hamlet" or "Hamlet by William Shakespeare" or "Hamlet, Prince of Denmark" etc).

At the same time, speed matters because the size of the datasets involved are fairly substantial. For example, there were approx 64 thousand titles that sold more than 5 copies in 2007 in the UK. If computing public domain status for each title takes 1 second then a full run will take 18 hours. If it takes 30s per title it will take 22 days.

### Some Examples

To illustrate the difficulties here I present the results of two different attempts at computing the PD status for the list of 64k titles which sold at least 5 copies in the UK in 2007.

#### Example 1: Open Library

I ran [this algorithm][1] (by_work method) against the Open Library database via their web api. This was a very slow process. First, because web apis are relatively slow and second because, perhaps due to overloading, the OL API would stop responding at some point and a manual reboot would be required (to try avoid overloading the API we'd already added a significant delay between requests -- another reason the process was quite slow). Overall it took more around 10 days to run through the whole 64k item dataset. The results were as follows:

[1]:http://knowledgeforge.net/pdw/hg/file/tip/pdw/openlibrary.py

    Total PD: 2206.0
    Total Items: 63937
    Fraction PD: 0.0345027136087
    Total Matched: 0.588469900058
 
As this shows matching was not that successful with only around 3/5 of items successfully matched. Part of this may be due to the fact that:

  * I limit the number of title matches to 10 in order to keep the time within reasonable bounds
  * The difficulty of allowing enough, but not too much, fuzziness in the matching process.

Overall, approximately 3.5% of all items were identified as PD (that being 5.8% of those actually matched). The PD determination algorithm was a conservative one with an item labelled as PD only if all authors were positively identified as PD.

Thus, this is likely to be lower bounds (at least assuming the match process was reasonable -- and allowing for the fact that some PD items included non-PD material such as commentaries). It was certainly clear from basic eyeballing that a substantial number of PD works were either not matched or not computed as PD (because of incorrect authors or missing death dates).

### Example 2

Our second algorithm ran against a local copy of Philip Harper's NGCOBA database ([data][ngcoba], [code][ngcoba-code]). The algorithm was as follows:

[ngcoba]:http://www.kingkong.demon.co.uk/ngcoba/ngcoba.htm
[ngcoba-code]:http://knowledgeforge.net/pdw/hg/file/tip/pdw/getdata/ngcoba.py

  1. Matched by title and authors.
    * If match: compute PD status strictly (all death dates known and all less than 1937)
    * Else: continue
  2. Pick first author and find all (approx) matching authors (allow extra first names)
    * If no match: Not PD
    * Intialize PD score to 0
    * For each matched author alter score in following manner:
      * If author PD: +1
      * If not PD: -3 
      * If unknown (no death_date) -0.5
    * PD if score > 0 (Else: Not PD)

This algorithm took a few hours to run (this could likely be much improved with a bit of DB optimization and a move from sqlite to something better). The results were:

    Total PD: 6404.0
    Total Items: 63917
    Fraction PD: 0.100192437067

As can be seen the fraction PD here was substantially higher at around 10%. One might be concerned that this was due to our more lenient PD algorithm (the problem was that without such 'leniency' a very large number of PD works/authors were being misclassified as not PD). However, basic eye-balling indicates that the number of false positives is not particularly high (and that there are also some false negatives).

## Summary

  1. Computing PD status is non-trivial largely because a) it is hard to match a given item to a work or person b) we lack data such as authorial death dates and dates of first publication that are required.
  2. As such we need to adopt approximate and probabilistic methods (such as the scoring approach)
  3. (Very) preliminary calculations suggest that between 3 and 10% of titles actively sold at any one time are public domain
    * NB: this does not mean 3-10% of *sales* were public domain (in fact this is very unlikely since few, if any of the best-selling items are PD)

