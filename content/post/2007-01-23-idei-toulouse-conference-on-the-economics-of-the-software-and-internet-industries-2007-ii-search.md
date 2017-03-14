---
title: >-
  IDEI Toulouse Conference on the Economics of the Software and Internet Industries 2007: II Search
slug: idei-toulouse-conference-on-the-economics-of-the-software-and-internet-industries-2007-ii-search
date: 2007-01-23T20:23:28
themes: [u'Information Economy']
tags: []
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 157
---

Below is a summary of, and a proposal inspired by, the search roundtable which closed out the Toulouse conference. The remarks are first and following them you can find my impressionistic notes of the each of the speakers' presentations.

## Open Search: A Proposal for Regulating Search the Open Way

### Introduction

In many parts of the world today we already have a situation in which a single
search engine has a dominant market share (that is over 70%). At the same time
there is, at least for the present, substantial competition -- though entry
costs are significant and growing. In such circumstances one must be concerned
that a monopoly (or small oligopoly) will develop. Such an outcome would not
only creates significant pricing/welfare issues but would raise very serious
'cultural/social' issues -- any entity, corporate or otherwise, that operated
the sole (or only significant) search engine on the planet would wield an
absolutely immense, and likely unacceptable, degree of power over our
political, cultural and social lives.

This concern has already begun to generate a growing discussion of if, and how,
we should regulate online search. There are, however, several unattractive
features of direct regulation of search: the cost of regulation itself, the
inefficiencies arising from poor or inappropriate regulation (arising from the
inevitable information asymmetries between the regulator and the regulated)
etc.

### Open Search: A Proposal

As a result most economists (and technologists) would prefer a situation where
competition did the job of regulation. This brings me the key proposal of this
article: **there should be a concerted effort (government assisted or
otherwise) to develop an open-source enterprise search system *along with* an
associated not-for-profit *open* web search service built on top of this system**.
  
The second part of this proposal is what differentiates it from previous
discussions. It is also crucial for several reasons:

  1. Learning-by-doing ('kaizen' effect) is *the* single most important route
     to improving search quality (it is assumed that the service would also be
     run in an 'open' manner with all data and research diffused openly -- at
     least as far as that is consistent with privacy etc). Hence, to develop
     good software you need to be actively used by a significant (and diverse)
     user population.
  2. Because of the ad-funded model it is perfectly possible for the search
     service to earn significant income (less, probably, than a closed service
     would do but the first mover and open-source 'brand' advantages should be
     sizable -- look at Firefox). As a result running a complementary service
     could be a substantial source of development funds.
  3. From a societal standpoint the service is what you really care about.
     While it is true that other people could run a web service with the same
     code (exactly the point!) it would be nice to guarantee the existence of a
     service, particularly one closed associated (name/reputation) with the
     underlying software. 

These are all important points from an implementation point of view but
they say little about why this proposal is good from a viewpoint of social
welfare. The answer though is obvious:

  1. We get de facto competition from a service which prices at 'marginal cost'
     (no rent extraction)
  2. the algorithms, software and accumulated data (by no means the least
     important of the 3!) are all open and therefore there are general
     efficiency gains
  3. As everything is open we have a guarantee of/commitment to future
     competition
  4. Extra competition from entry of other service providers using the same
     codebase (NB: license would want to be of a GPL+/Affero type so that
     service providers are obliged to contribute back code improvements)
  5. Greater transparency (we know why some sites come top, why some don't).

**Some remarks on funding:** while in the long-term this 'open-search' system
could well be self-supporting financially it seems likely that it would need a
decent injection of up-front funding to get it going. Where would this money
come from? Three possibilities: a) venture capital b) government or private
donor c) the general web community. (a) seems improbable given the
not-for-profit nature of the endeavour and the complete openness of both code
and service (might be possible to modify not-for-profit to allow pay-back to
backers but this is more like a straight loan and less like a VC setup). (c) is
possible but also seems difficult -- one would be looking for significant
community support for development, testing, use and promotion but harder to see
it as a reliable source of funds, at least initially. That leaves us with (b)
up front funding from government or private charity. Given the large
technological spillovers, the clear social benefits in promoting competition
and transparency, and the 'utility-like' nature of search this would seem to be
a promising route to take.

### The Current Search Model: Existing Problems

Even without the development of a monopoly (or oligopoly) the current search
situtation gives cause for concern, as Kamal Jain (Microsoft) detailed in his
presentation on the 'ugly side' of the ad-funded search model at the Toulouse
Roundtable (see below for more info on the Roundtable). In particular:

  * Search engines are currently getting to extract all the rents from selling
    my attention (equivalently: we are selling our attention, and click-stream,
    for free). This situation does not appear to be sustainable. It is already
    being addressed in some ways -- Firefox, for example, is getting money from
    Google for clicks -- and there are plenty of other methods, for example,
    one could start a not-for-profit web proxy that auctions queries to search
    engines and then routes results to users passing money back to those users.
    Storing and selling your clickstream would be another method (this has been
    around a while but never really taken off -- perhaps because privacy stuff
    becomes too obvious and not really clear what benefits will be).
  * The funding model of search (in which search is funded by advertisers and
    free for users) may be societally inefficient. Search engines are in a
    monopolistic position vis-a-vis advertisers and therefore may a) overcharge
    advertisting (with those charges eventually passed back to users) b)
    over-provide search quality.
  * Little transparency over search engine rankings which are of
    ever-increasing commercial and social importance.

## Summary of Search Round-table

Hal Varian (Berkley and Google):

  * Don't need to worry about antitrust stuff as won't get concentration since:
    * No demand-size network effects
    * Very low switching costs
    * Differentiated users so room for several competing differentiated
      products
    * OK there are economies of scale but not strong enough to overwhelm other
      effects [ed: as you can tell i'm not convinced on this score in the long
      run]
  * Huge benefit to having an oversold vs. undersold auction in market for ads
    (compare to Klemperer on dutch 3g auction).
  * online world: 'kaizen' -- continuous improvement as cost is now so low
    (iphone takes 2 years to get to market
  * => Learning by doing like never before (new advantages for incumbents)
  * Marketing is the new finance (data + computers + models).
  * Quantitative methods really work (game theory really work).

Michael Schwarz (Yahoo):

  * advertising auctions
  * massive number of products (each term, different times, term + user click
    history, ...). Massively combinatorial auctions.
  * Is attention a normal good (IMO: yes it is, but the ultimate scarce
    resource) 
  * collusive bidding by advertisers

Kamal Jain (Microsoft):

  * The good, the bad and the (mainly) ugly of search
  * Why are search engines able to extract such rents when there is quite a bit
    of competition and differences in quality (at least among top 3-5) are
    small 
  * Because they only charge one side: the advertisers. They therefore can
    overcharge (monopoly price) and over-provide quality.
  * ed: real solution is to have some way for consumers to get paid -- that way
    users get rents rather than search engines (e.g. Firefox with money for
    clicks, what about a search engine proxy -- see my comments below for more
    on this).
  * self-bidding: google take advertising slots on their own engine which
    pushes up bids (cf. Varian's example above about discontinuity between
    over-sold and under-sold auctions). With self-bidding many of the standard
    results in auction theory no longer go through.
  * google checkout: 20% discount for checkout users is a clever way to
    increase payments of non-participating advertisers (auction is
    second-price)
  * incentives for search engines to conceal information that conflicts with
    their advertisers interests (example from Page and Brin 1998 about
    cell-phone radiation risk and cell-phone advertisers)
  * decrease quality of commercial search side to force merchants to buy
    advertisements
  * google pack ad-blocker does not block Google syndicate ads
  * value of diversity: every search engine has bias/different results. As
    search engines become more important as gate-keepers one search engine
    means one single controller of our access to information. [ed: this really
    leads us towards regulating search as a traditional utility with a
    potential natural monopoly]

Steven Crossan (Google):
  
  * Hal Varian said he saw lots of diversity
  * But currently see Google with a dominant share (even more dominant in
    Europe)
  * 'kaizen' affect mean that more users mean more opportunity to improve
  * High fixed costs (but not that high)
  * Not a lot of a barriers to entry in terms of ideas (IR is well known)
  * BUT don't do versioning just have continuous improvement and there are a
    lot of them so HARD to replicate on the ground (lots of engineers for a lot
    of time)
  * So where would a challenge to a "monopolist of near-monopolist" like Google
    come from?
  * Answer 1: radical/disruptive innovation (discontinuity in algorithm
    quality) -- particularly since fixed costs of entry are low [ed: disputable
    to my mind as data centres are costly but ...]
  * Answer 2: open source [ed: but this doesn't work here so much as you need
    to fund the service at least if you want to do 'kaizen']. "If I were
    microsoft I would be open-sourcing my search engine".
  * The search box as the new command line: "move 500 euros to my savings
    account", "show me my wedding photos" [ed: this is google desktop and as he
    acknowledged pretty old hat -- natural language command line research has
    been around a long time but is just hard to do. Also though a single unified
    simplified interface might be a very good idea really don't want this
    interface (and all the apis to it) controlled by a single vendor -- should
    be open].

Francois Bourdoncle (Exalead):

  * costs of setting up search engine are high: their system is 3 million lines
   of code (a complete operating system is ~16 million) and took 5-6 years to
   develop.
  * not at the end of the road for entry into search but we are for advertising
    (just to hard to enter and exalead partner with yahoo for advertising
    stuff)
  * pages indexed: google 18 billion, yahoo 14 billion, exalead 8, msn 7, ask
    3.
  * major ongoing (or coming) wars:
    * telcos and isps vs. search engines (e.g. orange)
    * media companies (e.g. Largardere)
    * Advertisement companies (e.g. WPP)
  * SEs becoming global media brands (e.g. Google News) -- this will threaten
    traditional entities
  * "Free software is a threat" [ed: i assume he means to his type of
    enterprise]


