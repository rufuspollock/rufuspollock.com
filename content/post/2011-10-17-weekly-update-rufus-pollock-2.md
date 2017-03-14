---
title: >-
  Weekly Update: Rufus Pollock
slug: weekly-update-rufus-pollock-2
date: 2011-10-17T12:34:30
themes: []
tags: []
projects: [u'Open Knowledge', u'Shuttleworth Fellowship']
posttypes: [u'Updates']
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1016
---

### Availability

* Very limited due to [Open Government Data Camp][ogdcamp]

### Activity

 * In San Francisco last week Tuesday - Saturday. Attended Code for America Summit and had a variety of useful meetings including with Wikimedia Foundation folks including Erik MÃ¶ller and [Dario Taraborelli][dario], Dan Whaley of [Hypothes.is][hypothesis] and [Max Ogden][maxogden].
  * Below are some written up notes from excellent chat with Max

### This Week

* [Open Government Data Camp][ogdcamp] - come join us in Warsaw for the world's biggest open government data event!

### Max Ogden Chat

#### 1. Changes protocol

Want a general changes protocol for data (can we generalize CouchDB's _changes to lots of other stuff including the [Webstore][])

  * A changes protocol => syncing between DBs => support for updates and distributed systems

#### 2. Diffing and merging
  * We lack a diff (patch) format and a merge protocol (see previous posts [We Need Distributed Revision Control for Data][distributed] and (older) [Collaborative Development of Data][collaborative])
  * Note these issues are related but not identical -- full-on merging, as in e.g. git or mercurial is about more than simple patch application.
  * Diff format options (are there more?)
    1. Brute force: e.g. serialize to text and use git 
    2. Identify atomic structure (e.g. document) and apply diff at that level (think CouchDB or standard copy-on-write for RDBMS at row level)
    3. Recording transforms (e.g. Refine)
  * Capturing diffs at document level in a given system e.g. CouchDB (trivial as can just provide new and old document) or an SQL database (approx = Write-Ahead Log) isn't that hard though often not immediately exposed (as with SQL) and, more importantly, *specific to the data store and, often, type of data*
  * Aside: if using something like CouchDB how would we capture edits when editing 'offline' e.g. on CSV version locally

#### 3. Micro Schemas

Micro-schemas = just enough of standardized schema to apps and tools together with data in a minimal way

 * Micro-schemas = small schemas ("conventions") for data that would support interoperability and allow for generic tools and apps.
 * Simple example: one would have a geodata micro-schema for tabular data that required every dataset with a long / lat for points to have a field named geometry containing geojson representing that point. That way one could build a data browser to present any such dataset.
 * Not only should these schemas be very simple, they would be combinable so a given dataset could support many of these.
 * Aside: I'd sort of prefer the term knowledge or information API here as it would suggest all the nice analogies with code: schemas are just liked APIs but for information: they provide a standard way for other systems to interact with that material. Plus, things like the combinability I just referred to in the previous point, have a nice analogy with MixIns or Abstract interfaces in code where a given Class can implement many MixIns or Abstract interfaces. However, I fear the term API may just be too technical and "geeky".

[ogdcamp]: http://ogdcamp.org/
[dario]: http://nitens.org/taraborelli/home
[maxogden]: http://maxogden.com/
[Webstore]: https://github.com/okfn/webstore
[distributed]: http://blog.okfn.org/2007/02/20/collaborative-development-of-data/
[collaborative]: http://blog.okfn.org/2007/02/20/collaborative-development-of-data/
[hypothesis]: http://hypothes.is/

