---
title: >-
  A Data API for Data Packages in Seconds Using CKAN and its DataStore
slug: a-data-api-for-data-packages-in-seconds-using-ckan-and-its-datastore
date: 2014-09-11T00:00:00
themes: []
tags: []
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1362
---

<p><code>dpm</code> the command-line ‘data package manager’ now supports pushing <a href="http://data.okfn.org/standards">(Tabular)
Data Packages</a> straight into a <a href="http://ckan.org/">CKAN instance</a> (including
pushing all the data into the <a href="http://docs.ckan.org/en/latest/maintaining/datastore.html">CKAN DataStore</a>):</p>

<pre><code>dpm ckan {ckan-instance-url}
</code></pre>

<p>This allows you, in seconds, to get a fully-featured web data API – including <a href="http://docs.ckan.org/en/latest/maintaining/datastore.html#ckanext.datastore.logic.action.datastore_search">JSON</a> and
<a href="http://docs.ckan.org/en/latest/maintaining/datastore.html#ckanext.datastore.logic.action.datastore_search_sql">SQL-based</a> query APIs:</p>

<p><img src="http://assets.okfnlabs.org/p/dpm/img/dpm-ckan.gif" alt="dpm ckan demo" /></p>

<p style="text-align: center; font-size: x-small"><a href="http://assets.okfnlabs.org/p/dpm/img/dpm-ckan.gif">View fullsize</a></p>

<p>Once you have a nice web data API like this we can very easily create data-driven applications and visualizations. As a simple demonstration, there’s the <a href="http://dev.rufuspollock.org/ckan-explorer/">CKAN Data Explorer</a> (<a href="http://dev.rufuspollock.org/ckan-explorer/?endpoint=http://datahub.io&amp;resource=ea3926e3-43a8-46d0-832a-e53efd61ebb0">example with IMF data</a> - see below).</p>

<h2 id="where-can-i-find-a-ckan-instance-to-upload-to">Where Can I Find a CKAN instance to Upload to?</h2>

<p>If you’re looking for a CKAN site to upload your Data Packages to we recommend
the <a href="http://datahub.io/">DataHub</a> which is community-run and free. To upload to the DataHub
you’ll want to.</p>

<ol>
  <li>
    <p>Configure the DataHub CKAN instance in your <code>.dpmrc</code></p>

    <pre><code>[ckan.datahub]
url = http://datahub.io/
apikey = your-api-key
</code></pre>
  </li>
  <li>
    <p>Upload your Data Package</p>

    <pre><code>dpm ckan datahub --owner_org=your-organization
</code></pre>

    <p>You have to set the owner organization as all datasts on the DataHub need an
owner organization.</p>
  </li>
</ol>

<h2 id="one-i-did-earlier">One I Did Earlier</h2>

<p>Here’s a live example of one “I did earlier”:</p>

<ul>
  <li>Here’s the source Data Package: <a href="http://data.okfn.org/data/core/imf-weo">IMF World Economic Outlook in data.okfn.org
registry</a> (<a href="https://github.com/datasets/imf-weo">Data Package on github
(source)</a>)</li>
  <li>Get this on your local machine (<code>dpm install</code> or just clone the github repo)</li>
  <li>Then I uploaded it: <code>dpm ckan http://datahub.io/ --owner_org=rufuspollock</code></li>
  <li>Now it’s live on the DataHub: <a href="http://datahub.io/dataset/imf-weo">http://datahub.io/dataset/imf-weo</a>
    <ul>
      <li>Indicators: <a href="http://datahub.io/dataset/imf-weo/resource/ea3926e3-43a8-46d0-832a-e53efd61ebb0">http://datahub.io/dataset/imf-weo/resource/ea3926e3-43a8-46d0-832a-e53efd61ebb0</a></li>
      <li>Values: <a href="http://datahub.io/dataset/imf-weo/resource/24cd8ebe-fa3f-4353-9ad9-d53bd88751a6">http://datahub.io/dataset/imf-weo/resource/24cd8ebe-fa3f-4353-9ad9-d53bd88751a6</a></li>
      <li>Note this is a normalized dataset in which there are 2 tables (the
DataStore supports JOINS if we want to put them back together)</li>
    </ul>
  </li>
  <li>Here’s a sample API query to get all indicators related to GDP: <a href="http://datahub.io/api/action/datastore_search?resource_id=ea3926e3-43a8-46d0-832a-e53efd61ebb0&amp;limit=5&amp;q=GDP">http://datahub.io/api/action/datastore_search?resource_id=ea3926e3-43a8-46d0-832a-e53efd61ebb0&amp;limit=5&amp;q=GDP</a></li>
  <li>Now the data has a nice web Data API you can easily build data-driven apps or
visualizations. For example, the <a href="http://dev.rufuspollock.org/ckan-explorer/">CKAN Explorer</a> is a simple JS +
HTML app which allows you to explore CKAN DataStore data. Here’s the app
pre-loaded with the <a href="http://dev.rufuspollock.org/ckan-explorer/?endpoint=http://datahub.io&amp;resource=ea3926e3-43a8-46d0-832a-e53efd61ebb0">DataStore indicator data</a></li>
</ul>

<p>Context: a big motivation (personally) for doing this is that I’d like to see a
nice web data API available for the <a href="http://data.okfn.org/data/">“Core” Data Packages</a> we’re creating
as part of the <a href="http://data.okfn.org/">Frictionless Data effort</a>. If you’re interested
in helping, <a href="http://discuss.okfn.org/t/data-packages-creating-finding-and-tooling/48">get in touch</a>.</p>

<h2 id="links">Links</h2>

<ul>
  <li><a href="http://data.okfn.org/tools/">dpm Homepage</a></li>
  <li><a href="https://github.com/okfn/dpm">dpm on Github</a></li>
  <li><a href="https://github.com/okfn/datapackage-ckan">data package to ckan (node) library</a></li>
  <li>IRC: freenode.net Channel: #okfn</li>
</ul>



