---
title: >-
  Labs newsletter: 30 January, 2014
slug: labs-newsletter-30-january-2014
date: 2014-01-30T00:00:00
themes: []
tags: []
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1301
---

<p>From now on, the Labs newsletter will arrive through a special announce-only mailing list, <em>newsletter@okfnlabs.org</em>, more details on which can be found below.</p>

<p>Keep reading for other new developments including the fifth Labs Hangout, the launch of SayIt, and new developments in the vision of “Frictionless Data”.</p>

<h2 id="new-newsletter-format">New newsletter format</h2>

<p>Not everyone who wants to know about Labs activities wants or needs to observe those activities unfolding on the main Labs list. For friends of Labs who just want occasional updates, we’ve created a new, <a href="http://sendy.co/">Sendy</a>-based announce-only list that will bring you a Labs newsletter every two weeks.</p>

<p>Everyone currently subscribed to <em>okfn-labs@lists.okfn.org</em> has been added to the new list. To join the new announce list, see the <a href="http://okfnlabs.org/contact/">Labs Contact page</a>, where there’s a form.</p>

<h2 id="labs-hangout-no-5">Labs Hangout no. 5</h2>

<p>Last Thursday, <a href="http://okfnlabs.org/members/andylolz">Andy Lulham</a> hosted the fifth OKFN Labs Hangout. The Labs Hangouts are a way for people curious about Labs projects to informally get together, share their work, and talk about the future of Labs.</p>

<p>For full details, check out the <a href="http://pad.okfn.org/p/labs-hangouts">minutes from the hangout</a>. Highlights included:</p>

<ul>
  <li>SayIt, a new publication platform for speeches &amp; transcripts, introduced by <a href="http://twitter.com/steiny">Tom Steinberg</a> of <a href="http://t.co/KKNpVhbitu">mySociety</a> (see below for more!)</li>
  <li>announcement of an <a href="http://humanities.okfn.org/open-literature-sprint-jan-2014/">Open Literature Sprint</a> this past Saturday</li>
  <li>full coverage of PyBossa source code with <a href="https://coveralls.io/r/PyBossa/pybossa">unit tests</a></li>
  <li><a href="http://twitter.com/tfmorris">Tom Morris</a>’s work parsing and importing e-publications from <a href="http://openlibrary.org/">Open Library</a></li>
  <li>updates to <a href="http://data.okfn.org/vision">Frictionless Data</a> (see below)</li>
</ul>

<h2 id="sayit">SayIt</h2>

<p><a href="http://sayit.mysociety.org/">SayIt</a>, an open-source tool for publishing and sharing transcripts, has just been launched by <a href="http://poplus.org/">Poplus</a>. At last week’s Labs Hangout, <a href="http://twitter.com/steiny">Tom Steinberg</a> of <a href="http://t.co/KKNpVhbitu">mySociety</a> (one half of Poplus, alongside <a href="http://www.ciudadanointeligente.org/?lang=en">Ciudadano Inteligente</a>) shared some of the motivations behind the creation of the tool, which was also discussed <a href="https://lists.okfn.org/pipermail/okfn-discuss/2014-January/010083.html">on the okfn-discuss mailing list</a>.</p>

<p>As Tom explained, mySociety’s <a href="http://www.theyworkforyou.com/">They Work For You</a> has proven the popularity of transcript data. But making the transcripts available in a nice way (e.g. with a decent API) has so far called for bespoke software development. SayIt is designed to encourage “nice” publication as the starting-point—and to serve as a pedagogical example of what a good data publication tool looks like.</p>

<h2 id="frictionless-data-vision-roadmap-composability">Frictionless data: vision, roadmap, composability</h2>

<p>We’ve heard about <a href="http://okfnlabs.org/members/rgrp">Rufus</a>’s vision for an ecosystem of “frictionless data” in the past. Now the discussion is starting to get serious. <a href="http://data.okfn.org/">data.okfn.org</a> now hosts two key documents generated through the conversation:</p>

<ul>
  <li><a href="http://data.okfn.org/vision">the vision</a>: what will create a dynamic, productive, and attractive open data ecosystem?</li>
  <li><a href="http://data.okfn.org/roadmap">the roadmap</a>: what has to happen to bring this vision to life?</li>
</ul>

<p>The new roadmap is a particularly lucid overview of how the frictionless data vision connects with concrete actions. Would-be creators of this new ecosystem should consult the roadmap to see where to join in.</p>

<p><a href="https://lists.okfn.org/pipermail/okfn-labs/2014-January/001260.html">Discussion on the Labs list</a> has also generated some interesting insights. <a href="http://t.co/pL0Yy7uNuf">Data Unity</a>’s Kev Kirkland discussed his work with Semantic Web formalization of composable data manipulation processes, and <a href="http://okfnlabs.org/members/Stiivi/">S?tefan Urbánek</a> made a connection with his work on “abstracting datasets and operations” in the ETL framework <a href="https://github.com/Stiivi/bubbles">Bubbles</a>.</p>

<h2 id="on-the-blog-olap-part-two">On the blog: OLAP part two</h2>

<p>Last week, <a href="http://okfnlabs.org/members/Stiivi/">S?tefan Urbánek</a> wrote us an <a href="http://okfnlabs.org/blog/2014/01/10/olap-introduction.html">introduction to Online Analytical Processing</a>. Shortly afterwards, he followed up with a second post taking a closer look at <a href="http://okfnlabs.org/blog/2014/01/20/olap-cubes-and-logical-model.html">how OLAP data is structured and why</a>.</p>

<p>Check out S?tefan’s post to learn about how OLAP represents data as multidimensional “cubes” that users can slice and dice to explore the data along its many dimensions.</p>

<h2 id="timemapper-improvements">TimeMapper improvements</h2>

<p><a href="http://okfnlabs.org/members/andylolz">Andy Lulham</a> has started working on <a href="http://timemapper.okfnlabs.org/">TimeMapper</a>, Labs’s easy-to-use tool for the creation of interactive timelines linked to geomaps.</p>

<p>Some of the improvements he has made so far have been bugfixes (e.g. <a href="https://github.com/okfn/timemapper/pull/119">preventing overflowing form controls</a>, <a href="https://github.com/okfn/timemapper/pull/118">fixing the template settings file</a>), but one of them is a new user feature: adding a way to <a href="http://timemapper.okfnlabs.org/">change the starting event</a> on a timeline so that they don’t always have to start at the beginning.</p>

<h2 id="get-involved">Get involved</h2>

<p>Want to get involved with Labs’s projects? Now is a great time to join in! Check out the <a href="http://okfnlabs.org/ideas/">Ideas Page</a> to see some of the many things you can do once you <a href="http://okfnlabs.org/join/">join Labs</a>, or just jump on the <a href="http://lists.okfn.org/mailman/listinfo/okfn-labs">Labs mailing list</a> and take part in a conversation.</p>



