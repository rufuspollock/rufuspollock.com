---
title: >-
  Recent Work on Open Economics
slug: recent-work-on-open-economics
date: 2009-01-23T10:51:20
themes: ['Information Economy']
tags: ['Tech']
projects: ['Open Knowledge']
posttypes: ['Own Work']
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 383
---

Over the Christmas break I had a chance to make some substantial improvements/additions to our [Open Economics](http://www.openeconomics.net/) including:

 1. Improved javascript graphing.
 2. Extend Millenium Development Goals package and added web interface.
 3. First efforts at 'Where Does My Money Go'
   * Aim: Dig up govt finance info and visualize the results (online)
   * <http://okfn.org/wiki/projects/Where_Does_My_Money_Go>

More details on each of these can be found below. Also we'd be delighted to here from anyone interested in getting involved in this, especially with the last item, so if interested do get in touch.

### 1. Updated javascript graphing package to use flot.

This also allows us to use javascript make the graphing stuff more
interactive, in particular to select chart type and the series to
plot. See e.g. the data on [Daily Wages of Thatchers in the Middle
Ages](http://www.openeconomics.net/plot/chart/91adda98-802a-4980-abfa-a44007a8bb2e) or [Wheat, barley, oat, mutton and wool prices, and agricultural wages, 1500-1849](http://www.openeconomics.net/plot/chart/e2021071-f299-40de-952a-f4f3b3375561).

### 2. Improved Millenium Development Goals package/dataset and added a web interface.

  * [MDG entry in the store](http://www.openeconomics.net/store/mdg/)
  * Source for MDG package: <http://knowledgeforge.net/econ/svn/trunk/econdata/mdg/>

Extended 'packagization' of the MDG data by creating a mini-domain
model and an associated sql version of data in addition to the
existing csv normalized-tabular version of the data:

<http://knowledgeforge.net/econ/svn/trunk/econdata/mdg/db.py>

This is much more convenient for analysis (e.g. finding all countries which have at least one entry for any of these 3 series between 1995 and 2005 ...). It is also essential for:

#### New web interface for Millenium Development Goals

Using the sql version of the data is was easy to build a quick-and-dirty web interface to enables one to browse and view the data quickly:

  <http://www.openeconomics.net/mdg/>

For example here's chart and data showing "Children under 5 moderately
or severely underweight, percentage" for Afghanistan, China, India,
United States:

 <http://www.openeconomics.net/mdg/view?commit=Show+Values&series=559&countries=4&countries=156&countries=356&countries=840>

### 3. First efforts at 'Where Does My Money Go'

Two parts to this project a) getting the data on government
revenue/expenditure b) displaying it nicely in a web interface.

Part (a) is encapsulated in a new ukgovfinances dataset:

 <http://knowledgeforge.net/econ/svn/trunk/econdata/ukgovfinances/>

Using this data we have made a (small) start on the web interface:

 <http://www.openeconomics.net/wdmmg/>

