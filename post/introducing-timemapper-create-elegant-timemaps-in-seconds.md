---
title: >-
  Introducing TimeMapper - Create Elegant TimeMaps in Seconds
slug: introducing-timemapper-create-elegant-timemaps-in-seconds
date: 2013-10-11T07:00:00
themes: []
tags: []
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1310
---

<p><a href="http://timemapper.okfnlabs.org/">TimeMapper</a> lets you create elegant and embeddable timemaps quickly and easily from a simple spreadsheet.</p>

<p><a href="http://timemapper.okfnlabs.org/okfn/medieval-philosophers"><img src="http://i.imgur.com/FmPTZlr.png" alt="Medieval philosophers timemap" /></a></p>

<p>A timemap is an interactive timeline whose items connect to a geomap. Creating a timemap with TimeMapper is as easy as filling in a spreadsheet template and copying its URL.</p>

<p>In this quick walkthrough, we’ll learn how to recreate the <a href="http://timemapper.okfnlabs.org/okfn/medieval-philosophers">timemap of medieval philosophers</a> shown above using TimeMapper.</p>

<h2 id="getting-started-with-timemapper">Getting started with TimeMapper</h2>

<p>To get started, go to the <a href="http://timemapper.okfnlabs.org/">TimeMapper website</a> and sign in using your <a href="http://twitter.com/">Twitter</a> account. Then click <strong>Create a new Timeline or TimeMap</strong> to start a new project. As you’ll see, it really is as easy as 1-2-3.</p>

<p>TimeMapper projects are generated from <a href="http://docs.google.com/">Google Sheets</a> spreadsheets. Each item on the timemap – an event, an individual, or anything else associated with a date (or two, for the start and end of a period) – is a spreadsheet row.</p>

<p>What can you put in the spreadsheet? Check out the <a href="https://docs.google.com/a/okfn.org/spreadsheet/ccc?key=0AqR8dXc6Ji4JdFRNOTVYYTRqTmh6TUNNd3U2X2pKMGc#gid=0">TimeMapper template</a>. It contains all of the columns that TimeMapper understands, plus a row of cells explaining what each of them means. Your timemap doesn’t have to use all of these columns, though—it just requires a <em>Start</em> date, a <em>Title</em>, and a <em>Description</em> for each item, plus geographical coordinates for the map.</p>

<p>So you’ve put your data in a Google spreadsheet—how can you make it into a timemap? Easy! From Google Sheets, go to <strong>File -&gt; Publish to the web</strong> and hit <strong>Start publishing</strong>. Then click on your sheet’s <strong>Share</strong> button and set the sheet’s visibility to <em>Anyone who has the link can <strong>view</strong></em>. You can either copy the URL from <em>Link to share</em> and paste that URL into the box in Step 2 of the TimeMapper creation process or click on <strong>Select from Your Google Drive</strong> to just browse to the sheet. Whichever you do, then hit <strong>Connect and Publish</strong>—and voilà!</p>

<p><img src="http://i.imgur.com/5SLOURu.png" alt="Share your spreadsheet" /></p>

<p>Embedding your new timemap is just as easy as creating it. Click on <strong>Embed</strong> in the top right corner. It will pop up a snippet of HTML which you can paste into your webpage to embed the timemap. And that’s all it takes!</p>

<p><img src="http://i.imgur.com/3KWL6p6.png" alt="Embed your timemap" /></p>

<h2 id="coming-next">Coming next</h2>

<p>We have big plans for TimeMapper, including:</p>

<ul>
  <li>Support for indicating size and time on the map</li>
  <li>Quickly create TimeMaps using information from Wikipedia</li>
  <li>Connect markers in maps to form a route</li>
  <li>Options for timeline- and map-only project layouts</li>
  <li><a href="http://disqus.com/">Disqus</a>-based comments</li>
  <li>Core JS library, <strong>timemapper.js</strong>, so you can build your own apps with timemaps</li>
</ul>

<p>Check out the <a href="https://github.com/okfn/timemapper/issues">TimeMapper issues list</a> to see what ideas we’ve got and to leave suggestions.</p>

<h2 id="code">Code</h2>

<p>In terms of the internals the app is a simple node.js app with storage into s3. The timemap visualization is pure JS built using KnightLabs excellent <a href="http://timeline.knightlab.com/">Timeline.js</a> for the timeline and <a href="http://leafletjs.com/">Leaflet</a> (with OSM) for the maps. For those interested in the code it can be found at: <a href="https://github.com/okfn/timemapper/">https://github.com/okfn/timemapper/</a></p>

<h2 id="history-and-credits">History and credits</h2>

<p>TimeMapper is made possible by awesome open source libraries like <a href="http://timeline.verite.co/">TimelineJS</a>, <a href="http://backbonejs.org/">Backbone</a>, and <a href="http://leafletjs.com/">Leaflet</a>, not to mention open data from <a href="http://www.openstreetmap.org/">OpenStreetMap</a>. When we first built a TimeMapper-style site in 2007 under the title “Weaving History”, it was a real struggle over many months to build a responsive JavaScript-heavy app. Today, thanks to libraries like these and advances in browsers, it’s now a matter of weeks.</p>



