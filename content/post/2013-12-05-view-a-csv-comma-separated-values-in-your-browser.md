---
title: >-
  View a CSV (Comma Separated Values) in Your Browser
slug: view-a-csv-comma-separated-values-in-your-browser
date: 2013-12-05T08:00:00
themes: []
tags: []
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1305
---

<p>This post introduces one of the handiest features of <a href="http://datapipes.okfnlabs.org/">Data Pipes</a>: <strong><a href="http://datapipes.okfnlabs.org/html/">fast (pre) viewing of CSV files in your browser</a></strong> (and you can share the result by just copying a URL).</p>

<p><a href="http://datapipes.okfnlabs.org/html/"><img src="http://i.imgur.com/LKjphLo.png" alt="" /></a></p>

<h2 id="the-raw-csv">The Raw CSV</h2>

<p><a href="http://data.okfn.org/standards/csv/">CSV files are frequently used for storing tabular data</a> and are widely supported by spreadsheets and databases. However, you can’t usually look at a CSV file in your browser - usually your browser will automatically download a CSV file. And even if you <em>could</em> look at a CSV file, it is <a href="http://datapipes.okfnlabs.org/csv/?url=https://raw.github.com/okfn/datapipes/master/test/data/gla.csv">not very pleasant to look at</a>:</p>

<p><a href="http://datapipes.okfnlabs.org/csv/?url=https://raw.github.com/okfn/datapipes/master/test/data/gla.csv">
<img src="http://i.imgur.com/zVGW1zD.png" alt="Raw CSV" />
</a></p>

<h2 id="the-result">The Result</h2>

<p>But using the <a href="http://datapipes.okfnlabs.org/html/">Data Pipes <code>html</code> feature</a>, you can turn an online CSV into a pretty HTML table in a few seconds. For example, the CSV you’ve just seen would become <a href="http://datapipes.okfnlabs.org/csv/html/?url=https://raw.github.com/okfn/datapipes/master/test/data/gla.csv">this pretty table</a>:</p>

<p><a href="http://datapipes.okfnlabs.org/csv/html/?url=https://raw.github.com/okfn/datapipes/master/test/data/gla.csv"><img src="http://i.imgur.com/fbR8DvX.png" alt="CSV, HTML view" /></a></p>

<h2 id="using-it">Using it</h2>

<p>To use this service, just visit <a href="http://datapipes.okfnlabs.org/html/">http://datapipes.okfnlabs.org/html/</a> and paste your CSV’s URL into the form.</p>

<p>For power users (or for use from the command line or API), you can just append your CSV url to:</p>

<pre><code>http://datapipes.okfnlabs.org/csv/html/?url=
</code></pre>

<h3 id="previewing-just-the-first-part-of-a-csv-file">Previewing Just the First Part of a CSV File</h3>

<p>You can also extend this basic previewing using other datapipes features. For example, suppose you have a big CSV file (say with more than a few thousand rows). If you tried to turn this into an HTML table and then view in your browser, it would probably crash it.</p>

<p>So what if you could just see a part of the file? After all, you may well only be interested in seeing what that CSV file looks like, not every row. Fortunately, <strong>Data Pipes supports only showing the first 10 lines of a CSV file</strong> using a <a href="http://datapipes.okfnlabs.org/head"><code>head</code> operation</a>. To demonstrate, let’s just extend our example above to use <code>head</code>. This gives us the following URL (click to see the live result):</p>

<p><code><a href="http://datapipes.okfnlabs.org/csv/head/html/?url=https://raw.github.com/okfn/datapipes/master/test/data/gla.csv">http://datapipes.okfnlabs.org/csv/<strong>head</strong>/html/?url=https://raw.github.com/okfn/datapipes/master/test/data/gla.csv</a></code></p>

<h2 id="colophon">Colophon</h2>

<p>Data Pipes is a free and open service run by <a href="http://okfnlabs.org/">Open Knowledge Foundation Labs</a>. You can find the source code on GitHub at: <a href="https://github.com/okfn/datapipes">https://github.com/okfn/datapipes</a>. It also available as a <a href="http://nodejs.org/">Node</a> library and command line tool.</p>

<p>If you like previewing CSV files in your browser, you might also be interested in the <a href="https://chrome.google.com/webstore/detail/recline-csv-viewer/ibfcfelnbfhlbpelldnngdcklnndhael">Recline CSV Viewer</a>, a Chrome plugin that automatically turns CSVs into searchable HTML tables in your browser.</p>


