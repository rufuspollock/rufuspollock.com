---
title: >-
  Getting Better All the Time? Research Output in Economics 1970-2005
slug: getting-better-all-the-time-research-output-in-economics-1970-2005
date: 2008-01-21T12:13:10
themes: ['Information Economy']
tags: []
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 235
---

While at the EEA/ESEM summer conference, confronted by the multitude of papers and provoked by the [comments of Janos Kornai and Assar Lindbeck](http://www.rufuspollock.org/archives/214), I wondered how things had changed over the last half-century. How many more papers (and economists) were there compared to 20/30/50 years ago, and how had the nature and the quality of research change (at least partially as a result as a change in this quantity)?

The first question, while the less interesting, had the advantage of lending itself to ready quantitative analysis, so it was to this I first applied myself. Armed with my AEA password I quickly hacked up a [script to scrape total publications per annum out of econlit](http://knowledgeforge.net/econ/svn/trunk/data/dfc885a0-5483-4b75-a514-1438721ee6cc/data.py)
(note that this obviously does *not* include my real password) and posted the results as a [dataset on OpenEconomics.net](dataset).

Having now finally got round to writing it up here (after several months delay), the results can be seen below -- as  well as in the original plot linked from the [dataset page](dataset) the graph renders via javascript and may have some issues in IE so if you don't see anything try Firefox ...). The key points to note are:

  * Output has more than five-tupled between 1970 and today (~5k to ~28k).
  * There is a suggestion of a structural break in the data around 1990 with the rate of growth being higher after that point.

Thus, it would appear there has been a substantial increase in output -- for comparison world GDP has increased by slightly more than 2x 1970-2005 (see e.g. [Delong's estimates](http://www.j-bradford-delong.net/TCEH/1998_Draft/World_GDP/Estimating_World_GDP.html) and US GDP increased by slightly under 3x (3.7 trillion to 11trillion) over the same period.

The next step is to determine what is driving this increase and how much it actually corresponds to an increase in 'knowledge'. In particular one should compute output per (economist) capita and look at other possible explanations of the rise, for example: technology (computers and communications), different working practices, institutional factors -- e.g. greater focus on published research output (the research assessment exercises). The harder question will be the second item: trying to determine how much this increase in raw quantity actually signifies an increase in real understanding and know-how.

[dataset]: http://openeconomics.net/store/dfc885a0-5483-4b75-a514-1438721ee6cc

<script type="text/javascript" src="http://m.okfn.org/ext/mochikit/MochiKit.js">//pointless jscript comment</script>
<script type="text/javascript" src="http://m.okfn.org/ext/plotkit/PlotKit_Packed.js"> //pointless jscript comment</script>
<script type="text/javascript" src="http://m.okfn.org/ext/plotkit/excanvas.js">//pointless jscript comment</script>
<script type="text/javascript">
function drawPlot() {
    var options = { "xOriginIsZero" : false}
    var layout = new PlotKit.Layout("line", options);
    layout.addDatasetFromTable("datatable", $("table-econ-papers"));
    layout.evaluate();
    var canvas = MochiKit.DOM.getElement("plot");
    var plotter = new PlotKit.SweetCanvasRenderer(canvas, layout, {});
    plotter.render();
}
MochiKit.DOM.addLoadEvent(drawPlot);
</script>
<div>
<canvas id="plot" height="500" width="500"></canvas>
</div>
<div style="margin: 2em;">
<table id="table-econ-papers" border="1" style="text-align: center;">
<thead><tr><th>Year</th><th>Number of Articles</th></tr></thead>
<tbody><tr><td>1970</td><td>5081</td></tr>
<tr><td>1971</td><td>5012</td></tr><tr><td>1972</td><td>5685</td></tr>
<tr><td>1973</td><td>5981</td></tr><tr><td>1974</td><td>5965</td></tr>
<tr><td>1975</td><td>5997</td></tr><tr><td>1976</td><td>6403</td></tr>
<tr><td>1977</td><td>7077</td></tr><tr><td>1978</td><td>7573</td></tr>
<tr><td>1979</td><td>7799</td></tr><tr><td>1980</td><td>8220</td></tr>
<tr><td>1981</td><td>8420</td></tr><tr><td>1982</td><td>8387</td></tr>
<tr><td>1983</td><td>9418</td></tr><tr><td>1984</td><td>9552</td></tr>
<tr><td>1985</td><td>9918</td></tr><tr><td>1986</td><td>9872</td></tr>
<tr><td>1987</td><td>9918</td></tr><tr><td>1988</td><td>10551</td></tr>
<tr><td>1989</td><td>10768</td></tr><tr><td>1990</td><td>11254</td></tr>
<tr><td>1991</td><td>11905</td></tr><tr><td>1992</td><td>13108</td></tr>
<tr><td>1993</td><td>13493</td></tr><tr><td>1994</td><td>14374</td></tr>
<tr><td>1995</td><td>15825</td></tr><tr><td>1996</td><td>17692</td></tr>
<tr><td>1997</td><td>18385</td></tr><tr><td>1998</td><td>19869</td></tr>
<tr><td>1999</td><td>20818</td></tr><tr><td>2000</td><td>21836</td></tr>
<tr><td>2001</td><td>22322</td></tr><tr><td>2002</td><td>23331</td></tr>
<tr><td>2003</td><td>23984</td></tr><tr><td>2004</td><td>25843</td></tr>
<tr><td>2005</td><td>27738</td></tr>
</tbody></table>
		</div>


