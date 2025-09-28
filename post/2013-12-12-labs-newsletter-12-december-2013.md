---
title: >-
  Labs newsletter: 12 December, 2013
slug: labs-newsletter-12-december-2013
date: 2013-12-12T00:00:00
themes: []
tags: []
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1304
---

<p>We’re back after taking a break last week with a bumper crop of updates. A few things have changed: Labs activities are now coordinated entirely through GitHub. Meanwhile, there’s been some updates around the <a href="http://nomenklatura.okfnlabs.org/">Nomenklatura</a>, <a href="http://okfnlabs.org/annotator/">Annotator</a>, and <a href="http://www.dataprotocols.org/">Data Protocols</a> projects and some new posts on the <a href="http://okfnlabs.org/blog/">Labs blog</a>.</p>

<h2 id="migration-from-trello-to-github">Migration from Trello to GitHub</h2>

<p>For some time now, Labs activities requiring coordination have been organized on <a href="http://trello.com/">Trello</a>—but those days are now over. Labs has moved its organizational setup over to <a href="http://github.com/">GitHub</a>, coordinating actions and making plans by means of GitHub issues. This change comes as a big relief to the many Labs members who already use GitHub as their main platform for collaboration.</p>

<p>General Labs-related activities are now tracked on the <a href="https://github.com/okfn/okfn.github.com/issues/">Labs site’s issues</a>, and activities around individual projects are managed (as before!) through those projects’ own issues.</p>

<h2 id="new-bad-data">New Bad Data</h2>

<p>New examples of <a href="http://okfnlabs.org/bad-data/">bad data</a> continue to roll in—and we invite even more <a href="http://okfnlabs.org/bad-data/add/">new submissions</a>.</p>

<p>Bad datasets added since last newsletter include the <a href="http://okfnlabs.org/bad-data/ex/gla-spending/">UK’s Greater London Authority spend data</a> (65+ files with 25+ different structures!), <a href="http://okfnlabs.org/bad-data/ex/nature-magazine-supplementary/">Nature Magazine’s supplementary data</a> (an awful PDF jumble), and more.</p>

<h2 id="nomenklatura-new-alpha">Nomenklatura: new alpha</h2>

<p>As we’ve previously noted, Labs member <a href="http://pudo.org/">Friedrich Lindenberg</a> has been thinking about producing “a fairly radical re-framing” of the <a href="http://nomenklatura.okfnlabs.org/">Nomenklatura</a> data reconciliation service.</p>

<p>Friedrich has now released an alpha version of a new release of Nomenklatura at <a href="http://nk-dev.pudo.org/">nk-dev.pudo.org</a>. The major changes with this alpha include:</p>

<ul>
  <li>A fully JavaScript-driven frontend</li>
  <li>String matching now happens inside the PostgreSQL database</li>
  <li>Better introductory text explaining what Nomenklatura does</li>
  <li>“entity” and “alias” domain objects have been merged into “entity”</li>
</ul>

<p>Friedrich is keen to hear what people think about this prototype—so jump in, give it a try, and leave your comments at the <a href="https://github.com/pudo/nomenklatura">Nomenklatura repo</a>.</p>

<h2 id="annotator-v129">Annotator v1.2.9</h2>

<p>A new maintenance release of <a href="http://okfnlabs.org/annotator/">Annotator</a> came out ten days ago. This new version is intended to be one of the last in the v1.2.x  series—indeed, v1.2.8 itself was intended to be the last, but that version had some significant issues that this new release corrects.</p>

<p>Fixes in this version include:</p>

<ul>
  <li>Fixed a major packaging error in v1.2.8. Annotator no longer exports an excessive number of tokens to the page namespace.</li>
  <li>Notification display bugfixes. Notification levels are now correctly removed after notifications are hidden.</li>
</ul>

<p>The new Annotator is available, as always, <a href="https://github.com/okfn/annotator/releases/tag/v1.2.9">from GitHub</a>.</p>

<h2 id="data-protocols-updates">Data Protocols updates</h2>

<p><a href="http://dataprotocols.org/">Data Protocols</a> is a project to develop simple protocols and formats for working with open data. <a href="http://okfnlabs.org/members/rgrp/">Rufus Pollock</a> wrote a <a href="https://lists.okfn.org/pipermail/okfn-labs/2013-December/001185.html">cross-post to the list</a> about several new developments with Data Protocols of interest to Labs. These included:</p>

<ul>
  <li>Close to final agreement on a spec for adding “primary keys” to the <a href="http://dataprotocols.org/json-table-schema/">JSON Table Schema</a> (<a href="https://github.com/dataprotocols/dataprotocols/issues/21">discussion</a>)</li>
  <li>Close to consensus on spec for “foreign keys” (<a href="https://github.com/dataprotocols/dataprotocols/issues/23">discussion</a>)</li>
  <li>Proposal for a JSON spec for views of data, e.g. graphs or maps (<a href="https://github.com/dataprotocols/dataprotocols/issues/77">discussion</a>)</li>
</ul>

<p>For more, check out <a href="https://lists.okfn.org/pipermail/okfn-labs/2013-December/001185.html">Rufus’s message</a> and the <a href="https://github.com/dataprotocols/dataprotocols/issues">Data Protocols issues</a>.</p>

<h2 id="on-the-blog">On the blog</h2>

<p>Labs members have added a couple new posts to the blog since the last newsletter. Yours truly (with extensive help from Rufus) posted on <a href="http://okfnlabs.org/blog/2013/12/05/view-csv-with-data-pipes.html">using Data Pipes to view a CSV</a>. <a href="http://okfnlabs.org/members/mihi">Michael Bauer</a>, meanwhile, wrote about the new <a href="http://okfnlabs.org/blog/2013/12/06/Introducing-Reconcile-csv.html">Reconcile-CSV service</a> he developed while working on education data in Tanzania. Look to the <a href="http://okfnlabs.org/blog/">Labs blog</a> for the full scoop.</p>

<h2 id="get-involved">Get involved</h2>

<p>If you have some spare time this holiday season, why not spend it helping out with Labs? We’re always always looking for new people to <a href="http://okfnlabs.org/join/">join the community</a>—visit the <a href="https://github.com/okfn/okfn.github.com/issues/">Labs issues</a> and the <a href="http://okfnlabs.org/ideas/">Ideas Page</a> to get some ideas for how you can join in.</p>



