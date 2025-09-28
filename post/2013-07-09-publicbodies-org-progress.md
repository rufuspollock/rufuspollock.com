---
title: >-
  PublicBodies.org progress
slug: publicbodies-org-progress
date: 2013-07-09T07:00:00
themes: []
tags: []
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1312
---

<p>There have been many new developments with <a href="http://publicbodies.org/">PublicBodies.org</a>, the Labs project which aims to provide “a URL for every part of government”, since <a href="http://okfnlabs.org/blog/2013/05/01/publicbodies.org-an-update.html">the last update</a> on the Labs blog.</p>

<p>The news includes: a new and improved backend; a push for integration with <a href="http://nomenklatura.okfnlabs.org/">Nomenklatura</a>; discussion of a revamp of the PublicBodies schema; lots of new data waiting to be integrated; and a new idea for how PublicBodies might be useful.</p>

<h2 id="publicbodies-now-much-shinier">PublicBodies: now much shinier</h2>

<p>Thanks to the hard work of Labs member <a href="http://okfnlabs.org/members/wombleton/">Rowan Crawford</a>, PublicBodies is now a proper webapp. It’s now a <a href="https://github.com/okfn/publicbodies">Node.js app</a> running on <a href="https://www.heroku.com/">Heroku</a>, and its interface is much nicer than before. Let’s all give Rowan a hand!</p>

<p>Development of the PublicBodies website is ongoing. The next task for improving the site will be <a href="https://github.com/okfn/publicbodies/issues/3">adding search</a>.</p>

<h2 id="nomenklatura-integration">Nomenklatura integration</h2>

<p>Entity reconciliation is crucial for a service like PublicBodies. Luckily, the Labs has another project that simplifies reconciliation, namely <a href="http://nomenklatura.okfnlabs.org/">Nomenklatura</a>. The obvious step is to start pushing PublicBodies data to Nomenklatura and pulling it when it gets updated. This idea is discussed more fully in <a href="https://github.com/okfn/publicbodies/issues/2">an issue</a>.</p>

<p>Contributor <a href="https://github.com/davidread">David Read</a> has got the ball rolling with Nomenklatura integration by pushing <a href="http://nomenklatura.okfnlabs.org/uk-public-bodies">UK public bodies data</a>. This is a great start – but we want to automate this and start automatically pushing CSVs across to Nomenklatura. Volunteers to build this functionality, please step up!</p>

<h2 id="popolo-schema-integration">Popolo schema integration</h2>

<p><a href="http://popoloproject.com/">Popolo</a> is a project with a goal very relevant to PublicBodies: the creation of “international open government data specifications relating to the legislative branch of government”. These include a data specification for <a href="http://popoloproject.com/specs/organization.html">organizations</a>.</p>

<p>We’re considering reworking the PublicBodies schema to follow the Popolo organization spec. The changes would be nontrivial but wouldn’t involve any massive reorganization of the data. Please help us think this through by joining in the discussion <a href="https://github.com/okfn/publicbodies/issues/29">in the issues</a>.</p>

<h2 id="lots-of-new-data">Lots of new data</h2>

<p>Once the matter of revamping the schema is resolved, we can start integrating the heaps of new data which has been contributed. The new data includes public bodies from the US, Germany, China, Quebec, Italy, and Slovenia. You can see it all <a href="https://github.com/okfn/publicbodies/issues?direction=desc&amp;labels=Data&amp;page=1&amp;sort=updated&amp;state=open">here</a>. Thanks to the contributors who have brought this data together.</p>

<p>The sooner we come to a decision about the Popolo schema, the sooner we can start incorporating all of this new material – so please let us know what you think!</p>

<h2 id="discussion-organization-identifiers">Discussion: organization identifiers</h2>

<p>Contributor <a href="https://github.com/markbrough">Mark Brough</a> has come up with an interesting idea for how PublicBodies might be useful: it could be used to generate organisation identifiers usable in situations calling for unique identifiers, such as IATI data publication. As Mark observes, public organizations often lack these identifiers, which makes publishing data a struggle.</p>

<p>Read the details of Mark’s proposal <a href="https://github.com/okfn/publicbodies/issues/41">in the issues</a>, and let him know what you think.</p>



