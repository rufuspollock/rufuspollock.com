---
title: >-
  Where Does My Money Go? Spending Explorer using Protovis and jQuery
slug: where-does-my-money-go-spending-explorer-using-protovis-and-jquery
date: 2010-10-27T08:50:12
themes: ['Information Economy']
tags: ['Tech']
projects: ['Open Knowledge', 'Shuttleworth Fellowship']
posttypes: ['Own Work', 'Updates']
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 729
---

Over the last couple of months I've been playing around with [Protovis][] in my spare time to create an interactive pure javascript [Government Spending
Explorer](http://rufuspollock.org/wdmmg/explorer.html) for [Where Does My Money Go?][] ([datastore api][datastore]):

[Protovis]: http://vis.stanford.edu/protovis/

  * Explorer: <http://rufuspollock.org/wdmmg/explorer.html>
  * Source: <http://bitbucket.org/okfn/wdmmg-js/src/tip/src/explorer.html>

Warning: won't work in IE (atm due to lack of svg support) and works
best (i.e. fastest) in Chrome!

I'd be interested in any feedback and any suggestions for experience with protovis or any other javascript libraries (I've also used flot and thejit a bit). In particular one thing a bit lacking currently in protovis is any animation (something that's goodin thejit ...).

Features:

 * True 'explorer': you can choose any set of breakdown 'keys' to visualize
 * Primary 'financial bubbles' view with interactive navigation into bubbles
   * Support for arbitrary depth of data 'tree' so you can keep
navigating down (though currently limited by user interface to select
at most 3 levels)
 * Multiple other visualizations including treemap, sunburst,
dendrogram and 'icicle'
 * Time support
 * View the source data in table or as json

I'm sure there's tons to improve especially on the usability (e.g.
should default labels have amounts in them?) so if you take a look
please let me know any feedback.

Some specific limitations:

 * Does not work in IE -- but hope to fix this using svg.js soon
 * Colours and general 'look' could be improved -- help wanted!
 * Occasional bugs e.g. weird redraws -- if you find one please let me know

[Where Does My Money Go?]: http://wheredoesmymoneygo.org/
[datastore]: http://data.wheredoesmymoneygo.org/api/

