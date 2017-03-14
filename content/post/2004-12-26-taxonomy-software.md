---
title: >-
  Taxonomy Software
slug: taxonomy-software
date: 2004-12-26T13:37:59
themes: []
tags: [u'Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 2
---

<p>
	Is there a standard data format for taxonomies/classification systems. Should include a specification of text encoding (like LDIF but for taxonomies). If there is I would guess there will be open source implementations (and if not won't be that hard to write one's own).</p>

<h2>
	Requirements:
</h2>
<ol>
	<li>
		Type of taxonmy:
		<ol>
			<li>Enumerations (flat)</li>
			<li>Tree (single parent)</li>
			<li>Lattice (multiple parent)</li>
		</ol>
	</li>
	<li>
		Identifiers. Support for at least 10 million possible elements in taxonomy. Optional: Identifiers should be portable across systems (i.e. you can plug different taxonomies together without recoding identifiers). This means probably want a GUID based id system). Required: basic int32 or int64 based identifiers. 
	</li>
</ol>

<h2>
	Found So Far
</h2>
<ol>
	<li>
		DELTA <a href="http://biodiversity.uno.edu/delta/">http://biodiversity.uno.edu/delta/</a>. Seem to be primarily for standard tree taxonomies for animals and plants.
	</li>
</ol>

<h3>
	Written Myself
</h3>
<p>
	Two taxonomy systems with gui editors and serialization to xml. One in C# and the other in java. Major issue is non-stdness.</p>

<h2>
	Wild Ideas
</h2>
<ol>
	<li>
		Drupal has a pretty nice web-based gui for creating (and using) taxonomies. Could use that as a front end and then serialize to std text format from the drupal backend db
	</li>
</ol>





