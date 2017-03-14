---
title: >-
  Update on PublicBodies.org - a URL for every part of Government
slug: update-on-publicbodies-org-a-url-for-every-part-of-government
date: 2013-05-01T07:00:00
themes: []
tags: [u'Tech']
projects: [u'Open Knowledge']
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1243
---

<p>This is an update on <a href="http://publicbodies.org/">PublicBodies.org</a> - a Labs project whose aim is to provide a “URL for every part of Government”: <a href="http://publicbodies.org/">http://publicbodies.org/</a></p>

<p>PublicBodies.org is a database and website of “Public Bodies” – that is Government-run or controlled organizations (which may or may not have distinct corporate existence). Examples would include government ministries or departments, state-run organizations such as libraries, police and fire departments and more.</p>

<p><a href="http://publicbodies.org/"><img src="http://i.imgur.com/2AbIjSu.png" alt="" style="margin-top: 15px; margin-bottom: 15px;" /></a></p>

<p>We run into public bodies all the time in projects like OpenSpending (either as spenders or recipients). Back in 2011 as part of the “Organizations” data workshop at OGD Camp 2011, Labs member Friedrich Lindenberg scraped together a first database and site of “public bodies” from various sources (primarily FoI sites like WhatDoTheyKnow, FragDenStaat and AskTheEU).</p>

<p>We’ve recently redone the site converting the sqlite DB to simple flat CSV files:</p>

<ul>
  <li>Main github repo: <a href="https://github.com/okfn/publicbodies">https://github.com/okfn/publicbodies</a></li>
  <li>Example raw CSV: <a href="https://raw.github.com/okfn/publicbodies/master/data/gb.csv">https://raw.github.com/okfn/publicbodies/master/data/gb.csv</a></li>
</ul>

<p>The site itself is now super-simple flat-files hosted on s3 (<a href="https://github.com/okfn/publicbodies/tree/master/site">build code here</a>). Here’s an example of the output:</p>

<ul>
  <li>European Parliament: <a href="http://publicbodies.org/eu/european-parliament.html">http://publicbodies.org/eu/european-parliament.html</a></li>
  <li>Associated JSON API (with CORS!) <a href="http://publicbodies.org/eu/european-parliament.json">http://publicbodies.org/eu/european-parliament.json</a></li>
</ul>

<p>The simplicity of CSV for data plus simple templating to flat-files is very attractive. There are some drawbacks such as changes to primary template resulting in a full rebuild and upload of ~6k files so, especially as the data grows, we may want to look into something a bit nicer but for the time being this works well. </p>

<h2 id="next-steps">Next Steps</h2>

<p>There’s plenty that could be improved e.g.</p>

<ul>
  <li>More data - other jurisdictions (we only cover EU, UK and Germany) + descriptions for the bodies (this could be a nice crowdcrafting app)</li>
  <li>Search and Reconciliation (via nomenklatura)</li>
  <li>Making it easier to submit corrections or additions</li>
</ul>

<p>The full list of issues is on github here: <a href="https://github.com/okfn/publicbodies/issues">https://github.com/okfn/publicbodies/issues</a></p>

<p>Help is most definitely wanted! Just grab one of the issues or <a href="http://okfnlabs.org/contact/">get in touch</a> …</p>



