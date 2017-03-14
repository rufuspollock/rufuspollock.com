---
title: >-
  Labs newsletter: 21 November, 2013
slug: labs-newsletter-21-november-2013
date: 2013-11-21T00:00:00
themes: []
tags: []
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1307
---

<p>This week, Labs members gathered in an online hangout to discuss what they’ve been up to and what’s next for Labs. This special edition of the newsletter recaps that hangout for those who weren’t there (or who want a reminder).</p>

<h2 id="data-pipes-update">Data Pipes update</h2>

<p>Last week you heard about <a href="http://okfnlabs.org/members/andylolz">Andy Lulham</a>’s improvements to <a href="http://datapipes.okfnlabs.org/">Data Pipes</a>, the online streaming data transformations service. He didn’t stop there, and in this week’s hangout, Andy described some of the new features he has been adding:</p>

<ul>
  <li>parse and render are now <em>streaming</em> operations</li>
  <li>option parsing now uses <a href="https://github.com/substack/node-optimist">optimist</a></li>
  <li>a basic command-line interface</li>
  <li>… and much, much more</li>
</ul>

<p>Coming up next: <a href="https://github.com/okfn/datapipes/issues/21">map &amp; filter with arbitrary functions</a>!</p>

<h2 id="crowdcrafting-progress-and-projects">Crowdcrafting: progress and projects</h2>

<p>New <a href="http://www.shuttleworthfoundation.org/fellows/daniel-lombrana/">Shuttleworth fellow</a> <a href="http://okfnlabs.org/members/teleyinex">Daniel Lombraña González</a> reported on progress with <a href="http://crowdcrafting.org/">CrowdCrafting</a>, the citizen science platform built with <a href="http://dev.pybossa.com/">PyBossa</a>.</p>

<p>CrowdCrafting now has more than 3,500 users (though Daniel cautions that this doesn’t mean much in terms of participation), and the site now has more answers than tasks.</p>

<p>Last week, the team at <a href="http://micromappers.com/">MicroMappers</a> used CrowdCrafting to classify <a href="http://okfnlabs.org/blog/2013/11/21/newsletter.html">tweets about the typhoon disaster</a> in the Philippines. Digital mapping activists <a href="http://skytruth.org/">SkyTruth</a>, meanwhile, have used CrowdCrafting to <a href="http://crowdcrafting.org/app/frackfinder_tadpole/">map and track fracking sites</a> in the northeast United States. Daniel has also been in contact with <a href="http://www.epicollect.net/">EpiCollect</a> about a project on trash collection in Spain.</p>

<h2 id="open-data-button">Open Data Button</h2>

<p>Labs member <a href="http://okfnlabs.org/members/loleg">Oleg Lavrovsky</a> discussed the <a href="http://button.datalets.ch/">Open Data Button</a>, an interesting fork of the recently-launched <a href="https://www.openaccessbutton.org/">Open Access Button</a>.</p>

<p>The Open Access Button, an idea of the Open Science working group at <a href="http://okcon.org/">OKCon 2013</a>, is a bookmarklet that allows users to report their experiences of having their research blocked by paywalls. The Open Data Button applies this same idea to Open Data: users can use it to report their problems with legal and technical restrictions on data. (As Rufus pointed out, this ties in nicely with the <a href="https://github.com/okfn/ideas/issues/41">IsItOpenData</a> project.)</p>

<h2 id="queremos-saber">Queremos Saber</h2>

<p>Labs ally <a href="http://vitorbaptista.com/">Vítor Baptista</a> reported on a new development with <a href="http://www.queremossaber.org.br/">Queremos Saber</a>, the Brazilian FOI request portal.</p>

<p>Changes in the way the Brazilian federal government accepts FOI requests have caused Queremos Saber problems. The federal government no longer accepts requests by email, forcing the use of a specialized FOI system which they are now promoting for local governments as well. This limits the number of places that will accept requests from Queremos Saber.</p>

<p>A solution to this problem is underway: an <em>email-based API</em> that will take emails received at certain addresses (e.g. <em>ministryofhealthcare@queremossaber.org.br</em>) and turn them into instructions for a web crawler to create an FOI request in the appropriate system. An interesting side effect of this would be the creation of an <em>anonymization layer</em>, allowing users to bypass the legal requirement that FOI requests not be placed anonymously.</p>

<h2 id="philippines-projects">Philippines Projects</h2>

<p>Labs data wrangler <a href="http://okfnlabs.org/members/markbrough">Mark Brough</a> showed off a test project collecting <a href="http://markbrough.github.io/philippines/">data on aid activities in the Philippines</a>. Mark’s small static site, updated each night, collects <a href="http://iatistandard.org/">IATI</a> aid data  on projects in the Philippines and republishes it in a more browsable form.</p>

<p>Mark also discussed another data-mashup project, still in the planning stage, that would combine budget and aid data for Tanzania (or any other developing country)—similar to Publish What You Fund’s old <a href="http://publishwhatyoufund.org/uganda/">Uganda project</a> but based on a non-static dataset.</p>

<h2 id="global-economic-map">Global Economic Map</h2>

<p>Alex Peek discussed his initiative to create the <a href="http://meta.wikimedia.org/wiki/Global_Economic_Map">Global Economic Map</a>, “a collection of standardized data set of economic statistics that can be applied to every country, region and city in the world”.</p>

<p>The GEM will draw data from sources like government publications and SEC filings and will cover <a href="https://meta.wikimedia.org/wiki/Grants:IdeaLab/Global_Economic_Map#Format_and_economic_statistics">eleven statistics</a> that touch on GDP, employment, corporations, and budgets. The GEM aims to be <a href="https://meta.wikimedia.org/wiki/Grants:IdeaLab/Global_Economic_Map#Wikidata_integration">fully integrated with Wikidata</a>.</p>

<h2 id="frictionless-data">Frictionless data</h2>

<p>Finally, <a href="http://okfnlabs.org/members/rgrp">Rufus Pollock</a> discussed <a href="http://data.okfn.org/">data.okfn.org</a> and the mission of “frictionless data”: making it “as simple as possible to get the data you want into the tool of your choice.”</p>

<p>data.okfn.org aims to help achieve this goal by promoting, among other things, <a href="http://data.okfn.org/standards">simple data standards</a> and the tooling to support them. As reported in last week’s newsletter, this now includes a <a href="https://github.com/okfn/dpm">Data Package Manager</a> based on <a href="https://npmjs.org/">npm</a>, now working at a very basic level. It also includes the data.okfn.org <a href="http://data.okfn.org/tools/view">Data Package Viewer</a>, which provides a nice view on data packages hosted on GitHub, S3, or wherever else.</p>

<h2 id="improving-the-labs-site">Improving the Labs site</h2>

<p>The hangout wrapped up with a discussion of how to improve the Labs site. Besides some discussion of the possibility of a <a href="https://github.com/okfn/okfn.github.com/issues/134">one-click creation system for Open Data Maker Nights</a>, talk focused on <a href="https://github.com/okfn/okfn.github.com/issues/46">improving the projects page</a>.</p>

<p>Oleg, who has volunteered to take the lead in reforming the projects page, highlighted the need for a way to differentiate projects by their activity level and their need for more contributors. Mark agreed, suggesting also that it would be nice to be able to filter projects by the languages and technologies they use. Both ideas were proposed as a way to fill out <a href="http://www.todrobbins.com/">Tod Robbins</a>’s suggestion that the projects page needs <em>categories</em>.</p>

<p>See the <a href="http://pad.okfn.org/p/labs-hangouts">Labs hangout notes</a> for the full details of this discussion.</p>

<h2 id="get-involved">Get involved</h2>

<p>As always, Labs wants you to join in and get involved! Read more about how you can <a href="http://okfnlabs.org/join/">join the community</a> and participate by coding, wrangling data, or doing outreach and engagement, and have a look at the <a href="http://okfnlabs.org/ideas/">Ideas Page</a> to see what other members have been thinking.</p>



