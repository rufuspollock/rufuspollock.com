---
title: >-
  Labs newsletter: 14 November, 2013
slug: labs-newsletter-14-november-2013
date: 2013-11-14T08:00:00
themes: []
tags: []
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1308
---

<p>Labs was bristling with discussion and creation this week, with major improvements to two projects, interesting conversations around a few others, and an awesome new blog post.</p>

<h2 id="data-pipes-lots-of-improvements">Data Pipes: lots of improvements</h2>

<p><a href="http://datapipes.okfnlabs.org/">Data Pipes</a> is a Labs project that provides a web API for a set of simple data-transforming operations that can be chained together in the style of Unix pipes.</p>

<p>This past week, <a href="http://okfnlabs.org/members/andylolz">Andy Lulham</a> has made a <em>huge</em> number of improvements to Data Pipes. Just a few of the new features and fixes:</p>

<ul>
  <li>new operations: <code>strip</code> (removes empty rows), <code>tail</code> (truncate dataset to its last rows)</li>
  <li>new features: a <code>range</code> function and a “complement” switch for <code>cut</code>; options for <code>grep</code></li>
  <li>all operations in pipeline are now trimmed for whitespace</li>
  <li>basic tests have been added</li>
</ul>

<p>Have a look at the <a href="https://github.com/okfn/datapipes/issues?page=1&amp;state=closed">closed issues</a> to see more of what Andy has been up to.</p>

<h2 id="webshot-new-homepage-and-feature">Webshot: new homepage and feature</h2>

<p>Last week we introduced you to <a href="http://webshot.okfnlabs.org/">Webshot</a>, a web API for screenshots of web pages.</p>

<p>Back then, Webshot’s home page was just a screenshot of GitHub. Now Webshot has a <a href="http://webshot.okfnlabs.org/">proper home page</a> with a form interface to the API.</p>

<p>Webshot has also added support for <em>full page</em> screenshots. Now you can capture the whole page rather than just its visible portion.</p>

<h2 id="on-the-blog-natural-language-processing-with-python">On the blog: natural language processing with Python</h2>

<p>Labs member <a href="http://okfnlabs.org/members/tamr/">Tarek Amr</a> has contributed an awesome post on <a href="http://okfnlabs.org/blog/2013/11/11/python-nlp.html">Python natural language processing</a> with the NLTK toolkit to the Labs blog.</p>

<p>“The beauty of NLP,” Tarek says, “is that it enables computers to extract knowledge from unstructured data inside textual documents.” Read his post to learn how to do text normalization, frequency analysis, and text classification with Python.</p>

<h2 id="data-packages-workflow--la-node">Data Packages workflow à la Node</h2>

<p>Wouldn’t it be nice to be able to initialize new <a href="http://data.okfn.org/standards/data-package">Data Packages</a> as easily as you can initialize a Node module with  <code>npm init</code>?</p>

<p><a href="http://www.maxogden.com/">Max Ogden</a> started a <a href="https://github.com/okfn/datapackage.js/issues/3">discussion thread</a> around this enticing idea, eventually leading to <a href="http://okfnlabs.org/members/rgrp">Rufus Pollock</a> booting a new repo for <a href="https://github.com/okfn/dpm">dpm</a>, the Data Package Manager. Check out <a href="https://github.com/okfn/dpm/issues">dpm’s Issues</a> to see what needs to happen next with this project.</p>

<h2 id="nomenklatura-looking-forward">Nomenklatura: looking forward</h2>

<p><a href="http://nomenklatura.okfnlabs.org/">Nomenklatura</a> is a Labs project that does data reconciliation, making it possible “to maintain a canonical list of entities such as persons, companies or event streets and to match messy input, such as their names, against that canonical list”.</p>

<p><a href="http://okfnlabs.org/members/pudo">Friedrich Lindenberg</a> has noted on the Labs mailing list that <a href="http://lists.okfn.org/pipermail/okfn-labs/2013-November/001138.html">Nomenklatura has some serious problems</a>, and he has proposed “a fairly radical re-framing of the service”.</p>

<p>The conversation around what this re-framing should look like is still underway—check out <a href="http://lists.okfn.org/pipermail/okfn-labs/2013-November/001138.html">the discussion thread</a> and jump in with your ideas.</p>

<h2 id="data-issues-following-issues">Data Issues: following issues</h2>

<p>Last week, the idea of <a href="http://okfnlabs.org/blog/2013/11/06/tracking-data-issues.html">Data Issues</a> was floated: using GitHub Issues to track problems with public datasets. The idea has generated a few comments, and we’d love to hear more.</p>

<p>Discussion on the Labs list highlighted another benefit of using GitHub. <a href="https://github.com/aliounedia">Alioune Dia</a> suggested that Data Issues should let users register to be notified when a particular issue is fixed. But <a href="http://feedmechocolate.com/">Chris Mear</a> pointed out that GitHub already makes this possible: “Any GitHub user can ‘follow’ a specific issue by using the notification button at the bottom of the issue page.”</p>

<h2 id="get-involved">Get involved</h2>

<p>Anyone can join the Labs community and get involved! Read more about how you can <a href="http://okfnlabs.org/join/">join the community</a> and participate by coding, wrangling data, or doing outreach and engagement. Also check out the <a href="http://okfnlabs.org/ideas/">Ideas Page</a> to see what’s cooking in the Labs.</p>



