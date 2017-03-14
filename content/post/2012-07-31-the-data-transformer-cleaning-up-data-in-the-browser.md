---
title: >-
  The Data Transformer - Cleaning Up Data in the Browser
slug: the-data-transformer-cleaning-up-data-in-the-browser
date: 2012-07-31T07:00:00
themes: []
tags: [u'Tech']
projects: [u'Open Knowledge']
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1254
---

<p>This a brief post to announce an alpha prototype version of the Data Transformer, an app to let you clean up data in the browser using javascript:</p>

<p><a href="http://transformer.datahub.io/">http://transformer.datahub.io/</a></p>

<h3 id="m-overview-video">2m overview video:</h3>

<iframe width="560" height="315" src="http://www.youtube.com/embed/zM1USNaEcVQ" frameborder="0" allowfullscreen="1" style="margin-bottom: 30px;">&nbsp;</iframe>

<h3 id="what-does-this-app-do">What does this app do?</h3>

<ol>
  <li>You load a CSV file from github (fixed at the moment but soon to be customizable)</li>
  <li>You write simple javascript to edit this file (uses ReclineJS transform and grid views + CSV backends – here’s the <a href="http://reclinejs.com/demos/multiview/?currentView=transform">original ReclineJS transform demo</a>)</li>
  <li>You save this updated file back to github (via oauth login - this utilizes Michael’s great work in Prose!)</li>
</ol>

<p>This prototype was hacked together in an afternoon a couple of weeks ago when I was fortunate enough to spend an an afternoon with Michael Aufreiter, Chris Herwig, Mike Morris and others at the Development Seed offices. It builds on ReclineJS + oauth / github connectors borrowed from Prose.</p>

<p>It’s part of an ongoing plan to create a “Data Orchestra” of lightweight data services that can play nicely together with each
other and connect to things like the DataHub (or GitHub …): <a href="http://notebook.okfn.org/2012/06/22/datahub-small-pieces-loosely-joined/">http://notebook.okfn.org/2012/06/22/datahub-small-pieces-loosely-joined/</a></p>



