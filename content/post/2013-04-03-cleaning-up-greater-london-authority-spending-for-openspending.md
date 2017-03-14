---
title: >-
  Cleaning up Greater London Authority Spending (for OpenSpending)
slug: cleaning-up-greater-london-authority-spending-for-openspending
date: 2013-04-03T07:00:00
themes: []
tags: [u'Tech']
projects: [u'Open Knowledge']
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1245
---

<p>I’ve been working to get Greater London Authority spending data cleaned up and
into <a href="http://openspending.org/">OpenSpending</a>. Primary motivation comes from this question:</p>

<blockquote>
  <p><strong>Which companies got paid the most (and for doing what)?</strong> (see this <a href="https://github.com/openspending/thingstodo/issues/5&gt;">issue for
more</a>)</p>
</blockquote>

<p>I wanted to share where I’m up to and some of the experience so far as I think
these can inform our wider efforts - and illustrate the challenges just getting
and cleaning up data. I note that the <a href="https://github.com/rgrp/dataset-gla#readme">code and README</a> for this
ongoing work is in a repo on github: <a href="https://github.com/rgrp/dataset-gla">https://github.com/rgrp/dataset-gla</a></p>

<p><a href="http://openspending.org/gb-local-gla"><img src="http://awesomeness.openphoto.me/custom/201307/gla-spend-function-476af3_870x870.jpg" alt="" /></a></p>

<h2 id="data-quality-issues">Data Quality Issues</h2>

<p>There are 61 CSV files as of March 2013 (a list can be found in <a href="https://github.com/rgrp/dataset-gla/blob/master/scrape.json&gt;">scrape.json</a>).</p>

<p>Unfortunately the “format” varies substantially across files (even though they
are all CSV!) which makes using this data real pain. Some examples:</p>

<ul>
  <li>no of fields and there names vary across files (e.g. SAP Document no vs
Document no)</li>
  <li>number of blank columns or blank lines (some files have no blank lines
(good!), many have blank lines plus some metadata etc etc)</li>
  <li>There is also at least one “bad” file which looks to be an excel file saved
as CSV</li>
  <li>Amounts are frequently formatted with “,” making them appear as strings to
computers.</li>
  <li>Dates vary substantially in format e.g. “16 Mar 2011”, “21.01.2011” etc</li>
  <li>No unique transaction number (possibly document number)</li>
</ul>

<p>They also switched from monthly reporting to period reporting (where there are 13 periods of approx 28d each).</p>

<h2 id="progress-so-far">Progress so far</h2>

<p>I do have one month loaded (Jan 2013) with a nice breakdown by “Expenditure
Account”:</p>

<p><a href="http://openspending.org/gb-local-gla">http://openspending.org/gb-local-gla</a></p>

<p>Interestingly after some fairly standard grants to other bodies, <a href="http://openspending.org/gb-local-gla/expenditure-account/542420">“Claim Settlements”</a>
comes in as the biggest item at £2.3m</p>

<ul>
  <li>Data getting archived at <a href="http://data.openspending.org/datasets/gb-local-gla/">http://data.openspending.org/datasets/gb-local-gla/</a></li>
  <li>Clean up script: <a href="https://github.com/rgrp/dataset-gla/blob/master/scripts/process.js">https://github.com/rgrp/dataset-gla/blob/master/scripts/process.js</a></li>
</ul>



