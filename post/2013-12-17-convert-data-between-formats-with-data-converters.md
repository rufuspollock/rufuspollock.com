---
title: >-
  Convert data between formats with Data Converters
slug: convert-data-between-formats-with-data-converters
date: 2013-12-17T08:00:00
themes: []
tags: []
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1303
---

<p><a href="http://okfnlabs.org/dataconverters/">Data Converters</a> is a command line tool and Python library making routine data conversion tasks easier. It helps data wranglers with everyday tasks like moving between tabular data formats—for example, converting an Excel spreadsheet to a CSV or a CSV to a JSON object.</p>

<p>The current release of Data Converters can convert between Excel spreadsheets, CSV data, and JSON tables, as well as some geodata formats (with additional requirements).</p>

<p>Its smart parser can guess the types of data, correctly recognizing dates, numbers, strings, and so on. It works as easily with URLs as with local files, and it is designed to handle very large files (bigger than memory) as easily as small ones.</p>

<p><img src="http://i.imgur.com/kDDrgPW.png" alt="Data Converters homepage" /></p>

<h2 id="converting-data">Converting data</h2>

<p>Converting an Excel spreadsheet to a CSV or a <a href="http://dataprotocols.org/en/latest/json-table-schema.html">JSON table</a> with the Data Converters command line tool is easy. Data Converters is able to read XLS(X) and CSV files and to write CSV and JSON, and input files can be either local or remote.</p>

<pre><code>dataconvert simple.xls out.csv
dataconvert out.csv out.json

# URLs also work
dataconvert https://github.com/okfn/dataconverters/raw/master/testdata/xls/simple.xls out.csv
</code></pre>

<p>Data Converters will try to guess the format of your input data, but you can also specify it manually.</p>

<pre><code>dataconvert --format=xls input.spreadsheet out.csv
</code></pre>

<p>Instead of writing the converted output to a file, you can also send it to <em>stdout</em> (and then pipe it to other command-line utilities).</p>

<pre><code>dataconvert simple.xls _.json  # JSON table to stdout
dataconvert simple.xls _.csv   # CSV to stdout
</code></pre>

<p>Converting data files can also be done within Python using the Data Converters library. The <code>dataconvert</code> convenience function shares the <code>dataconvert</code> command line utility’s file reading and writing functionality.</p>

<pre><code>from dataconverters import dataconvert
dataconvert('simple.xls', 'out.csv')
dataconvert('out.csv', 'out.json')
dataconvert('input.spreadsheet', 'out.csv', format='xls')
</code></pre>

<h2 id="parsing-data">Parsing data</h2>

<p>Data Converters can do more than just convert data files. It can also parse tabular data into Python objects that captures the semantics of the source data.</p>

<p>Data Converters’ various <code>parse</code> functions each return an iterator over the records of the source data along with a metadata dictionary containing information about the data. The records returned by <code>parse</code> are not just (e.g.) split strings: they’re hash representations of the contents of the row, with column names and data types auto-detected.</p>

<pre><code>import dataconverters.xls as xls
with open('simple.xls') as f:
    records, metadata = xls.parse(f)
    print metadata
    print [r for r in records]
=&gt; {'fields': [{'type': 'DateTime', 'id': u'date'}, {'type': 'Integer', 'id': u'temperature'}, {'type': 'String', 'id': u'place'}]}
=&gt; [{u'date': datetime.datetime(2011, 1, 1, 0, 0), u'place': u'Galway', u'temperature': 1.0}, {u'date': datetime.datetime(2011, 1, 2, 0, 0), u'place': u'Galway', u'temperature': -1.0}, {u'date': datetime.datetime(2011, 1, 3, 0, 0), u'place': u'Galway', u'temperature': 0.0}, {u'date': datetime.datetime(2011, 1, 1, 0, 0), u'place': u'Berkeley', u'temperature': 6.0}, {u'date': datetime.datetime(2011, 1, 2, 0, 0), u'place': u'Berkeley', u'temperature': 8.0}, {u'date': datetime.datetime(2011, 1, 3, 0, 0), u'place': u'Berkeley', u'temperature': 5.0}]
</code></pre>

<h2 id="whats-next">What’s next?</h2>

<p>Excel spreadsheets and CSVs aren’t the only kinds of data that need converting.</p>

<p>Data Converters also supports geodata conversion, including converting between <a href="https://developers.google.com/kml/documentation/">KML</a> (the format for geographical data used in Google Maps and Google Earth), <a href="http://geojson.org/">GeoJSON</a>, and <a href="http://www.esri.com/library/whitepapers/pdfs/shapefile.pdf">ESRI Shapefiles</a>.</p>

<p>Data Converters’ ability to convert between tabular data may also grow, adding JSON support on the input side and XLS(X) support on the output side—as well as new conversions for <a href="https://github.com/okfn/dataconverters/issues/15">XML</a>, <a href="https://github.com/okfn/dataconverters/issues/11">SQL dumps</a>, and <a href="https://github.com/okfn/dataconverters/issues/7">SPSS</a>.</p>

<p>Visit the <a href="http://okfnlabs.org/dataconverters/">Data Converters home page</a> to learn how to install Data Converters and its dependencies, and check out <a href="https://github.com/okfn/dataconverters">Data Converters on GitHub</a> to see how you can contribute to the project.</p>



