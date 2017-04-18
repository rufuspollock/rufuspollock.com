---
title: >-
  Progress on the Data Explorer
slug: progress-on-the-data-explorer
date: 2013-03-18T07:00:00
themes: []
tags: ['Tech']
projects: ['Open Knowledge']
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1246
---

<p>This is an update on progress with the <a href="http://explorer.okfnlabs.org/">Data Explorer</a> (aka Data Transformer).</p>

<p>Progress is best seen from this <a href="http://explorer.okfnlabs.org/#rgrp/e3e0b0f18dfe151f9f7e">demo which takes you on a tour of house prices and the difference between real and nominal values</a>.</p>

<p>More information on recent developments can be found below. Feedback is <em>very welcome</em> - either here or the issues <a href="https://github.com/okfn/dataexplorer">https://github.com/okfn/dataexplorer</a>.</p>

<p><a href="http://explorer.okfnlabs.org/#rgrp/e3e0b0f18dfe151f9f7e"><img src="http://i.imgur.com/WeDO0vK.png" alt="House prices tutorial" /></a></p>

<h2 id="what-is-the-data-explorer">What is the Data Explorer</h2>

<p>For those not familiar, the <a href="http://explorer.okfnlabs.org/">Data Explorer is a HTML+JS app</a> to view, visualize and process data <em>just in the browser</em> (no backend!). It draws heavily on the <a href="http://okfnlabs.org/recline/">Recline library</a> and features now include:</p>

<ul>
  <li>Importing data from various sources (the UX of this could be much improved!)</li>
  <li>Viewing and visualizing using Recline to create grids, graphs and maps</li>
  <li>Cleaning and transforming data using a scripting component that allows you to write and run javascript</li>
  <li>Saving and sharing: everything you create (scripts, graphs etc) can be saved and then shared via public URL.</li>
</ul>

<p>Note, that persistence (for sharing) is to Gists (here’s the <a href="https://gist.github.com/rgrp/e3e0b0f18dfe151f9f7e">gist for the House Prices demo linked above</a>). This has some nice benefits such as versioning; offline editing (clone the gist, edit and push); and bl.ocks.org-style ability to create a gist and have it result in public viewable output (though with substantial differences vs blocks …).</p>

<h2 id="whats-next">What’s Next</h2>

<p>There are many areas that could be worked on – a full list of <a href="https://github.com/okfn/dataexplorer/issues">issues is in github</a>. The most important I think at the moment are:</p>

<ul>
  <li><a href="https://github.com/okfn/dataexplorer/issues/88">Storing the data “locally” in the data project</a>. At present, data is always loaded from an “external” source. This probably involves extending the current Recline datastore to back on to IndexedDB.</li>
  <li>A <a href="https://github.com/okfn/dataexplorer/issues/60">better project creation &amp; data import process</a> - I think we could learn a lot from Refine here</li>
  <li><a href="https://github.com/okfn/dataexplorer/issues/84">“Fork” support</a></li>
  <li>More <a href="https://github.com/okfn/dataexplorer/issues/52">documentation and tutorials especially for scripting</a></li>
  <li>Getting rid of the many rough edges especially on the UX side of things!</li>
</ul>

<p>I’d very interested in people’s thoughts on the app so far and what should be done next and code contributions are also very welcome (the app has already benefitted from the efforts of many people including the likes of <a href="http://mk.ucant.org/">Martin Keegan</a> and <a href="https://github.com/michael">Michael Aufreiter</a> to the app itself; and from folks like <a href="http://maxogden.com/">Max Ogden</a>, <a href="http://pudo.org/">Friedrich Lindenberg</a>, <a href="http://casbon.me/">James Casbon</a>, <a href="http://driven-by-data.net/">Gregor Aisch</a>, <a href="http://nigelb.me/">Nigel Babu</a> (and many more) in the form of ideas, feedback, work on Recline etc). </p>



