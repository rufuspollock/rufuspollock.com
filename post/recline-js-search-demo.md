---
title: >-
  Recline JS Search Demo
slug: recline-js-search-demo
date: 2012-11-01T00:00:00
themes: []
tags: []
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1251
---

<p><a href="http://reclinejs.com/"><img src="http://assets.okfn.org/p/recline/img/logo.png" style="float: right; height: 100px;" alt="Recline JS" /></a></p>

<p>We’ve recently finished a demo for ReclineJS showing how it can be used to build
JS-based (ajax-style) search interfaces in minutes (or even seconds!):
<a href="http://reclinejs.com/demos/search/">http://reclinejs.com/demos/search/</a></p>

<p>Because of Recline’s <a href="http://reclinejs.com/docs/backends.html">pluggable backends</a> you get out of the box
support for data sources such as SOLR, Google Spreadsheet, ElasticSearch, or
plain old JSON or CSV – see examples below for live examples of using
different backends.</p>

<p>Interested in using this yourself? The <a href="">(prettified) source JS for the demo is
available</a> (plus the <a href="http://reclinejs.com/demos/search/demo.search.app.js">raw version</a>) and it shows how simple
it is to build an app like this using Recline – plus it has tips on how
to customize and extend).</p>

<p><a href="http://reclinejs.com/demos/search/"><img src="http://i.imgur.com/Ja8SV.png" alt="demo" style="width: 100%" /></a></p>

<h2 id="more-examples">More Examples</h2>

<p>In addition to the simple example with local data there are several other
examples showing how one can use this with other data sources including Google
Docs and SOLR: </p>

<ol>
  <li>
    <p>A <a href="http://reclinejs.com/demos/search/?backend=gdocs&amp;url=https://docs.google.com/spreadsheet/ccc?key=0Aon3JiuouxLUdExXSTl2Y01xZEszOTBFZjVzcGtzVVE">search example using a google docs listing Shell Oil spills in the Niger
delta</a></p>
  </li>
  <li>
    <p>A <a href="http://reclinejs.com/demos/search/?backend=solr&amp;url=http://openspending.org/api/search">search example running of OpenSpending SOLR
API</a>
– we suggest searching for something interesting like “Drugs” or “Nuclear
power”!</p>
  </li>
</ol>

<h2 id="code">Code</h2>

<p>The full <a href="">(prettified) source JS for the demo is available</a>
(plus the <a href="http://reclinejs.com/demos/search/demo.search.app.js">raw version</a>) but here’s a key code sample to give a flavour:</p>

<div class="highlight"><pre><code class="language-javascript" data-lang="javascript"><span class="c1">// ## Simple Search View</span>
<span class="c1">//</span>
<span class="c1">// This is a simple bespoke Backbone view for the Search. It Pulls together</span>
<span class="c1">// various Recline UI components and the central Dataset and Query (state)</span>
<span class="c1">// object</span>
<span class="c1">//</span>
<span class="c1">// It also provides simple support for customization e.g. of template for list of results</span>
<span class="c1">// </span>
<span class="c1">//      var view = new SearchView({</span>
<span class="c1">//        el: $(&#39;some-element&#39;),</span>
<span class="c1">//        model: dataset</span>
<span class="c1">//        // EITHER a mustache template (passed a JSON version of recline.Model.Record</span>
<span class="c1">//        // OR a function which receives a record in JSON form and returns html</span>
<span class="c1">//        template: mustache-template-or-function</span>
<span class="c1">//      });</span>
<span class="kd">var</span> <span class="nx">SearchView</span> <span class="o">=</span> <span class="nx">Backbone</span><span class="p">.</span><span class="nx">View</span><span class="p">.</span><span class="nx">extend</span><span class="p">({</span>
  <span class="nx">initialize</span><span class="o">:</span> <span class="kd">function</span><span class="p">(</span><span class="nx">options</span><span class="p">)</span> <span class="p">{</span>
    <span class="k">this</span><span class="p">.</span><span class="nx">el</span> <span class="o">=</span> <span class="nx">$</span><span class="p">(</span><span class="k">this</span><span class="p">.</span><span class="nx">el</span><span class="p">);</span>
    <span class="nx">_</span><span class="p">.</span><span class="nx">bindAll</span><span class="p">(</span><span class="k">this</span><span class="p">,</span> <span class="s1">&#39;render&#39;</span><span class="p">);</span>
    <span class="k">this</span><span class="p">.</span><span class="nx">recordTemplate</span> <span class="o">=</span> <span class="nx">options</span><span class="p">.</span><span class="nx">template</span><span class="p">;</span>
    <span class="c1">// Every time we do a search the recline.Dataset.records Backbone</span>
    <span class="c1">// collection will get reset. We want to re-render each time!</span>
    <span class="k">this</span><span class="p">.</span><span class="nx">model</span><span class="p">.</span><span class="nx">records</span><span class="p">.</span><span class="nx">bind</span><span class="p">(</span><span class="s1">&#39;reset&#39;</span><span class="p">,</span> <span class="k">this</span><span class="p">.</span><span class="nx">render</span><span class="p">);</span>
    <span class="k">this</span><span class="p">.</span><span class="nx">templateResults</span> <span class="o">=</span> <span class="nx">options</span><span class="p">.</span><span class="nx">template</span><span class="p">;</span>
  <span class="p">},</span>

  <span class="c1">// overall template for this view</span>
  <span class="nx">template</span><span class="o">:</span> <span class="s1">&#39; \</span>
<span class="s1">    &lt;div class=&quot;controls&quot;&gt; \</span>
<span class="s1">      &lt;div class=&quot;query-here&quot;&gt;&lt;/div&gt; \</span>
<span class="s1">    &lt;/div&gt; \</span>
<span class="s1">    &lt;div class=&quot;total&quot;&gt;&lt;h2&gt;&lt;span&gt;&lt;/span&gt; records found&lt;/h2&gt;&lt;/div&gt; \</span>
<span class="s1">    &lt;div class=&quot;body&quot;&gt; \</span>
<span class="s1">      &lt;div class=&quot;sidebar&quot;&gt;&lt;/div&gt; \</span>
<span class="s1">      &lt;div class=&quot;results&quot;&gt; \</span>
<span class="s1">        } \</span>
<span class="s1">      &lt;/div&gt; \</span>
<span class="s1">    &lt;/div&gt; \</span>
<span class="s1">    &lt;div class=&quot;pager-here&quot;&gt;&lt;/div&gt; \</span>
<span class="s1">  &#39;</span><span class="p">,</span>
 
  <span class="c1">// render the view</span>
  <span class="nx">render</span><span class="o">:</span> <span class="kd">function</span><span class="p">()</span> <span class="p">{</span>
    <span class="kd">var</span> <span class="nx">results</span> <span class="o">=</span> <span class="s1">&#39;&#39;</span><span class="p">;</span>
    <span class="k">if</span> <span class="p">(</span><span class="nx">_</span><span class="p">.</span><span class="nx">isFunction</span><span class="p">(</span><span class="k">this</span><span class="p">.</span><span class="nx">templateResults</span><span class="p">))</span> <span class="p">{</span>
      <span class="kd">var</span> <span class="nx">results</span> <span class="o">=</span> <span class="nx">_</span><span class="p">.</span><span class="nx">map</span><span class="p">(</span><span class="k">this</span><span class="p">.</span><span class="nx">model</span><span class="p">.</span><span class="nx">records</span><span class="p">.</span><span class="nx">toJSON</span><span class="p">(),</span> <span class="k">this</span><span class="p">.</span><span class="nx">templateResults</span><span class="p">).</span><span class="nx">join</span><span class="p">(</span><span class="s1">&#39;\n&#39;</span><span class="p">);</span>
    <span class="p">}</span> <span class="k">else</span> <span class="p">{</span>
      <span class="c1">// templateResults is just for one result ...</span>
      <span class="kd">var</span> <span class="nx">tmpl</span> <span class="o">=</span> <span class="s1">&#39;&#39;</span> <span class="o">+</span> <span class="k">this</span><span class="p">.</span><span class="nx">templateResults</span> <span class="o">+</span> <span class="s1">&#39;&#39;</span><span class="p">;</span> 
      <span class="kd">var</span> <span class="nx">results</span> <span class="o">=</span> <span class="nx">Mustache</span><span class="p">.</span><span class="nx">render</span><span class="p">(</span><span class="nx">tmpl</span><span class="p">,</span> <span class="p">{</span>
        <span class="nx">records</span><span class="o">:</span> <span class="k">this</span><span class="p">.</span><span class="nx">model</span><span class="p">.</span><span class="nx">records</span><span class="p">.</span><span class="nx">toJSON</span><span class="p">()</span>
      <span class="p">});</span>
    <span class="p">}</span>
    <span class="kd">var</span> <span class="nx">html</span> <span class="o">=</span> <span class="nx">Mustache</span><span class="p">.</span><span class="nx">render</span><span class="p">(</span><span class="k">this</span><span class="p">.</span><span class="nx">template</span><span class="p">,</span> <span class="p">{</span>
      <span class="nx">results</span><span class="o">:</span> <span class="nx">results</span>
    <span class="p">});</span>
    <span class="k">this</span><span class="p">.</span><span class="nx">el</span><span class="p">.</span><span class="nx">html</span><span class="p">(</span><span class="nx">html</span><span class="p">);</span>

    <span class="c1">// Set the total records found info</span>
    <span class="k">this</span><span class="p">.</span><span class="nx">el</span><span class="p">.</span><span class="nx">find</span><span class="p">(</span><span class="s1">&#39;.total span&#39;</span><span class="p">).</span><span class="nx">text</span><span class="p">(</span><span class="k">this</span><span class="p">.</span><span class="nx">model</span><span class="p">.</span><span class="nx">recordCount</span><span class="p">);</span>

    <span class="c1">// ### Now setup all the extra mini-widgets</span>
    <span class="c1">// </span>
    <span class="c1">// Facets, Pager, QueryEditor etc</span>

    <span class="kd">var</span> <span class="nx">view</span> <span class="o">=</span> <span class="k">new</span> <span class="nx">recline</span><span class="p">.</span><span class="nx">View</span><span class="p">.</span><span class="nx">FacetViewer</span><span class="p">({</span>
      <span class="nx">model</span><span class="o">:</span> <span class="k">this</span><span class="p">.</span><span class="nx">model</span>
    <span class="p">});</span>
    <span class="nx">view</span><span class="p">.</span><span class="nx">render</span><span class="p">();</span>
    <span class="k">this</span><span class="p">.</span><span class="nx">el</span><span class="p">.</span><span class="nx">find</span><span class="p">(</span><span class="s1">&#39;.sidebar&#39;</span><span class="p">).</span><span class="nx">append</span><span class="p">(</span><span class="nx">view</span><span class="p">.</span><span class="nx">el</span><span class="p">);</span>

    <span class="kd">var</span> <span class="nx">pager</span> <span class="o">=</span> <span class="k">new</span> <span class="nx">recline</span><span class="p">.</span><span class="nx">View</span><span class="p">.</span><span class="nx">Pager</span><span class="p">({</span>
      <span class="nx">model</span><span class="o">:</span> <span class="k">this</span><span class="p">.</span><span class="nx">model</span><span class="p">.</span><span class="nx">queryState</span>
    <span class="p">});</span>
    <span class="k">this</span><span class="p">.</span><span class="nx">el</span><span class="p">.</span><span class="nx">find</span><span class="p">(</span><span class="s1">&#39;.pager-here&#39;</span><span class="p">).</span><span class="nx">append</span><span class="p">(</span><span class="nx">pager</span><span class="p">.</span><span class="nx">el</span><span class="p">);</span>

    <span class="kd">var</span> <span class="nx">queryEditor</span> <span class="o">=</span> <span class="k">new</span> <span class="nx">recline</span><span class="p">.</span><span class="nx">View</span><span class="p">.</span><span class="nx">QueryEditor</span><span class="p">({</span>
      <span class="nx">model</span><span class="o">:</span> <span class="k">this</span><span class="p">.</span><span class="nx">model</span><span class="p">.</span><span class="nx">queryState</span>
    <span class="p">});</span>
    <span class="k">this</span><span class="p">.</span><span class="nx">el</span><span class="p">.</span><span class="nx">find</span><span class="p">(</span><span class="s1">&#39;.query-here&#39;</span><span class="p">).</span><span class="nx">append</span><span class="p">(</span><span class="nx">queryEditor</span><span class="p">.</span><span class="nx">el</span><span class="p">);</span>
  <span class="p">}</span>
<span class="p">});</span></code></pre></div>



