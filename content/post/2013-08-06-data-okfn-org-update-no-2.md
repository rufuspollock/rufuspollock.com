---
title: >-
  data.okfn.org - update no. 2
slug: data-okfn-org-update-no-2
date: 2013-08-06T07:00:00
themes: []
tags: []
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1311
---

<p><a href="http://data.okfn.org/">data.okfn.org</a> is the Labs’ repository of high-quality, easy-to-use <a href="http://opendefinition.org/">open data</a>. This update summarizes some of the improvements to data.okfn.org that have taken place over the past two months.</p>

<h2 id="new-tools">New tools</h2>

<p>Several tools which make it easier to use the <a href="http://data.okfn.org/standards/data-package">Data Package standard</a> are now operational. These include a <a href="http://data.okfn.org/tools/create">Data Package creator</a>, a <a href="http://data.okfn.org/tools/view">Data Package viewer</a>, and there’s progress on a <a href="https://github.com/okfn/data.okfn.org/issues/27">validator for Data Packages</a>.</p>

<h3 id="data-package-creator">Data Package Creator</h3>

<p>Turning a CSV into a Data Package means creating a file, <code>datapackage.json</code>, which houses the metadata associated with the CSV. The <a href="http://data.okfn.org/tools/create">Data Package Creator</a> simplifies this process.</p>

<p>Provide the Creator with the URL of a CSV and it will return a well-formed JSON object with the required fields, as well as a raw JSON URL (the JSON URL serves as a basic machine accessible API).</p>

<p><img src="http://farm8.staticflickr.com/7362/9449152387_962624e792.jpg" alt="Data Package Creator in action" /></p>

<h3 id="data-package-viewer">Data Package Viewer</h3>

<p>The metadata included with Data Packages makes it possible to construct a simple view of the data. We now provide an online <a href="http://data.okfn.org/tools/view">Data Package Viewer</a> to do this for you.</p>

<p>Just provide the link to your Data Package and Viewer generates a user-friendly description, a graph of the data, and a summary of the data fields. Here, for example, is the Viewer’s display of <a href="http://data.okfn.org/tools/view?url=https://raw.github.com/rgrp/wheat-us/master/datapackage.json">US wheat production data</a>.</p>

<p><img src="http://farm6.staticflickr.com/5340/9449152367_13b33222df.jpg" alt="Data Package Viewer in action" /></p>

<h2 id="new-datasets">New datasets</h2>

<p>The biggest data news was having our first ‘out-of-the-blue’ contribution of an ‘official’ dataset! <a href="https://github.com/ewheeler">Evan Wheeler</a> pinged us to offer a comprehensive collection of <a href="http://data.okfn.org/data/country-codes-comprehensive">country codes</a> for the world’s countries in <a href="http://data.okfn.org/standards/simple-data-format">Simple Data Format</a>. Here is the:</p>

<ul>
  <li><a href="http://data.okfn.org/data/country-codes-comprehensive">Comprehensive Country Codes dataset on data.okfn.org</a> </li>
  <li><a href="https://github.com/datasets/country-codes-comprehensive">Associated GitHub repo</a> for the dataset</li>
</ul>

<p><img src="http://farm8.staticflickr.com/7324/9451935968_32719167a7.jpg" alt="Country codes data, table view" /></p>

<p>Also new: </p>

<ul>
  <li><a href="http://data.okfn.org/data/s-and-p-500">Standard and Poor’s 500 Index Data including Dividend, Earnings, and P/E Ratio</a>  (<a href="https://github.com/datasets/s-and-p-500">GitHub</a>)</li>
  <li><a href="http://data.okfn.org/data/cpi-us">US Consumer Price Index and Inflation monthly time series from January 1913</a> (<a href="https://github.com/datasets/cpi-us">GitHub</a>) </li>
</ul>

<p>If you want to contribute a new dataset, check out the <a href="http://data.okfn.org/about/contribute#data">instructions</a> and the <a href="https://github.com/datasets/registry/issues">outstanding requests</a>.</p>

<h2 id="new-standards-pages">New standards pages</h2>

<p>Among data.okfn.org’s chief purpose is promoting simple <a href="http://data.okfn.org/standards">standards for data transport</a> in the form of Data Package and Simple Data Format - helping to create a world of <a href="http://blog.okfn.org/2013/04/24/frictionless-data-making-it-radically-easier-to-get-stuff-done-with-data/">frictionless data</a>.</p>

<p>Key here is providing simple, easy-to-understand, information and so we’ve <a href="http://data.okfn.org/standards">revamped the standards page</a> and created two new pages dedicated to providing simple introduction and overview for Data Package and Simple Data Format:</p>

<ul>
  <li><a href="http://data.okfn.org/standards/data-package">Data Package Overview and Introduction</a></li>
  <li><a href="http://data.okfn.org/standards/simple-data-format">Simple Data Format Overview and Introduction</a></li>
</ul>

<h2 id="get-involved">Get involved</h2>

<p>Anyone can contribute, and it’s easy – if you can use a spreadsheet, you can help!</p>

<p>Instructions for <a href="http://data.okfn.org/about/contribute">getting involved can be found here</a>.</p>



