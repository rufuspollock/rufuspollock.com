---
title: >-
  Contact Management Software
slug: contact-management-software
date: 2005-04-12T12:53:38
themes: [u'Notebook']
tags: [u'Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 81
---

<table style="text-align: center;" border="1">
	<thead>
		<tr>
			<td>Feature</td>
			<td>Importance</td>
			<td>Comments</td>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Centralized remote repository</td>
			<td>3</td>
			<td></td>
		</tr>
		<tr>
			<td>Can work offline (with syncing when back online)</td>
			<td>3</td>
			<td></td>
		</tr>
		<tr>
			<td>xml (rdf?) storage format</td>
			<td>3</td>
			<td>make our own (can't use vcal/ical unfortunately)</td>
		</tr>
		<tr>
			<td>export to html and ....</td>
			<td>2</td>
			<td>trivial (use some xsl)</td>
		</tr>
		<tr>
			<td>integration with a calendar app ...</td>
			<td>1</td>
			<td>difficult and in that case we might as well try building on sunbird</td>
		</tr>
		<tr>
			<td>min info to store</td>
			<td>3</td>
			<td>
				date entered, date due (if any), subject, details (allow html etc - specify markup type? different types (configurable of todo item): day schedule, todo, goals (long, short, medium). support for closure info (make this a separate item)
			</td>
		</tr>
		<tr>
			<td>other possible info to store</td>
			<td>2</td>
			<td>
				classification of entries (taxonomy) and allow for multiple classification. support linking between items
			</td>
		</tr>
	</tbody>
</table>

<h2>
	Architecture
</h2>
Functionally can split into layers:
<ol>
	<li>
		Remote repository communication
	</li>
	<li>
		Read/write export data format
	</li>
	<li>
		GUI
	</li>
</ol>

<h2>
	Data Design and XML/RDF Format
</h2>
<h3>
	Remarks
</h3>
<ol>
	<li>
		Can make day schedule as compositions of todo items ??? (thing is they are kind of trivial .....). NO this	is the way to do it. What to provide interface when it is like that .....?
	</li>
	<li>
		This is getting TOO complicated .....
	</li>
</ol>

<h3>
	Fields/Values
</h3>
<table style="text-align: center;" border="1">
	<thead>
		<tr>
			<td>Feature</td>
			<td>Importance</td>
			<td>Comments</td>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>standard attributes of dc: title, data created, date last modified, author (creator)</td>
			<td>3</td>
			<td></td>
		</tr>
		<tr>
			<td>details/fulltext</td>
			<td>3</td>
			<td></td>
		</tr>
		<tr>
			<td>classification with vocabularies</td>
			<td>2</td>
			<td>this should be the main site of extensibility</td>
		</tr>
		<tr>
			<td>status (closed, open, urgent ....?)</td>
			<td>3</td>
			<td>trivial (use some xsl)</td>
		</tr>
		<tr>
			<td>assigned</td>
			<td>1</td>
			<td></td>
		</tr>
	</tbody>
</table>

