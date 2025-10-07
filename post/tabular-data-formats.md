---
title: >-
  Tabular Data Formats
slug: tabular-data-formats
date: 2011-10-09T14:04:52
themes: []
tags: ['Tech']
projects: ['Open Knowledge', 'Shuttleworth Fellowship']
posttypes: ['Updates']
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1011
---

As part of recent work on the [DataExplorer][] I've been looking into formats / schemas for tabular data and have just posted this info on the wiki:

<http://wiki.ckan.org/Data_Formats#Formats_-_Tabular>

The list is quite short and if anyone out there has useful links or comments I'd love to know more (as one example, I hear very positive things about R and its data frames but have not yet tracked down a really good overview of interface of how its designed).

Background: why are we looking at this? The immediate reason is that we want to define a lightweight intermediate format for [DataExplorer][] (and possibly the [Webstore][]) into which one can convert incoming data coming from different sources (e.g. Webstore, Google docs, OData etc) before exporting to formats needed for the display widgets (such as SlickGrid, flot, d3 etc). 

[DataExplorer]: http://wiki.ckan.org/DataExplorer
[Webstore]: http://wiki.ckan.org/Webstore

