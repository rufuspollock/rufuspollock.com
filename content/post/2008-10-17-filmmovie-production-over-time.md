---
title: >-
  Film/Movie Production Over Time
slug: filmmovie-production-over-time
date: 2008-10-17T12:15:49
themes: ['Information Economy']
tags: []
projects: ['Academia']
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 351
---

As part of my research work on knowledge production, particularly how it relates to the intellectual property regime I've recently been looking at film/movie production over time. Thanks to the [semi-openness](http://www.ckan.net/package/read/imdb) of <http://www.imdb.com/> we have a fairly comprehensive database of statistics available. Combining this with the excellent [IMDbPY](http://imdbpy.sourceforge.net/) scripts and my own home-brewed code and I was able to start extracting some basic information on movie production over time.

Points to note about the dataset:

  * IMDb includes information both on films scheduled to be released, in production etc. This explains why there are data points for years in the future. These values should probably be ignored.
  * It is not clear exactly how comprehensive the IMDb dataset is -- and more importantly how its comprehensiveness varies over time. One might be concerned that some periods (especially early ones) are under-represented in the database in which case the figures shown will be somewhat biased.

### Production as Number of Titles

Movie production as measured by titles has shown marked rises and falls over time. Specifically there is a major expansion in the 1910s followed by a sharp fall in the 1920s with continuing decline until the end of WWII (1945). Following that production steadily increased up until the 1990s when is started to grow much faster. By the mid 2000s the number of titles had broken the 10k a year barrier.  We do need to be cautious here, as the number of titles may be highly misleading measure of production over time (see next section). However it is reasonable can compare across countries.

<img class="medium" src='http://www.rufuspollock.org/wp-content/uploads/2008/10/production_usa.png' alt='production_usa.png' />
<p class="caption">World film (blue) and US film (red) production (number of titles)</p>

<img class="medium" src='http://www.rufuspollock.org/wp-content/uploads/2008/10/production_uk.png' alt='production_uk.png' />
<p class="caption">UK film production (number of titles).</p>

While production is substantially lower than the US the overall trend is very similar.

<img class="medium" src='http://www.rufuspollock.org/wp-content/uploads/2008/10/production_india.png' alt='production_india.png' />
<p class="caption">Indian film production (number of titles).</p>

This shows a rather different trend. First production only really begins in the mid-1920s, and perhaps most interesting of all, production actually drops from the mid-1980s through to the mid 2000s. Here, however one needs to be especially concerned about IMDb's coverage (the number of titles looks rather low particularly for recent years).

### Production as Running Time

It is not clear that the number of titles is the correct measure of film production. After all a short of 5 minutes and 2.5 hour blockbuster both get counted equally. Thus, here we use total running time as a measure of production rather than the raw number of titles. As one can see this gives a rather different picture: there is a relatively smooth (and almost linear) trend upwards from 1900 to around 1990 followed by a massive explosion.

<img class="medium" src='http://www.rufuspollock.org/wp-content/uploads/2008/10/production_by_times_all.png' alt='production_by_times_all.png' />
<p class="caption">World production (running time)</p>



