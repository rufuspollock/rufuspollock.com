---
title: >-
  Recline JS - Componentization and a Smaller Core
slug: recline-js-componentization-and-a-smaller-core
date: 2013-02-26T08:00:00
themes: []
tags: [u'Tech']
projects: [u'Open Knowledge']
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1247
---

<p>Over time <a href="http://okfnlabs.org/recline/">Recline JS</a> has grown. In particular, since the first <a href="http://blog.okfn.org/2012/07/05/announcing-recline-js-a-javascript-library-for-building-data-applications-in-the-browser/">public
announce of Recline</a> last summer we’ve had several people producing
new backends and views (e.g.  <a href="https://github.com/okfn/recline/wiki/Extensions">backends for Couch, a view for d3, a map view
based on Ordnance Survey’s tiles etc etc</a>).</p>

<p>As <a href="http://lists.okfn.org/pipermail/okfn-labs/2013-February/000638.html">I wrote to the labs list recently</a>, continually adding these to
core Recline runs the risk of bloat. Instead, we think it’s better to keep the
core lean and move more of these “extensions” out of core with a clear listing
and curation process - the design of Recline means that <a href="http://okfnlabs.org/recline/docs/backends.html">new backends</a> and
<a href="http://okfnlabs.org/recline/docs/views.html">views</a> can extend the core easily and without any complex dependencies.</p>

<p>This approach is useful in other ways. For example, Recline backends are
designed to support standalone use as well as use with Recline core (they have
no dependency on <em>any</em> other part of Recline - <em>including core</em>) but this is
not very obvious as it stands (where the backend is bundled with Recline). To
take a concrete example, the Google Docs backend is a useful wrapper for the
Google Spreadsheets API in its own right. While this is already true, when this
code is in the main Recline repository it isn’t very obvious but having the
repo split out with its own README would make this much clearer.</p>

<h2 id="so-the-plan-is-">So the plan is …</h2>

<ul>
  <li>Announce this approach of a leaner core and more “Extensions”
    <ul>
      <li>Link to the specifications for <a href="http://okfnlabs.org/recline/docs/backends.html">Backends</a> and <a href="http://okfnlabs.org/recline/docs/views.html">Views</a></li>
      <li>Create an official <a href="https://github.com/okfn/recline/wiki/Extensions">Recline Extensions page</a></li>
    </ul>
  </li>
  <li>Identify first items to split out from core - see <a href="https://github.com/okfn/recline/issues/314">this issue</a></li>
  <li>Identify what components <em>should</em> remain in core? (I’m thinking Dataset +
Memory DataStore plus one Grid, Graph and Map)</li>
</ul>

<p>So far I’ve already started the process of factoring out some backends (and
soon views) into standalone repos, e.g. here’s GDocs:</p>

<p><a href="https://github.com/okfn/recline.backend.gdocs">https://github.com/okfn/recline.backend.gdocs</a></p>

<p>Any thoughts very welcome and if you already have Recline extensions lurking in
your repos please add them to the <a href="https://github.com/okfn/recline/wiki/Extensions">wiki page</a></p>



