---
title: >-
  Web Scraping with CSS Selectors in Node using JSDOM or Cheerio
slug: web-scraping-with-css-selectors-in-node-using-jsdom-or-cheerio
date: 2013-01-15T00:00:00
themes: []
tags: []
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1248
---

<p>I’ve traditionally used python for web scraping but I’d been increasingly thinking about using Node given that it is pure JS and therefore could be a more natural fit when getting info out of <em>web</em> pages.</p>

<p>In particular, when my first steps when looking to extract information from a website is to open up the Chrome Developer tools (or Firebug in Firefox) and try and extract information by inspecting the page and playing around in the console - the latter is especially attractive if jQuery is available.</p>

<p>What I often end up with from this is a few lines of jQuery selectors. My desire here was to find a way to directly reuse these same css selectors I use in my browser experimentation directly in the scraping script. Now, things like <a href="http://packages.python.org/pyquery/">pyquery</a> do exist in python (and there is some css selector support in the brilliant BeautifulSoup) but a connection with something like Node seems even more natural - it is after the JS engine from a browser!</p>

<h2 id="uk-crime-data">UK Crime Data</h2>

<p>My immediate motivation for this work was wanting to play around with the <a href="http://police.uk/data">UK Crime data</a> (all <a href="http://opendefinition.org/">open data</a> now!).</p>

<p>To do this I needed to:</p>

<ol>
  <li>Get the data in consolidated form by scraping the file list and data files from <a href="http://police.uk/data/">http://police.uk/data/</a> - while they commendably provide the data in bulk there is no single file to download, instead there is one file per force per month. </li>
  <li>Do data cleaning and analysis - this included some fun geo-conversion and csv parsing</li>
</ol>

<p>I’m just going to talk about the first part in what folllows - though I hope to cover the second part in a follow up post.</p>

<p>I should also note that all the code used for scraping and working with this data can be found in the <a href="https://github.com/datasets/crime-uk">UK Crime dataset data package on GitHub</a> on Github - <a href="https://github.com/datasets/crime-uk/blob/master/scripts/scrape.js">scrape.js file is here</a>. You can also see some of the ongoing results of these data experiments in an experimental <a href="http://okfnlabs.org/crime/">UK crime “dashboard” here</a>.</p>

<h2 id="scraping-using-css-selectors-in-node">Scraping using CSS Selectors in Node</h2>

<p>Two options present themselves when doing simple scraping using css selectors in node.js:</p>

<ul>
  <li>Using <a href="https://github.com/tmpvar/jsdom">jsdom</a> (+ jquery)</li>
  <li>Using <a href="https://github.com/MatthewMueller/cheerio">cheerio</a> (which provides jquery like access to html) + something to retrieve html (my preference is <a href="https://github.com/mikeal/request">request</a> but you can just uses <a href="http://nodejs.org/docs/v0.6.11/api/http.html#http.request">node’s built in http request</a>)</li>
</ul>

<p>For the UK crime work I used jsdom but I’ve subsequently used cheerio as it is substantially faster so I’ll cover both here (I didn’t discover cheerio until I’d started on the crime work!).</p>

<p>Here’s an excerpted code example (full example in the <a href="https://github.com/datasets/crime-uk/blob/master/scripts/scrape.js">source file</a>):</p>

<div class="highlight"><pre><code class="language-javascript" data-lang="javascript"><span class="kd">var</span> <span class="nx">url</span> <span class="o">=</span> <span class="s1">&#39;http://police.uk/data&#39;</span><span class="p">;</span>
<span class="c1">// holder for results</span>
<span class="kd">var</span> <span class="nx">out</span> <span class="o">=</span> <span class="p">{</span>
  <span class="s1">&#39;streets&#39;</span><span class="o">:</span> <span class="p">[]</span>
<span class="p">}</span>
<span class="nx">jsdom</span><span class="p">.</span><span class="nx">env</span><span class="p">({</span>
  <span class="nx">html</span><span class="o">:</span> <span class="nx">url</span><span class="p">,</span>
  <span class="nx">scripts</span><span class="o">:</span> <span class="p">[</span>
    <span class="s1">&#39;http://code.jquery.com/jquery.js&#39;</span>
  <span class="p">],</span>
  <span class="nx">done</span><span class="o">:</span> <span class="kd">function</span><span class="p">(</span><span class="nx">errors</span><span class="p">,</span> <span class="nb">window</span><span class="p">)</span> <span class="p">{</span>
    <span class="kd">var</span> <span class="nx">$</span> <span class="o">=</span> <span class="nb">window</span><span class="p">.</span><span class="nx">$</span><span class="p">;</span>
    <span class="c1">// find all the html links to the street zip files</span>
    <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;#downloads .months table tr td:nth-child(2) a&#39;</span><span class="p">).</span><span class="nx">each</span><span class="p">(</span><span class="kd">function</span><span class="p">(</span><span class="nx">idx</span><span class="p">,</span> <span class="nx">elem</span><span class="p">)</span> <span class="p">{</span>
      <span class="c1">// push the url (href attribute) onto the list</span>
      <span class="nx">out</span><span class="p">[</span><span class="s1">&#39;streets&#39;</span><span class="p">].</span><span class="nx">push</span><span class="p">(</span> <span class="nx">$</span><span class="p">(</span><span class="nx">elem</span><span class="p">).</span><span class="nx">attr</span><span class="p">(</span><span class="s1">&#39;href&#39;</span><span class="p">)</span> <span class="p">);</span>
    <span class="p">});</span>
  <span class="p">});</span>
<span class="p">});</span></code></pre></div>

<p>As an example of Cheerio scraping here’s an example from work <a href="https://github.com/datasets/opented">scraping info the EU’s TED database</a> (sample <a href="http://files.opented.org.s3.amazonaws.com/scraped/100120-2011/summary.html">html file</a>):</p>

<div class="highlight"><pre><code class="language-javascript" data-lang="javascript"><span class="kd">var</span> <span class="nx">url</span> <span class="o">=</span> <span class="s1">&#39;http://files.opented.org.s3.amazonaws.com/scraped/100120-2011/summary.html&#39;</span><span class="p">;</span>
<span class="c1">// place to store results</span>
<span class="kd">var</span> <span class="nx">data</span> <span class="o">=</span> <span class="p">{};</span>
<span class="c1">// do the request using the request library</span>
<span class="nx">request</span><span class="p">(</span><span class="nx">url</span><span class="p">,</span> <span class="kd">function</span><span class="p">(</span><span class="nx">err</span><span class="p">,</span> <span class="nx">resp</span><span class="p">,</span> <span class="nx">body</span><span class="p">){</span>
  <span class="nx">$</span> <span class="o">=</span> <span class="nx">cheerio</span><span class="p">.</span><span class="nx">load</span><span class="p">(</span><span class="nx">body</span><span class="p">);</span>

  <span class="nx">data</span><span class="p">.</span><span class="nx">winnerDetails</span> <span class="o">=</span> <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;.txtmark .addr&#39;</span><span class="p">).</span><span class="nx">html</span><span class="p">();</span>

  <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;.mlioccur .txtmark&#39;</span><span class="p">).</span><span class="nx">each</span><span class="p">(</span><span class="kd">function</span><span class="p">(</span><span class="nx">i</span><span class="p">,</span> <span class="nx">html</span><span class="p">)</span> <span class="p">{</span>
    <span class="kd">var</span> <span class="nx">spans</span> <span class="o">=</span> <span class="nx">$</span><span class="p">(</span><span class="nx">html</span><span class="p">).</span><span class="nx">find</span><span class="p">(</span><span class="s1">&#39;span&#39;</span><span class="p">);</span>
    <span class="kd">var</span> <span class="nx">span0</span> <span class="o">=</span> <span class="nx">$</span><span class="p">(</span><span class="nx">spans</span><span class="p">[</span><span class="mi">0</span><span class="p">]);</span>
    <span class="k">if</span> <span class="p">(</span><span class="nx">span0</span><span class="p">.</span><span class="nx">text</span><span class="p">()</span> <span class="o">==</span> <span class="s1">&#39;Initial estimated total value of the contract &#39;</span><span class="p">)</span> <span class="p">{</span>
      <span class="kd">var</span> <span class="nx">amount</span> <span class="o">=</span> <span class="nx">$</span><span class="p">(</span><span class="nx">spans</span><span class="p">[</span><span class="mi">4</span><span class="p">]).</span><span class="nx">text</span><span class="p">()</span>
      <span class="nx">data</span><span class="p">.</span><span class="nx">finalamount</span> <span class="o">=</span> <span class="nx">cleanAmount</span><span class="p">(</span><span class="nx">amount</span><span class="p">);</span>
      <span class="nx">data</span><span class="p">.</span><span class="nx">initialamount</span> <span class="o">=</span> <span class="nx">cleanAmount</span><span class="p">(</span><span class="nx">$</span><span class="p">(</span><span class="nx">spans</span><span class="p">[</span><span class="mi">1</span><span class="p">]).</span><span class="nx">text</span><span class="p">());</span>
    <span class="p">}</span>
  <span class="p">});</span>
<span class="p">});</span></code></pre></div>



