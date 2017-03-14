---
title: >-
  Data Pipes - streaming online data transformations
slug: data-pipes-streaming-online-data-transformations
date: 2013-09-11T07:00:00
themes: []
tags: []
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1276
---

<p><strong><a href="http://datapipes.okfnlabs.org/">Data Pipes</a></strong> provides an online service built in NodeJS to do <strong>simple data transformations</strong> – deleting rows and columns, find and replace, filtering, viewing as HTML – and, furthermore, to <strong>connect these transformations together</strong> <em>Unix pipes style</em> to make more complex transformations. Because Data Pipes is a web service, data transformation with Data Pipes takes place entirely online and the results <strong>and</strong> process are completely shareable simply by sharing the URL.</p>

<h2 id="an-example">An example</h2>

<p>This takes the <a href="https://raw.github.com/okfn/datapipes/master/test/data/gla.csv">input data</a> (sourced from this <a href="http://static.london.gov.uk/gla/expenditure/docs/2012-13-P12-250.csv">original Greater London Authority financial data</a>), slices out the first 50 rows (head), deletes the first column (its blank!) (cut), deletes rows 1 through 7 (delete) and finally renders the result as HTML (html).</p>

<p><a href="http://datapipes.okfnlabs.org/csv/head%20-n%2050/cut%200/delete%201:7/html?url=https://raw.github.com/okfn/datapipes/master/test/data/gla.csv"><code>http://datapipes.okfn.labs.org/csv/head -n 50/cut 0/delete 1:7/html?url=https://raw.github.com/okfn/datapipes/master/test/data/gla.csv</code></a></p>

<h3 id="before">Before</h3>

<p><a href="http://datapipes.okfnlabs.org/csv/html?url=https://raw.github.com/okfn/datapipes/master/test/data/gla.csv">
<img src="http://farm3.staticflickr.com/2827/9726020844_0301af2ded.jpg" width="500" height="213" alt="Data pipes: GLA data, HTML view" />
</a></p>

<h3 id="after">After</h3>

<p><a href="http://datapipes.okfnlabs.org/csv/head%20-n%2050/cut%200/delete%201:7/html?url=https://raw.github.com/okfn/datapipes/master/test/data/gla.csv">
<img src="http://farm4.staticflickr.com/3728/9726020800_ff01da582e.jpg" width="500" height="177" alt="Data pipes: GLA data, trimmed" />
</a></p>

<h2 id="motivation---data-wrangling-pipes-nodejs-and-the-unix-philosophy">Motivation - Data Wrangling, Pipes, NodeJS and the Unix Philosophy</h2>

<p>When you find data in the wild you usually need to poke around in it and then to some cleaning for it to be usable.</p>

<p>Much of the inspiration for Data Pipes comes from our experience using Unix command lines tools like <code>grep</code>, <code>sed</code>, and <code>head</code> to do this kind of work. These tools a powerful way to operate on <em>streams</em> of text (or more precisely streams of lines of text, since Unix tools process text files line by line). By using streams, they can scale to large files easily (they don’t load the whole file but process it bit by bit) and, more importantly, allow “piping” – that is, direct connection of the output of one command with the input of another.</p>

<p>This already provides quite a powerful way to do data wrangling (see <a href="https://github.com/rgrp/command-line-data-wrangling">here</a> for more). But there are limits: data isn’t always line-oriented, plus command line tools aren’t online, so it’s difficult to share and repeat what you are doing. Inspired by a combination of Unix pipes and the possibilities of <a href="http://nodejs.org/">NodeJS</a>’s great streaming capabilities, we wanted to take the pipes online for data processing – and so Data Pipes was born.</p>

<p>We wanted to use the <a href="http://www.faqs.org/docs/artu/ch01s06.html">Unix philosophy</a> that teaches us to solve problems with cascades of simple, composable operations that manipulate streams, an approach which has proven almost <em>universally</em> effective.</p>

<p>Data Pipes brings the Unix philosophy and the Unix pipes style to online data. Any <a href="http://data.okfn.org/standards/csv">CSV</a> data can be piped through a cascade of transformations to produce a modified dataset, without ever downloading the data and with no need for your own backend. Being online means that the operations are immediately shareable and linkable.</p>

<h2 id="more-examples">More Examples</h2>

<p>Take, for example, this copy of a set of <a href="https://raw.github.com/okfn/datapipes/master/test/data/gla.csv">Greater London Authority financial data</a>. It’s unusable for most purposes, simply because it doesn’t abide by the CSV convention that the first line should contain the headers of the table. The header is preceded by six lines of useless commentary. Another problem is that the first column is totally empty.</p>

<p><img src="http://farm4.staticflickr.com/3824/9726020908_bb2d26b694.jpg" width="500" height="363" alt="Data pipes: Greater London Authority financial data, in the raw" /></p>

<p>First of all, let’s use the Data Pipes <code>html</code> operation to get a nicer-looking view of the table.</p>

<pre><code>GET /csv/html/?url=http://static.london.gov.uk/gla/expenditure/docs/2012-13-P12-250.csv
</code></pre>

<p><img src="http://farm3.staticflickr.com/2827/9726020844_0301af2ded.jpg" width="500" height="213" alt="Data pipes: GLA data, HTML view" /></p>

<p>Now let’s get rid of those first six lines and the empty column. We can do this by chaining together the <code>delete</code> operation and the <code>cut</code> operation:</p>

<pre><code>GET /csv/delete 0:6/cut 0/html/?url=http://static.london.gov.uk/gla/expenditure/docs/2012-13-P12-250.csv
</code></pre>

<p>And just like that, we’ve got a well-formed CSV!</p>

<p><img src="http://farm4.staticflickr.com/3728/9726020800_ff01da582e.jpg" width="500" height="177" alt="Data pipes: GLA data, trimmed" /></p>

<p>But why stop there? Why not take the output of that transformation and, say, search it for the string “LONDON” with the <code>grep</code> transform, then take just the first 20 entries with <code>head</code>?</p>

<pre><code>GET /csv/delete 0:6/cut 0/grep LONDON/head -n 20/html/?url=http://static.london.gov.uk/gla/expenditure/docs/2012-13-P12-250.csv
</code></pre>

<p><img src="http://farm6.staticflickr.com/5505/9726020732_c5ca38c10a.jpg" width="500" height="370" alt="Data pipes: GLA data, final view" /></p>

<p>Awesome!</p>

<h2 id="whats-next">What’s next?</h2>

<p>Data Pipes already supports a useful collection of operations, but it’s still in development, and more are yet to come, including find-and-replace operation <code>sed</code> plus support for <a href="https://github.com/okfn/datapipes/issues/21">arbitrary map and filter functions</a>.</p>

<p>You can see the full list <a href="http://datapipes.okfnlabs.org/">on the Data Pipes site</a>, and you can suggest more transforms to implement by <a href="https://github.com/okfn/datapipes/issues/new">raising an issue</a>.</p>

<p>Data Pipes needs more operations for its toolkit. That means its developers need to know what you do with data – and to think about how it can be broken down in the grand old Unix fashion. To join in, check out <a href="https://github.com/okfn/datapipes">Data Pipes on GitHub</a> and let us know what you think.</p>



