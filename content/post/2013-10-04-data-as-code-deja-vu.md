---
title: >-
  Data as Code Deja-Vu
slug: data-as-code-deja-vu
date: 2013-10-04T07:00:00
themes: []
tags: []
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1275
---

<p>Someone just pointed me at <a href="http://ben.balter.com/2013/09/16/treat-data-as-code/">this post from Ben Balter about Data as Code</a> in which he emphasizes the analogies between data and code (and especially open data and open-source – e.g. “data is where code was 2 decades ago” …).</p>

<p>I was delighted to see this post as it makes many points I deeply agree with - and have for some time. In fact, reading it gave me something a sense of (very positive) deja-vu since it made similar points to several posts I and others had written several years ago - suggesting that perhaps we’re now getting close to the critical mass we need to create a real distributed and collaborative <a href="http://blog.okfn.org/2011/03/31/building-the-open-data-ecosystem/">open data ecosystem</a>!</p>

<p>It also suggested it was worth dusting off and recapping some of this earlier material as much of it was written more than 6 years ago, a period which, in tech terms, can seem like the stone age.</p>

<h2 id="previous-thinking">Previous Thinking</h2>

<p>For example, there is this essay from 2007 on <a href="http://blog.okfn.org/writings/componentization/">Componentization and Open Data</a> that Jo Walsh and I wrote for our XTech talk that year on CKAN. It emphasized analogies with code and the importance of componentization and packaging.</p>

<p>This, in turn, was based on <a href="http://blog.okfn.org/2006/05/09/the-four-principles-of-open-knowledge-development/">Four principles for Open Knowledge Development</a> and <a href="http://blog.okfn.org/2007/04/30/what-do-we-mean-by-componentization-for-knowledge/">What do we mean by componentization for knowledge</a>. We also emphasized the importance of “version control” in facilitating distributed collaboration, for example in <a href="http://blog.okfn.org/2007/02/20/collaborative-development-of-data/">Collaborative Development of Data (2006/2007)</a> and, more recently, in <a href="http://blog.okfn.org/2010/07/12/we-need-distributed-revisionversion-control-for-data/">Distributed Revision Control for Data (2010)</a> and this year in <a href="http://blog.okfn.org/2013/07/02/git-and-github-for-data/">Git (and GitHub) for Data</a>.</p>

<h2 id="package-managers-and-ckan">Package Managers and CKAN</h2>

<p>This also brings me to a point relevant both to Ben’s post and Michal’s comment: the original purpose (and design) of CKAN was <em>precisely</em> to be a package manager a la rubygems, pypi, debian etc. It has evolved a lot from that into more of a “wordpress for data” - i.e. a platform for publishing, managing (and storing) data because of user demand. (Note that in early CKAN “datasets” were called packages in both the interface and code - a poor UX decision ;-) that illustrated we were definitely ahead of our time - or just wrong!)</p>

<p>Some sense of what was intended is evidenced by the fact that in 2007 we were writing a command line tool called datapkg (since changed to dpm for data package manager) to act at the command equivalent of gem / pip / apt-get - see <a href="http://blog.okfn.org/2010/02/23/introducing-datapkg/">this Introducting DataPkg post</a> which included this diagram illustrating how things were supposed to work.</p>

<p><img src="http://m.okfn.org/files/talks/media/debian_of_data.png" alt="" /></p>

<h2 id="recent-developments">Recent Developments</h2>

<p>As CKAN has evolved into a more general-purpose tool – with less of a focus on just being a registry supported automated access – we’ve continued to develop those ideas. For example:</p>

<ul>
  <li>The basic “package” idea from CKAN has evolved into the <a href="http://data.okfn.org/standards/data-package">Data Package spec</a> - and <a href="http://data.okfn.org/standards/simple-data-format">Simple Data Format</a></li>
  <li>We’ve <a href="http://blog.okfn.org/2013/07/02/git-and-github-for-data/">explored storing data using code tools like git</a> - with a dedicated <a href="http://github.com/datasets">datasets organization on Github</a></li>
  <li>We’ve re-booted the idea of a simple registry and storage mechanism in the form of <a href="http://data.okfn.org/">http://data.okfn.org/</a> - with data stored in simple data format in git repos on github, displayed in a very simple registry with good tool integration, and curated by a dedicated group of maintainers</li>
  <li>We’ve booted the <a href="http://blog.okfn.org/2013/04/24/frictionless-data-making-it-radically-easier-to-get-stuff-done-with-data/">“Frictionless Data” initiative</a> as a way to bring together these different activities in one coherent vision of how we can do something simple to make progress</li>
</ul>

<p><a href="http://data.okfn.org/standards"><img src="http://assets.okfn.org/p/data.okfn.org/img/the-idea.png" alt="" /></a></p>

<p class="caption">Data Packages and Frictionless Data - from <a href="http://data.okfn.org/about">data.okfn.org</a></p>



