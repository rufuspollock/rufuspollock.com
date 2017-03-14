---
title: >-
  Quick and Dirty Analysis on Large CSVs
slug: quick-and-dirty-analysis-on-large-csvs
date: 2013-04-11T07:00:00
themes: []
tags: [u'Tech']
projects: [u'Open Knowledge']
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1244
---

<p>I’m playing around with some large(ish) CSV files as part of a <a href="http://openspending.org/">OpenSpending</a> related data investigation to look at UK government spending last year – example question: which companies were the top 10 recipients of government money? (More details can be
found in <a href="https://github.com/openspending/thingstodo/issues/5&gt;">this issue on OpenSpending’s things-to-do repo</a>).</p>

<p>The dataset I’m working with is the consolidated spending (over £25k) by all UK goverment departments. Thanks to the efforts of of OpenSpending folks (and specifically Friedrich Lindenberg) this data is already nicely ETL’d from thousands of individual CSV (and xls) files into one big 3.7 Gb file (see below for links and details).</p>

<p>My question is what is the best way to do quick and dirty analysis on this?</p>

<p>Examples of the kinds of options I was considering were:</p>

<ul>
  <li>Simple scripting (python, perl etc)</li>
  <li>Postgresql - load, build indexes and then sum, avg etc</li>
  <li>Elastic MapReduce (AWS Hadoop)</li>
  <li>Google BigQuery</li>
</ul>

<p>Love to hear what folks think and if there are tools or approaches they would specifically recommend.</p>

<h3 id="the-data">The Data</h3>

<ul>
  <li>Here’s the <a href="http://data.etl.openspending.org/uk25k/spending-latest.csv">3.7 Gb CSV</a></li>
  <li>A <a href="http://www.dataprotocols.org/en/latest/data-packages.html">Data Package file</a> for the data describing the fields: <a href="https://raw.github.com/openspending/dpkg-uk25k/master/datapackage.json">https://raw.github.com/openspending/dpkg-uk25k/master/datapackage.json</a></li>
</ul>



