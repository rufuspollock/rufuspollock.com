---
title: >-
  Javascript Timeline Libaries - A Review
slug: javascript-timeline-libaries-a-review
date: 2012-12-04T08:00:00
themes: []
tags: []
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1250
---

<p>This post is a rough and ready overview of various javascript timeline libraries that arose from research in creating a timeline view for <a href="http://reclinejs.com/">Recline JS</a>. Note this material hung around on my hard disk for a few months so some of it may already be a little bit out of date!</p>

<div class="alert alert-info">
<strong>October 2013</strong>: We have released <strong><a href="http://timemapper.okfnlabs.org/">TimeMapper</a></strong> a new online app for creating <strong>Timelines and TimeMaps</strong> quickly and easily. Check it out at <strong><a href="http://timemapper.okfnlabs.org/">http://timemapper.okfnlabs.org/</a></strong>
</div>

<p>I want to start with a general comment. Timeline libraries consist of various components:</p>

<ul>
  <li>Data loading
    <ul>
      <li>Date parsing</li>
    </ul>
  </li>
  <li>Band (timeline) rendering</li>
  <li>Showing render info on individual items</li>
</ul>

<p>For me a timeline visualization library need only be the second of these but most that I’ve come across do more.</p>

<p>In fact a major issue in my opinion with most libraries is that they are <em>under-componentized</em> - they don’t separate cleanly into these different components and end up doing everything.</p>

<p>To take one example, the Verite timeline (in my view is one of the best libraries out there) has a whole bunch of its own custom date parsing built in inside an internal utility library which are hard to override or replace and also has a large chunk of code just for loading from google docs and other data sources. (You can of course somewhat solve this somewhat – as I do in Recline by parsing the dates directly  and then submitting in a standardized form).</p>

<p>In my view, even if library authors do want to include these sorts of things, it would be good to do it in a way that allowed for a clean separation so that you could just use the parts you wanted (and/or over-ride parts more cleanly).</p>

<h2 id="propublica-timeline-setter">Propublica Timeline Setter</h2>

<ul>
  <li><a href="http://propublica.github.com/timeline-setter/">http://propublica.github.com/timeline-setter/</a></li>
  <li>HTML + JS
    <ul>
      <li>But Requires a build step (using ruby)</li>
    </ul>
  </li>
  <li>Very simple and compact design (nice!)</li>
</ul>

<h2 id="verite-timeline">Verite Timeline</h2>

<ul>
  <li><a href="http://timeline.verite.co/">http://timeline.verite.co/</a></li>
  <li>Very elegant frontend design</li>
  <li>2 bands in timeline segment and tight integration of item display </li>
  <li>Includes much more than Timeline (e.g. sourcing data from google docs etc)</li>
  <li>Mozilla Public License (was GPL)</li>
</ul>

<h2 id="simile-timeline">Simile Timeline</h2>

<ul>
  <li>http://www.simile-widgets.org/timeline/</li>
  <li>The original open-source JS timeline but less regularly update and maintained today: “As of Spring 2012, Exhibit is the only Simile widget seeing active development.” and the timeline control has not been updated since 2009 (see this <a href="http://stackoverflow.com/questions/4700419/alternative-to-simile-timeline-for-timeline-visualization">stackoverflow question for more</a></li>
</ul>

<h2 id="chronoline">Chronoline</h2>

<ul>
  <li><a href="http://stoicloofah.github.com/chronoline.js/">http://stoicloofah.github.com/chronoline.js/</a></li>
  <li>Recently developed and updated</li>
  <li>MIT licensed</li>
</ul>

<h2 id="timeglider">Timeglider</h2>

<ul>
  <li><a href="https://github.com/timeglider/jquery_widget">https://github.com/timeglider/jquery_widget</a></li>
  <li>Non-open license (but was MIT licensed <a href="https://github.com/timeglider/jquery_widget/tree/345442fa3dc7c66b23c36031a6569693ecf309bd">earlier on</a></li>
</ul>

<h2 id="chaps-timeline">CHAPS Timeline</h2>

<ul>
  <li><a href="http://almende.github.com/chap-links-library/timeline.html">http://almende.github.com/chap-links-library/timeline.html</a></li>
  <li>Looks pretty nice though CSS is not quite as elegant (probably fixable!)</li>
  <li>Not clear whether it supports multiple bands</li>
</ul>



