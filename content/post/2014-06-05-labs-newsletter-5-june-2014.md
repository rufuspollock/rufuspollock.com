---
title: >-
  Labs newsletter: 5 June, 2014
slug: labs-newsletter-5-june-2014
date: 2014-06-05T00:00:00
themes: []
tags: []
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1350
---

<p>Welcome back to the OKFN Labs! Members of the Labs have been building tools, visualizations, and even new data protocols—as well as setting up conferences and events. Read on to learn more.</p>

<p>If you’d like to suggest a piece of news for next month’s newsletter, leave a comment on its <a href="https://github.com/okfn/okfn.github.com/issues/215">GitHub issue</a>.</p>

<h2 id="commasearch">commasearch</h2>

<p><a href="http://okfnlabs.org/members/tlevine/">Thomas Levine</a> has been working on an innovative new approach to searching tabular data, <a href="https://github.com/tlevine/commasearch">commasearch</a>.</p>

<p>Unlike a normal search engine, where you submit words and get pages of words back, with commasearch, you submit spreadsheets and get spreadsheets in return.</p>

<p>What does that mean, and how does it work? Check out Thomas’s excellent blog post “<a href="http://dada.pink/dada/pagerank-for-spreadsheets/">Pagerank for Spreadsheets</a>” to learn more.</p>

<h2 id="github-diffs-for-csv-files">GitHub diffs for CSV files</h2>

<p><em>Submitted by <a href="http://okfnlabs.org/members/paulfitz/">Paul Fitzpatrick</a>.</em></p>

<p>GitHub has added CSV viewing support in their web interface, which is fantastic, but it still doesn’t handle changes well. If you use Chrome, and want lovely diffs, check out James Smith’s <a href="https://github.com/theodi/csvhub">CSVHub</a> extension (<a href="http://theodi.org/blog/csvhub-github-diffs-for-csv-files">blogpost and screenshot</a>). The diffs are produced using the <a href="http://paulfitz.github.io/daff/">daff</a> library, available in javascript, ruby, php, and python3.</p>

<h2 id="textus-wordpress-plugin">Textus Wordpress plugin</h2>

<p><em>Update from Iain Emsley.</em></p>

<p>The Open Literature project to provide a <a href="https://github.com/okfn/textus-wordpress">Wordpress plugin back-end for the Textus viewer</a> has made new progress.</p>

<p>This project’s goal was to keep the existing Textus frontend—which has been <a href="https://github.com/okfn/textus-viewer">split off as its own project</a> by Rufus Pollock—and replace the backend with a Wordpress plugin, to make it easier to deploy. A version of this plugin backend is now available.</p>

<p>The new plugin acts as a stand-alone module that can be enabled and disabled as required by the administrative user. It creates a new Wordpress post type called “Textus” which is available as part of the menu, giving the user a place to upload text and annotation files using the Media uploader.</p>

<p>If you are interested in the project, check out its <a href="https://github.com/okfn/textus-wordpress/issues">issues</a> and discussion on the <a href="https://lists.okfn.org/mailman/listinfo/open-humanities">Open Humanities list</a>.</p>

<h2 id="data-protocols-updates">Data protocols: updates</h2>

<p><a href="http://dataprotocols.org/">Data Protocols</a>, the Labs’s set of lightweight standards and patterns for open data, has had a couple of interesting developments.</p>

<p>The <a href="http://dataprotocols.org/json-table-schema/">JSON Table Schema</a> protocol has just added support for constraints (i.e. validation), thanks to <a href="http://www.ldodds.com/">Leigh Dodds</a>. This adds a <code>constraints</code> attribute containing requirements on the content of fields. See the full <a href="http://dataprotocols.org/json-table-schema/#field-constraints">list of valid constraints</a> on the JSON Table Schema site.</p>

<p>The <a href="https://github.com/okfn/dpm/">Data Package Manager</a> tool for Data Packages is shaping up nicely: the <code>install</code> and <code>init</code> commands have now been implemented. You can see an <a href="https://github.com/okfn/dpm/issues/3#issuecomment-43440812">animated GIF</a> of the former in the issue thread.</p>

<h2 id="annotatorjs-new-home">AnnotatorJS: new home</h2>

<p>Annotator is “an open-source JavaScript library to easily add annotation functionality to any webpage”.</p>

<p>The project now lives on its own domain at <a href="http://annotatorjs.org/">annotatorjs.org</a>. Check it out and see how easy it is to add comments and notes to your pages!</p>

<h2 id="csvconf">csv,conf</h2>

<p>Data makers everywhere will want to check out <a href="http://csvconf.com/">csv,conf</a>, a fringe event of <a href="http://2014.okfestival.org/">Open Knowledge Festival 2014</a> taking place in Berlin on 15 July.</p>

<p>csv,conf is a non-profit community conference that will “bring together data makers/doers/hackers from backgrounds like science, journalism, open government and the wider software industry to share tools and stories”.</p>

<p><a href="http://register.csvconf.com/">Tickets are $75, $50 with an OKFest ticket</a>. If you can make it to Berlin in July and you’re into “advancing the art of data collaboration”, come join in!</p>


