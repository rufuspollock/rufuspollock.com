---
title: >-
  Git (and Github) for Data
slug: git-and-github-for-data
date: 2013-07-02T11:02:33
themes: ['Data Systems', 'Information Economy', 'Notebook']
tags: ['Tech']
projects: ['Open Knowledge']
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1237
---

<!--magazine.image = http://i.imgur.com/9RZvCLl.png -->

<p>The ability to do “version control” for data is a big deal. There are various options but one of the most attractive is to reuse existing tools for doing this with code, like <strong>git</strong> and <strong>mercurial</strong>. This post describes a simple &#8220;data pattern&#8221; for storing and versioning data using those tools which we&#8217;ve been using for some time and found to be very effective.</p>

<h2>Introduction</h2>

<p>The ability to do revisioning and versioning data &#8211; store changes made and share them with others &#8211; especially in a distributed way would be a huge benefit to the (open) data community. I’ve discussed why at <a href="http://blog.okfn.org/2010/07/12/we-need-distributed-revisionversion-control-for-data/">some length before</a> (see also <a href="http://blog.okfn.org/2007/02/20/collaborative-development-of-data/">this earlier post</a>) but to summarize:</p>

<ul>
<li>It allows effective distributed collaboration &#8211; you can take my dataset, make changes, and share those back with me (and different people can do this at once!)</li>
<li>It allows one to track provenance better (i.e. what changes came from where)</li>
<li>It allows for sharing updates and synchronizing datasets in a simple, effective, way &#8211; e.g. an automated way to get the last months GDP or employment data without pulling the whole file again</li>
</ul>

<p>There are several ways to address the “revision control for data” problem. The approach here is to get data in a form that means we can take existing powerful distributed version control systems designed for code like <strong>git</strong> and <strong>mercurial</strong> and apply them to the data. As such, the best <a href="http://www.informationdiet.com/blog/read/we-need-a-github-for-data">github for data</a> may, in fact, be <a href="https://github.com/">github</a> (of course, you may want to layer data-specific interfaces on on top of git(hub) &#8211; this is what we do with <a href="http://data.okfn.org/">http://data.okfn.org/</a>).</p>

<p>There are limitations to this approach and I discuss some of these and alternative models below. In particular, it’s best for &#8220;<a href="http://blog.okfn.org/2013/04/26/what-do-we-mean-by-small-data/">small (or even micro) data</a>&#8221; &#8211; say, under 10Mb or 100k rows. (One alternative model can be found in the very interesting <a href="http://github.com/maxogden/dat">Dat project</a> recently started by Max Ogden &#8212; with whom I&#8217;ve <a href="http://rufuspollock.org/2011/10/17/weekly-update-rufus-pollock-2/">talked many times</a> on this topic).</p>

<p>However, given the maturity and power of the tooling &#8211; and its likely evolution &#8211; and the fact that <a href="http://blog.okfn.org/2013/04/22/forget-big-data-small-data-is-the-real-revolution/">so much data <em>is</em> small</a> we think this approach is very attractive.</p>

<h2>The Pattern</h2>

<p>The essence of the pattern is:</p>

<blockquote>
  <ol>
  <li><p><strong>Storing data as <em>line-oriented text</em> and specifically as CSV<sup id="fnref:csv"><a href="http://feedproxy.google.com/~r/okfn/~3/41g9lIOmQGo/#fn:csv" rel="footnote">1</a></sup> (comma-separated variable) files</strong>. “Line oriented text” just indicates that individual units of the data such as a row of a table (or an individual cell) corresponds to one line<sup id="fnref:line"><a href="http://feedproxy.google.com/~r/okfn/~3/41g9lIOmQGo/#fn:line" rel="footnote">2</a></sup>.</p></li>
  <li><p><strong>Use best of breed (code) versioning like git mercurial to store and manage the data</strong>.</p></li>
  </ol>
</blockquote>

<p>Line-oriented text is important because it enables the powerful distributed version control tools like <strong>git</strong> and <strong>mercurial</strong> to work effectively (this, in turn, is because those tools are built for code which is (usually) line-oriented text). It’s not just version control though: there is a <strong>large and mature set of tools</strong> for managing and manipulating these types of files (from grep to Excel!).</p>

<p>In addition to the basic pattern, there are several a few optional extras you can add:</p>

<blockquote>
  <ul>
  <li>Store the data in GitHub (or Gitorious or Bitbucket or …) &ndash; all the examples below follow this approach</li>
  <li>Turn the collection of data into a <a href="http://data.okfn.org/standards/simple-data-format/">Simple Data Format</a> <a href="http://data.okfn.org/standards/data-package/">data package</a> by adding a datapackage.json file which provides a small set of essential information like the license, sources, and schema (this column is a number, this one is a string)</li>
  <li>Add the scripts you used to process and manage data &#8212; that way everything is nicely together in one repository</li>
  </ul>
</blockquote>

<h2>What’s good about this approach?</h2>

<p>The set of tools that exists for managing and manipulating line-oriented files is <strong>huge and mature</strong>. In particular, powerful distributed version control systems like <strong>git</strong> and <strong>mercurial</strong> are already extremely robust ways to do distributed, peer-to-peer collaboration around code, and this pattern takes that model and makes it applicable to data. Here are some concrete examples of why its good.</p>

<h4>Provenance tracking</h4>

<p>Git and mercurial provide a complete history of individual contributions with &#8220;simple&#8221; provenance via commit messages and diffs.</p>

<p><img src="http://i.imgur.com/9RZvCLl.png" alt="Example of commit messages" /></p>

<h4>Peer-to-peer collaboration</h4>

<p>Forking and pulling data allows independent contributors to work on it simultaneously.</p>

<p><img src="http://i.imgur.com/ZDmoZQL.png" alt="Timeline of pull requests" /></p>

<h4>Data review</h4>

<p>By using git or mercurial, tools for code review can be repurposed for data review.</p>

<p><img src="http://i.imgur.com/txFGVLI.png" alt="Pull screen" /></p>

<h4>Simple packaging</h4>

<p>The repo model provides a simple way to store data, code, and metadata in a single place.</p>

<p><img src="http://i.imgur.com/3UQRf4V.png" alt="A repo for data" /></p>

<h4>Accessibility</h4>

<p>This method of storing and versioning data is very low-tech. The format and tools are both very mature and are ubiquitous. For example, every spreadsheet and every relational database can handle CSV. Every unix platform has a <a href="https://github.com/rgrp/command-line-data-wrangling">suite of tools</a> like grep, sed, cut that can be used on these kind of files.</p>

<h3>Examples</h3>

<p>We&#8217;ve been using with this approach for a long-time: in 2005 we first stored CSV&#8217;s in subversion, then in mercurial, and then when we switched to git (and github) 3 years ago we started storing them there. In 2011 we started the datasets organization on github which contains a <a href="https://github.com/datasets">whole list of of datasets managed according to the pattern above</a>. Here are a couple of specific examples:</p>

<ul>
<li><p><a href="https://github.com/datasets/gdp">Country, regional, and world GDP</a>, collected from the World Bank and turned into a normalized CSV. The Python script used to clean the data is included in <a href="https://github.com/datasets/gdp/tree/master/scripts">scripts</a>.</p></li>
<li><p>List of companies in <a href="https://github.com/datasets/s-and-p-500-companies">Standard &amp; Poor’s 500</a>, an index of the top 500 publicly listed stocks in the US. Includes Python scripts to process data and instructions on how to replicate cleaned data from source. This dataset provides interesting examples of <a href="https://github.com/datasets/s-and-p-500-companies/commit/7371edf0eadff2bfc0874bcd31e1ffbc1169a4c8">what diffs</a> <a href="https://github.com/datasets/s-and-p-500-companies/commit/ac0b811977ad6d36c318e6dfdf9b9cbce17064cb">look like</a>, including <a href="https://github.com/datasets/s-and-p-500-companies/commit/d0c91b90e7e8e8f92d57b04a0f22caca1f377543">bad diffs (e.g.. a column rearrange)</a>.</p></li>
</ul>

<p><em>Note</em> Most of these examples not only show CSVs being managed in github but are also <a href="http://data.okfn.org/standards/simple-data-format/">simple data format</a> <a href="http://data.okfn.org/standards/data-package/">data packages</a> – see the datapackage.json they contain.</p>

<hr />

<h2>Appendix</h2>

<h3>Limitations and Alternatives</h3>

<p>Line-oriented text and its tools are, of course, far from <em>perfect</em> solutions to data storage and versioning. They will not work for datasets of every shape and size, and in some respects they are awkward tools for tracking and merging changes to tabular data. For example:</p>

<ul>
<li>Simple actions on data stored as line-oriented text can lead to a very large changeset. For example, swapping the order of two fields (= columns) leads to a change in <em>every single line</em>. Given that diffs, merges, etc. are line-oriented, this is unfortunate.<sup id="fnref:line_diffs"><a href="http://feedproxy.google.com/~r/okfn/~3/41g9lIOmQGo/#fn:line_diffs" rel="footnote">3</a></sup></li>
<li>It works best for smallish data (e.g. &lt; 100k rows, &lt; 50mb files, optimally &lt; 5mb files). git and mercurial don&#8217;t handle big files that well, and features like diffs get more cumbersome with larger files.<sup id="fnref:s3"><a href="http://feedproxy.google.com/~r/okfn/~3/41g9lIOmQGo/#fn:s3" rel="footnote">4</a></sup></li>
<li>It works best for data made up of lots of similar records, ideally tabular data. In order for line-oriented storage and tools to be appropriate, you need the record structure of the data to fit with the CSV line-oriented structure. The pattern is less good if your CSV is not very line-oriented (e.g. you have a lot of fields with line breaks in them), causing problems for diff and merge.</li>
<li>CSV lacks a lot of information, e.g. information on the types of fields (everything is a string). There is no way to add metadata to a CSV without compromising its simplicity or making it no longer usable as pure data. You can, however, add this kind of information in a separate file, and this exactly what the <a href="http://data.okfn.org/standards/data-package/">Data Package standard</a> provides with its datapackage.json file.</li>
</ul>

<p>The most fundamental limitations above all arise from applying line-oriented diffs and merges to structured data whose atomic unit is <em>not</em> a line (its a cell, or a transform of some kind like swapping two columns)</p>

<p>The first issue discussed below, where a simple change to a table is treated as a change to every line of the file, is a clear example. In a perfect world, we’d have both a convenient structure <em>and</em> a whole set of robust tools to support it, e.g. tools that recognize swapping two columns of a CSV as a single, simple change or that work at the level of individual cells.</p>

Fundamentally a revision system is built around a diff format and a merge protocol. Get these right and much of the rest follows. The basic 3 options you have are:

1. Serialize to line-oriented text and use the great tools like git (what’s we’ve described above)
2. Identify atomic structure (e.g. document) and apply diff at that level (think CouchDB or standard copy-on-write for RDBMS at row level)
3. Recording transforms (e.g. Refine)

<p>At the Open Knowledge Foundation we built a system along the lines of (2) and been involved in exploring and researching both (2) and (3) &#8211; see <a href="http://www.dataprotocols.org/en/latest/syncing.html">changes and syncing for data on on dataprotocols.org</a>. These options are definitely worth exploring &#8212; and, for example, Max Ogden, with whom I’ve had many great discussions on this topic, is currently working on an exciting project called <a href="http://github.com/maxogden/dat">Dat</a>, a collaborative data tool which will use the <a href="http://www.dataprotocols.org/en/latest/sleep.html">“sleep” protocol</a>.</p>

<p>However, our experience so far is that the line-oriented approach beats any currently available options along those other lines (at least for smaller sized files!).</p>

<h3>data.okfn.org</h3>

<p>Having already been storing data in github like this for several years, we recently launched <a href="http://data.okfn.org/">http://data.okfn.org/</a> which is explicitly based on this approach:</p>

<ul>
<li>Data is CSV stored in git repos on GitHub at <a href="https://github.com/datasets">https://github.com/datasets</a></li>
<li>All datasets are data packages with datapackage.json metadata</li>
<li>Frontend site is ultra-simple – it just provides catalog and API and pulls data directly from github</li>
</ul>

<h3>Why line-oriented</h3>

<p>Line-oriented text is the natural form of code and so is supported by a huge number of excellent tools. But line-oriented text is also the simplest and most parsimonious form for storing general record-oriented data—and most data can be turned into records.</p>

<p>At its most basic, structured data requires a delimiter for fields and a delimiter for records. Comma- or tab-separated values (CSV, TSV) files are a very simple and natural implementation of this encoding. They delimit records with the most natural separation character besides the space, the line break. For a field delimiter, since spaces are too common in values to be appropriate, they naturally resort to commas or tabs.</p>

<p>Version control systems require an atomic unit to operate on. A versioning system for data can quite usefully treat <em>records</em> as the atomic units. Using line-oriented text as the encoding for record-oriented data automatically gives us a record-oriented versioning system in the form of existing tools built for versioning code.</p>

<div class="footnotes">
<hr />
<ol>

<li id="fn:csv">
<p>Note that,  by CSV, we really mean “DSV”, as the delimiter in the file does <em>not</em> have to be a comma. However, the row terminator <em>should</em> be a line break (or a line break plus carriage return).&#160;<a href="http://feedproxy.google.com/~r/okfn/~3/41g9lIOmQGo/#fnref:csv" rev="footnote">&#8617;</a></p>
</li>

<li id="fn:line">
<p>CSVs do not <em>always</em> have one row to one line (it is possible to have line-breaks in a field with quoting). However, most CSVs are one-row-to-one-line. CSVs are pretty much the simplest possible structured data format you can have.&#160;<a href="http://feedproxy.google.com/~r/okfn/~3/41g9lIOmQGo/#fnref:line" rev="footnote">&#8617;</a></p>
</li>

<li id="fn:line_diffs">
<p>As a concrete example, the merge function will probably work quite well in reconciling two sets of changes that affect different sets of records, hence lines. Two sets of changes which each move a column will not merge well, however.&#160;<a href="http://feedproxy.google.com/~r/okfn/~3/41g9lIOmQGo/#fnref:line_diffs" rev="footnote">&#8617;</a></p>
</li>

<li id="fn:s3">
<p>For larger data, we suggest swapping out git (and e.g. GitHub) for simple file storage like s3. Note that s3 can support basic copy-on-write versioning. However, being copy-on-write, it is comparatively very inefficient.&#160;<a href="http://feedproxy.google.com/~r/okfn/~3/41g9lIOmQGo/#fnref:s3" rev="footnote">&#8617;</a></p>
</li>

</ol>
</div>
<img src="http://feeds.feedburner.com/~r/okfn/~4/ROYMU0cRI4o" height="1" width="1"/><img src="http://feeds.feedburner.com/~r/okfn/~4/41g9lIOmQGo" height="1" width="1"/>

