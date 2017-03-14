---
title: >-
  Tracking Issues with Data the Simple Way
slug: tracking-issues-with-data-the-simple-way
date: 2013-11-06T08:00:00
themes: []
tags: []
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1278
---

<p><a href="https://github.com/datasets/issues">Data Issues</a> is a prototype initiative to track “issues” with data using a simple bug tracker—in this case, GitHub Issues.</p>

<p>We’ve all come across “issues” with data, whether it’s “data” that turns out to be provided as a PDF, the many ways to badly format tabular data (<a href="http://okfnlabs.org/bad-data/ex/tfl-passenger-numbers/">empty rows, empty columns</a>, inlined metadata …), “<a href="http://okfnlabs.org/bad-data/ex/bls-us-employment/">ASCII spreadsheets</a>”, or simply erroneous data.</p>

<p>Key to starting to improve data quality is a way to report and record these issues.</p>

<p>We’ve thought about ways to address this for <a href="http://blog.okfn.org/2011/03/31/building-the-open-data-ecosystem/">quite some time</a> and, led by <a href="http://okfnlabs.org/members/pudo/">Labs member Friedrich Lindenberg</a>, even experimented with building our <a href="http://okfnlabs.org/blog/2012/07/10/dataissues.html">own service</a>. But recently, thanks to a comment from <a href="http://okfnlabs.org/members/david/">Labs member David Miller</a>, we were hit with a blinding insight: why not do the simplest thing possible and just use an <strong>existing bug tracker tool</strong>? And so was born the current version of <a href="https://github.com/datasets/issues">Data Issues based on a github issue tracker</a>!</p>

<p><img src="http://i.imgur.com/lyIJYGo.png" alt="Data Issues" /></p>

<p><em>Aside: Before you decide we were completely crazy not to see this in the first place, it should be said that doing data issues “properly” (in the medium term) probably does require something a bit more than a normal bug tracker. For example, it would be nice to be able to both pinpoint an issue precisely (e.g. the date in column 5 on line 3751 is invalid) and group similar issues (e.g. all amounts in column 7 have a commas in them). Doing this would require a tracker that was customized for data. The solution described in this post, however, seems like a great way to get started.</em></p>

<h2 id="introducing-data-issues">Introducing Data Issues</h2>

<p>Given the existence of so many excellent issue-tracking systems, we thought the best way to start is to reuse one—in the simplest possible way.</p>

<p>With <a href="https://github.com/datasets/issues">Data Issues</a>, we’re using GitHub Issues to track issues with datasets. Data Issues is essentially just a GitHub repository whose Issues are used to report problems on open datasets. Any problem with any dataset can be reported on Data Issues.</p>

<p>To report an issue with some data, just <a href="https://github.com/datasets/issues/issues/new">open an issue in the tracker</a>, add relevant info on the data (its URL, who’s responsible for it, the line number of the bug, etc.), and explain the problem. You can add labels to group related issues—for example, if multiple datasets from the same site have problems, you can add a label that identifies the dataset’s site of origin.</p>

<p>Straightaway, the issue you raise becomes a <em>public notice</em> of the problem with the dataset. Everyone interested in the dataset has access to the issue. The issue is also <em>actionable</em>: each issue contains a thread of comments that can be used to track the issue’s status, and the issue can be <em>closed</em> when it has been fixed. All issues submitted to Data Issues are visible in a central list, which can be filtered by keyword or label to zoom in on relevant issues. All of these great features come <em>for free</em> because we’re using GitHub Issues.</p>

<h2 id="get-involved">Get Involved</h2>

<p>For Data Issues to work, people need to use it. If civic hackers, journalists, and other data wranglers learn about Data Issues and start using it to track their work on datasets, we might find that the problem of tracking issues with datasets has already been solved.</p>

<p>You can also contribute by helping develop the project into something richer than a simple Issues page. One limitation of Data Issues is that raising an issue does not actually contact the parties responsible for the data. Our next goal is to automate sending along feedback from Data Issues, making it a more effective bug tracker.</p>

<p>If you want to discuss new directions for Data Issues or point out something you’ve built that contributes to the project, get in touch via the <a href="http://lists.okfn.org/mailman/listinfo/okfn-labs">Labs mailing list</a>.</p>



