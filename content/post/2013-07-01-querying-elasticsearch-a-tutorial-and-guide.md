---
title: >-
  Querying ElasticSearch - A Tutorial and Guide
slug: querying-elasticsearch-a-tutorial-and-guide
date: 2013-07-01T00:00:00
themes: []
tags: []
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1241
---

<p>ElasticSearch is a great open-source search tool that’s built on Lucene (like
SOLR) but is natively JSON + RESTful. Its been used quite a bit at the <a href="http://okfn.org/">Open
Knowledge Foundation</a> over the last few years. Plus, as its easy to
<a href="http://www.elasticsearch.org/guide/reference/setup/">setup locally</a> its an attractive option for digging into data on your
local machine.</p>

<p>While its general interface is pretty natural, I must confess I’ve sometimes
struggled to find my way around ElasticSearch’s powerful, but also quite
complex, query system and the associated JSON-based “<a href="http://www.elasticsearch.org/guide/reference/query-dsl/">query DSL</a>” (domain
specific language).</p>

<p>This post therefore provides a simple introduction and guide to querying
ElasticSearch that provides a short overview of how it all works together with
a good set of examples of some of the most standard queries.</p>

<div class="alert alert-success">
Note: here at Open Knowledge Foundation Labs we have several open-source
ElasticSearch related project including an <strong><a href="http://okfnlabs.org/projects/elasticsearch-js/">easy-to-use Javascript Library for
ElasticSearch</a></strong> and the <strong><a href="http://okfnlabs.org/projects/reclinejs/">Recline suite of JS Data Components</a></strong>
which make it easy and fast to build powerful JS+HTML-based interfaces to
ElasticSearch.
</div>

<p><strong>Table of Contents</strong></p>

<ul id="markdown-toc">
  <li><a href="http://okfnlabs.org/blog/2013/07/01/elasticsearch-query-tutorial.html#terminology-and-urls">Terminology and URLs</a></li>
  <li><a href="http://okfnlabs.org/blog/2013/07/01/elasticsearch-query-tutorial.html#quickstart">Quickstart</a>    <ul>
      <li><a href="http://okfnlabs.org/blog/2013/07/01/elasticsearch-query-tutorial.html#curl-or-browser">cURL (or Browser)</a></li>
      <li><a href="http://okfnlabs.org/blog/2013/07/01/elasticsearch-query-tutorial.html#javascript">Javascript</a></li>
      <li><a href="http://okfnlabs.org/blog/2013/07/01/elasticsearch-query-tutorial.html#python">Python</a></li>
    </ul>
  </li>
  <li><a href="http://okfnlabs.org/blog/2013/07/01/elasticsearch-query-tutorial.html#querying">Querying</a>    <ul>
      <li><a href="http://okfnlabs.org/blog/2013/07/01/elasticsearch-query-tutorial.html#basic-queries-using-only-the-query-string">Basic Queries Using Only the Query String</a></li>
      <li><a href="http://okfnlabs.org/blog/2013/07/01/elasticsearch-query-tutorial.html#full-query-api">Full Query API</a></li>
    </ul>
  </li>
  <li><a href="http://okfnlabs.org/blog/2013/07/01/elasticsearch-query-tutorial.html#query-language">Query Language</a>    <ul>
      <li><a href="http://okfnlabs.org/blog/2013/07/01/elasticsearch-query-tutorial.html#query-dsl-overview">Query DSL: Overview</a></li>
      <li><a href="http://okfnlabs.org/blog/2013/07/01/elasticsearch-query-tutorial.html#examples">Examples</a>        <ul>
          <li><a href="http://okfnlabs.org/blog/2013/07/01/elasticsearch-query-tutorial.html#match-all--find-everything">Match all / Find Everything</a></li>
          <li><a href="http://okfnlabs.org/blog/2013/07/01/elasticsearch-query-tutorial.html#classic-search-box-style-full-text-query">Classic Search-Box Style Full-Text Query</a></li>
          <li><a href="http://okfnlabs.org/blog/2013/07/01/elasticsearch-query-tutorial.html#filter-on-one-field">Filter on One Field</a></li>
          <li><a href="http://okfnlabs.org/blog/2013/07/01/elasticsearch-query-tutorial.html#find-all-documents-with-value-in-a-range">Find all documents with value in a range</a></li>
          <li><a href="http://okfnlabs.org/blog/2013/07/01/elasticsearch-query-tutorial.html#full-text-query-plus-filter-on-a-field">Full-Text Query plus Filter on a Field</a></li>
          <li><a href="http://okfnlabs.org/blog/2013/07/01/elasticsearch-query-tutorial.html#filter-on-two-fields">Filter on two fields</a></li>
          <li><a href="http://okfnlabs.org/blog/2013/07/01/elasticsearch-query-tutorial.html#geospatial-query-to-find-results-near-a-given-point">Geospatial Query to find results near a given point</a></li>
        </ul>
      </li>
      <li><a href="http://okfnlabs.org/blog/2013/07/01/elasticsearch-query-tutorial.html#facets">Facets</a></li>
    </ul>
  </li>
  <li><a href="http://okfnlabs.org/blog/2013/07/01/elasticsearch-query-tutorial.html#appendix">Appendix</a>    <ul>
      <li><a href="http://okfnlabs.org/blog/2013/07/01/elasticsearch-query-tutorial.html#adding-updating-and-deleting-data">Adding, Updating and Deleting Data</a></li>
      <li><a href="http://okfnlabs.org/blog/2013/07/01/elasticsearch-query-tutorial.html#schema-mapping">Schema Mapping</a></li>
      <li><a href="http://okfnlabs.org/blog/2013/07/01/elasticsearch-query-tutorial.html#jsonp-support">JSONP support</a></li>
    </ul>
  </li>
</ul>

<h2 id="terminology-and-urls">Terminology and URLs</h2>

<p>Throughout <code>{endpoint}</code> refers to the ElasticSearch <a href="http://www.elasticsearch.org/guide/reference/glossary/#type">index type</a> (aka
table). Note that ElasticSearch often let’s you run the same queries on both
“<a href="http://www.elasticsearch.org/guide/reference/glossary/#index">indexes</a>” (aka database) and types.</p>

<p>If you were just using ElasticSearch standalone an example of an endpoint would be:
http://localhost:9200/gold-prices/monthly-price-table.</p>

<p>Key urls:</p>

<ul>
  <li>
    <p>Query: <code>{endpoint}/_search</code> (in ElasticSearch &lt; 0.19 this will return an
error if visited without a query parameter)</p>

    <ul>
      <li>Query example: <code>{endpoint}/_search?size=5&amp;pretty=true</code></li>
    </ul>
  </li>
  <li>
    <p>Schema (Mapping): <code>{endpoint}/_mapping</code></p>
  </li>
</ul>

<h2 id="quickstart">Quickstart</h2>

<h3 id="curl-or-browser">cURL (or Browser)</h3>

<p>The following examples utilize the <a href="http://curl.haxx.se/">cURL</a> command line utility. If you prefer,
you you can just open the relevant urls in your browser:</p>

<div class="highlight"><pre><code class="language-bash" data-lang="bash"><span class="c"># query for documents / rows with title field containing &#39;jones&#39;</span>
    <span class="c"># added pretty=true to get the json results pretty printed</span>
    curl <span class="o">{</span>endpoint<span class="o">}</span>/_search?q<span class="o">=</span>title:jones<span class="p">&amp;</span><span class="nv">size</span><span class="o">=</span>5<span class="p">&amp;</span><span class="nv">pretty</span><span class="o">=</span><span class="nb">true</span></code></pre></div>

<p>Adding some data:</p>

<div class="highlight"><pre><code class="language-bash" data-lang="bash"><span class="c"># Data (argument to -d) should be a JSON document</span>
    curl -X POST  <span class="o">{</span>endpoint<span class="o">}</span> -d <span class="s1">&#39;{</span>
<span class="s1">      &quot;title&quot;: &quot;jones&quot;,</span>
<span class="s1">      &quot;amount&quot;: 5.7</span>
<span class="s1">    }&#39;</span></code></pre></div>

<h3 id="javascript">Javascript</h3>

<p>A simple ajax (JSONP) request to the data API using jQuery:</p>

<div class="highlight"><pre><code class="language-javascript" data-lang="javascript"><span class="kd">var</span> <span class="nx">data</span> <span class="o">=</span> <span class="p">{</span>
      <span class="nx">size</span><span class="o">:</span> <span class="mi">5</span> <span class="c1">// get 5 results</span>
      <span class="nx">q</span><span class="o">:</span> <span class="s1">&#39;title:jones&#39;</span> <span class="c1">// query on the title field for &#39;jones&#39;</span>
    <span class="p">};</span>
    <span class="nx">$</span><span class="p">.</span><span class="nx">ajax</span><span class="p">({</span>
      <span class="nx">url</span><span class="o">:</span> <span class="p">{</span><span class="nx">endpoint</span><span class="p">}</span><span class="o">/</span><span class="nx">_search</span><span class="p">,</span>
      <span class="nx">dataType</span><span class="o">:</span> <span class="s1">&#39;jsonp&#39;</span><span class="p">,</span>
      <span class="nx">success</span><span class="o">:</span> <span class="kd">function</span><span class="p">(</span><span class="nx">data</span><span class="p">)</span> <span class="p">{</span>
        <span class="nx">alert</span><span class="p">(</span><span class="s1">&#39;Total results found: &#39;</span> <span class="o">+</span> <span class="nx">data</span><span class="p">.</span><span class="nx">hits</span><span class="p">.</span><span class="nx">total</span><span class="p">)</span>
      <span class="p">}</span>
    <span class="p">});</span></code></pre></div>

<p><em>Note: we’ve written a simple <a href="https://github.com/okfn/elasticsearch.js">JS library for ElasticSearch</a> which makes working with ElasticSearch much easier. Here’s a sample:</em></p>

<div class="highlight"><pre><code class="language-javascript" data-lang="javascript"><span class="c1">// Your ElasticSearch instance is running at http://localhost:9200/</span>
<span class="c1">// We are using index &#39;twitter&#39; and type (table) &#39;tweet&#39;</span>
<span class="kd">var</span> <span class="nx">endpoint</span> <span class="o">=</span> <span class="s1">&#39;http://localhost:9200/twitter/tweet&#39;</span><span class="p">;</span>

<span class="c1">// Table = an ElasticSearch Type (aka Table)</span>
<span class="c1">// http://www.elasticsearch.org/guide/reference/glossary/#type</span>
<span class="kd">var</span> <span class="nx">table</span> <span class="o">=</span> <span class="nx">ES</span><span class="p">.</span><span class="nx">Table</span><span class="p">(</span><span class="nx">endpoint</span><span class="p">);</span>

<span class="c1">// Create some data</span>
<span class="nx">table</span><span class="p">.</span><span class="nx">upsert</span><span class="p">({</span>
  <span class="nx">id</span><span class="o">:</span> <span class="s1">&#39;123&#39;</span><span class="p">,</span>
  <span class="nx">title</span><span class="o">:</span> <span class="s1">&#39;My new tweet&#39;</span>
<span class="p">}).</span><span class="nx">done</span><span class="p">(</span><span class="kd">function</span><span class="p">()</span> <span class="p">{</span>
  <span class="c1">// now get it</span>
  <span class="nx">table</span><span class="p">.</span><span class="nx">get</span><span class="p">(</span><span class="s1">&#39;123&#39;</span><span class="p">).</span><span class="nx">done</span><span class="p">(</span><span class="kd">function</span><span class="p">(</span><span class="nx">doc</span><span class="p">)</span> <span class="p">{</span>
    <span class="nx">console</span><span class="p">.</span><span class="nx">log</span><span class="p">(</span><span class="nx">doc</span><span class="p">);</span>
  <span class="p">});</span>
<span class="p">});</span>

<span class="c1">// Query for data</span>
<span class="c1">// Queries follow Recline Query spec -</span>
<span class="c1">// http://okfnlabs.org/recline/docs/models.html#query-structure</span>
<span class="c1">// (very similar to ES)</span>
<span class="nx">table</span><span class="p">.</span><span class="nx">query</span><span class="p">({</span>
  <span class="nx">q</span><span class="o">:</span> <span class="s1">&#39;hello&#39;</span>
  <span class="nx">filters</span><span class="o">:</span> <span class="p">[</span>
    <span class="p">{</span> <span class="nx">term</span><span class="o">:</span> <span class="p">{</span> <span class="s1">&#39;owner&#39;</span><span class="o">:</span> <span class="s1">&#39;jones&#39;</span> <span class="p">}</span> <span class="p">}</span>
  <span class="p">]</span>
<span class="p">}).</span><span class="nx">done</span><span class="p">(</span><span class="kd">function</span><span class="p">(</span><span class="nx">out</span><span class="p">)</span> <span class="p">{</span>
  <span class="nx">console</span><span class="p">.</span><span class="nx">log</span><span class="p">(</span><span class="nx">out</span><span class="p">);</span>
<span class="p">});</span></code></pre></div>

<h3 id="python">Python</h3>

<div class="highlight"><pre><code class="language-python" data-lang="python"><span class="kn">import</span> <span class="nn">urllib2</span>
<span class="kn">import</span> <span class="nn">json</span>

<span class="c"># =================================</span>
<span class="c"># Store some data</span>

<span class="n">url</span> <span class="o">=</span> <span class="s">&#39;{endpoint}&#39;</span>
<span class="n">data</span> <span class="o">=</span> <span class="p">{</span>
    <span class="s">&#39;title&#39;</span><span class="p">:</span> <span class="s">&#39;jones&#39;</span><span class="p">,</span>
    <span class="s">&#39;amount&#39;</span><span class="p">:</span> <span class="mf">5.7</span>
    <span class="p">}</span>
<span class="c"># have to send the data as JSON</span>
<span class="n">data</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>

<span class="n">req</span> <span class="o">=</span> <span class="n">urllib2</span><span class="o">.</span><span class="n">Request</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">data</span><span class="p">,</span> <span class="n">headers</span><span class="p">)</span>
<span class="n">out</span> <span class="o">=</span> <span class="n">urllib2</span><span class="o">.</span><span class="n">urlopen</span><span class="p">(</span><span class="n">req</span><span class="p">)</span>
<span class="k">print</span> <span class="n">out</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>

<span class="c"># =================================</span>
<span class="c"># Query the resulting &quot;table&quot;</span>

<span class="n">url</span> <span class="o">=</span> <span class="s">&#39;{endpoint}/_search?q=title:jones&amp;size=5&#39;</span>
<span class="n">req</span> <span class="o">=</span> <span class="n">urllib2</span><span class="o">.</span><span class="n">Request</span><span class="p">(</span><span class="n">url</span><span class="p">)</span>
<span class="n">out</span> <span class="o">=</span> <span class="n">urllib2</span><span class="o">.</span><span class="n">urlopen</span><span class="p">(</span><span class="n">req</span><span class="p">)</span>
<span class="n">data</span> <span class="o">=</span> <span class="n">out</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
<span class="k">print</span> <span class="n">data</span>
<span class="c"># returned data is JSON</span>
<span class="n">data</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
<span class="c"># total number of results</span>
<span class="k">print</span> <span class="n">data</span><span class="p">[</span><span class="s">&#39;hits&#39;</span><span class="p">][</span><span class="s">&#39;total&#39;</span><span class="p">]</span></code></pre></div>

<h2 id="querying">Querying</h2>

<h3 id="basic-queries-using-only-the-query-string">Basic Queries Using Only the Query String</h3>

<p>Basic queries can be done using only query string parameters in the URL. For
example, the following searches for text ‘hello’ in any field in any document
and returns at most 5 results:</p>

<pre><code>{endpoint}/_search?q=hello&amp;size=5
</code></pre>

<p>Basic queries like this have the advantage that they only involve accessing a
URL and thus, for example, can be performed just using any web browser.
However, this method is limited and does not give you access to most of the
more powerful query features.</p>

<p>Basic queries use the <code>q</code> query string parameter which supports the <a href="http://lucene.apache.org/core/old_versioned_docs/versions/3_0_0/queryparsersyntax.html">Lucene
query parser syntax</a> and hence filters on specific fields (e.g.
<code>fieldname:value</code>), wildcards (e.g. <code>abc*</code>) and more.</p>

<p>There are a variety of other options (e.g. size, from etc) that you can also
specify to customize the query and its results. Full details can be found in
the <a href="http://www.elasticsearch.org/guide/reference/api/search/uri-request.html">ElasticSearch URI request docs</a>.</p>

<h3 id="full-query-api">Full Query API</h3>

<p>More powerful and complex queries, including those that involve faceting and
statistical operations, should use the full ElasticSearch query language and API.</p>

<p>In the query language queries are written as a JSON structure and is then sent
to the query endpoint (details of the query langague below). There are two
options for how a query is sent to the search endpoint:</p>

<ol>
  <li>
    <p>Either as the value of a source query parameter e.g.:</p>

    <pre><code> {endpoint}/_search?source={Query-as-JSON}
</code></pre>
  </li>
  <li>
    <p>Or in the request body, e.g.:</p>

    <pre><code> curl -XGET {endpoint}/_search -d 'Query-as-JSON'
</code></pre>

    <p>For example:</p>

    <pre><code> curl -XGET {endpoint}/_search -d '{
     "query" : {
         "term" : { "user": "kimchy" }
     }
 }'
</code></pre>
  </li>
</ol>

<h2 id="query-language">Query Language</h2>

<p>Queries are JSON objects with the following structure (each of the main
sections has more detail below):</p>

<div class="highlight"><pre><code class="language-javascript" data-lang="javascript"><span class="p">{</span>
        <span class="nx">size</span><span class="o">:</span> <span class="err">#</span> <span class="nx">number</span> <span class="nx">of</span> <span class="nx">results</span> <span class="nx">to</span> <span class="k">return</span> <span class="p">(</span><span class="nx">defaults</span> <span class="nx">to</span> <span class="mi">10</span><span class="p">)</span>
        <span class="nx">from</span><span class="o">:</span> <span class="err">#</span> <span class="nx">offset</span> <span class="nx">into</span> <span class="nx">results</span> <span class="p">(</span><span class="nx">defaults</span> <span class="nx">to</span> <span class="mi">0</span><span class="p">)</span>
        <span class="nx">fields</span><span class="o">:</span> <span class="err">#</span> <span class="nx">list</span> <span class="nx">of</span> <span class="nb">document</span> <span class="nx">fields</span> <span class="nx">that</span> <span class="nx">should</span> <span class="nx">be</span> <span class="nx">returned</span> <span class="o">-</span> <span class="nx">http</span><span class="o">:</span><span class="c1">//elasticsearch.org/guide/reference/api/search/fields.html</span>
        <span class="nx">sort</span><span class="o">:</span> <span class="err">#</span> <span class="nx">define</span> <span class="nx">sort</span> <span class="nx">order</span> <span class="o">-</span> <span class="nx">see</span> <span class="nx">http</span><span class="o">:</span><span class="c1">//elasticsearch.org/guide/reference/api/search/sort.html</span>

        <span class="nx">query</span><span class="o">:</span> <span class="p">{</span>
            <span class="err">#</span> <span class="s2">&quot;query&quot;</span> <span class="nx">object</span> <span class="nx">following</span> <span class="nx">the</span> <span class="nx">Query</span> <span class="nx">DSL</span><span class="o">:</span> <span class="nx">http</span><span class="o">:</span><span class="c1">//elasticsearch.org/guide/reference/query-dsl/</span>
            <span class="err">#</span> <span class="nx">details</span> <span class="nx">below</span>
        <span class="p">},</span>

        <span class="nx">facets</span><span class="o">:</span> <span class="p">{</span>
            <span class="err">#</span> <span class="nx">facets</span> <span class="nx">specifications</span>
            <span class="err">#</span> <span class="nx">Facets</span> <span class="nx">provide</span> <span class="nx">summary</span> <span class="nx">information</span> <span class="nx">about</span> <span class="nx">a</span> <span class="nx">particular</span> <span class="nx">field</span> <span class="nx">or</span> <span class="nx">fields</span> <span class="k">in</span> <span class="nx">the</span> <span class="nx">data</span>
        <span class="p">}</span>

        <span class="err">#</span> <span class="nx">special</span> <span class="k">case</span> <span class="k">for</span> <span class="nx">situations</span> <span class="nx">where</span> <span class="nx">you</span> <span class="nx">want</span> <span class="nx">to</span> <span class="nx">apply</span> <span class="nx">filter</span><span class="o">/</span><span class="nx">query</span> <span class="nx">to</span> <span class="nx">results</span> <span class="nx">but</span> <span class="o">*</span><span class="nx">not</span><span class="o">*</span> <span class="nx">to</span> <span class="nx">facets</span>
        <span class="nx">filter</span><span class="o">:</span> <span class="p">{</span>
            <span class="err">#</span> <span class="nx">filter</span> <span class="nx">objects</span>
            <span class="err">#</span> <span class="nx">a</span> <span class="nx">filter</span> <span class="nx">is</span> <span class="nx">a</span> <span class="nx">simple</span> <span class="s2">&quot;filter&quot;</span> <span class="p">(</span><span class="nx">query</span><span class="p">)</span> <span class="nx">on</span> <span class="nx">a</span> <span class="nx">specific</span> <span class="nx">field</span><span class="p">.</span>
            <span class="err">#</span> <span class="nx">Simple</span> <span class="nx">means</span> <span class="nx">e</span><span class="p">.</span><span class="nx">g</span><span class="p">.</span> <span class="nx">checking</span> <span class="nx">against</span> <span class="nx">a</span> <span class="nx">specific</span> <span class="nx">value</span> <span class="nx">or</span> <span class="nx">range</span> <span class="nx">of</span> <span class="nx">values</span>
        <span class="p">},</span>
    <span class="p">}</span></code></pre></div>

<p>Query results look like:</p>

<pre><code>{
    # some info about the query (which shards it used, how long it took etc)
    ...
    # the results
    hits: {
        total: # total number of matching documents
        hits: [
            # list of "hits" returned
            {
                _id: # id of document
                score: # the search index score
                _source: {
                    # document 'source' (i.e. the original JSON document you sent to the index
                }
            }
        ]
    }
    # facets if these were requested
    facets: {
        ...
    }
}
</code></pre>

<h3 id="query-dsl-overview">Query DSL: Overview</h3>

<p>Query objects are built up of sub-components. These sub-components are either
basic or compound. Compound sub-components may contains other sub-components
while basic may not. Example:</p>

<pre><code>{
    "query": {
        # compound component
        "bool": {
            # compound component
            "must": {
                # basic component
                "term": {
                    "user": "jones"
                }
            }
            # compound component
            "must_not": {
                # basic component
                "range" : {
                    "age" : {
                        "from" : 10,
                        "to" : 20
                    }
                } 
            }
        }
    }
}
</code></pre>

<p>In addition, and somewhat confusingly, ElasticSearch distinguishes between
sub-components that are “queries” and those that are “filters”. Filters, are
really special kind of queries that are: mostly basic (though boolean
compounding is alllowed); limited to one field or operation and which, as such,
are especially performant.</p>

<p>Examples, of filters are (full list on RHS at the bottom of the <a href="http://elasticsearch.org/guide/reference/query-dsl/">query-dsl</a> page):</p>

<ul>
  <li>term: filter on a value for a field</li>
  <li>range: filter for a field having a range of values (&gt;=, &lt;= etc)</li>
  <li>geo_bbox: geo bounding box</li>
  <li>geo_distance: geo distance</li>
</ul>

<p>Rather than attempting to set out all the constraints and options of the
query-dsl we now offer a variety of examples.</p>

<h3 id="examples">Examples</h3>

<h4 id="match-all--find-everything">Match all / Find Everything</h4>

<pre><code>{
    "query": {
        "match_all": {}
    }
}
</code></pre>

<h4 id="classic-search-box-style-full-text-query">Classic Search-Box Style Full-Text Query</h4>

<p>This will perform a full-text style query across all fields. The query string
supports the <a href="http://lucene.apache.org/core/old_versioned_docs/versions/3_0_0/queryparsersyntax.html">Lucene query parser syntax</a> and hence filters on specific fields
(e.g. <code>fieldname:value</code>), wildcards (e.g. <code>abc*</code>) as well as a variety of
options. For full details see the <a href="http://elasticsearch.org/guide/reference/query-dsl/query-string-query.html">query-string</a> documentation.</p>

<pre><code>{
    "query": {
        "query_string": {
            "query": {query string}
        }
    }
}
</code></pre>

<h4 id="filter-on-one-field">Filter on One Field</h4>

<pre><code>{
    "query": {
        "term": {
            {field-name}: {value}
        }
    }
}
</code></pre>

<p>High performance equivalent using filters:</p>

<pre><code>{
    "query": {
        "constant_score": {
            "filter": {
                "term": {
                    # note that value should be *lower-cased*
                    {field-name}: {value}
                }
            }
        }
}
</code></pre>

<h4 id="find-all-documents-with-value-in-a-range">Find all documents with value in a range</h4>

<p>This can be used both for text ranges (e.g. A to Z), numeric ranges (10-20) and
for dates (ElasticSearch will converts dates to ISO 8601 format so you can
search as 1900-01-01 to 1920-02-03).</p>

<pre><code>{
    "query": {
        "constant_score": {
            "filter": {
                "range": {
                    {field-name}: {
                        "from": {lower-value}
                        "to": {upper-value}
                    }
                }
            }
        }
    }
}
</code></pre>

<p>For more details see <a href="http://elasticsearch.org/guide/reference/query-dsl/range-filter.html">range filters</a>.</p>

<h4 id="full-text-query-plus-filter-on-a-field">Full-Text Query plus Filter on a Field</h4>

<pre><code>{
    "query": {
        "query_string": {
            "query": {query string}
        },
        "term": {
            {field}: {value}
        }
    }
}
</code></pre>

<h4 id="filter-on-two-fields">Filter on two fields</h4>

<p>Note that you cannot, unfortunately, have a simple <code>and</code> query by adding two
filters inside the query element. Instead you need an ‘and’ clause in a filter
(which in turn requires nesting in ‘filtered’). You could also achieve the same
result here using a <a href="http://elasticsearch.org/guide/reference/query-dsl/bool-query.html">bool query</a>.</p>

<pre><code>{
    "query": {
        "filtered": {
            "query": {
                "match_all": {}
            },
            "filter": {
                "and": [
                    {
                        "range" : {
                            "b" : { 
                                "from" : 4, 
                                "to" : "8"
                            }
                        },
                    },
                    {
                        "term": {
                            "a": "john"
                        }
                    }
                ]
            }
        }
    }
}
</code></pre>

<h4 id="geospatial-query-to-find-results-near-a-given-point">Geospatial Query to find results near a given point</h4>

<p>This uses the <a href="http://www.elasticsearch.org/guide/reference/query-dsl/geo-distance-filter.html">Geo Distance filter</a>. It requires that indexed documents have
a field of <a href="http://www.elasticsearch.org/guide/reference/mapping/geo-point-type.html">geo point type</a>.</p>

<p>Source data (a point in San Francisco!):</p>

<pre><code># This should be in lat,lon order
{
  ...
  "Location": "37.7809035011582, -122.412119695795"
}
</code></pre>

<p>There are alternative formats to provide lon/lat locations e.g. (see
ElasticSearch documentation for more):</p>

<pre><code># Note this must have lon,lat order (opposite of previous example!)
{
  "Location":[-122.414753390488, 37.7762147914147]
}

# or ...
{
  "Location": {
    "lon": -122.414753390488,
    "lat": 37.7762147914147
  }
}
</code></pre>

<p>We also need a mapping to specify that Location field is of type geo_point as this will not usually get guessed from the data (see below for more on mappings):</p>

<pre><code>"properties": {
    "Location": {
        "type": "geo_point"
     }
     ...
}
</code></pre>

<p>Now the actual query:</p>

<pre><code>{
    "query": {
        "filtered" : {
            "query" : {
                "match_all" : {}
            },
            "filter" : {
                "geo_distance" : {
                    "distance" : "20km",
                    "Location" : {
                        "lat" : 37.776,
                        "lon" : -122.41
                    }
                }
            }
        }
    }
}    
</code></pre>

<p>Note that you can specify the query using specific lat, lon attributes even
though original data did not have this structure (you can also use a query
similar to the original structure if you wish - see <a href="http://www.elasticsearch.org/guide/reference/query-dsl/geo-distance-filter.html">Geo distance filter</a> for
more information).</p>

<h3 id="facets">Facets</h3>

<p>Facets provide a way to get summary information about then data in an
elasticsearch table, for example counts of distinct values.</p>

<p>ElasticSearch (and hence the Data API) provides <a href="http://www.elasticsearch.org/guide/reference/api/search/facets/">rich faceting
capabilities</a>. The <a href="http://www.elasticsearch.org/guide/reference/api/search/facets/">ES facet docs</a> go a great job of listing of the various
kinds of facets available and their structure so I won’t repeat it all here.
Here is a list of some of the most important (full list on the facets page):</p>

<ul>
  <li><a href="http://www.elasticsearch.org/guide/reference/api/search/facets/terms-facet.html">Terms</a> - counts by distinct terms (values) in a field</li>
  <li><a href="http://www.elasticsearch.org/guide/reference/api/search/facets/range-facet.html">Range</a> - counts for a given set of ranges in a field</li>
  <li><a href="http://www.elasticsearch.org/guide/reference/api/search/facets/histogram-facet.html">Histogram</a> and <a href="http://www.elasticsearch.org/guide/reference/api/search/facets/date-histogram-facet.html">Date Histogram</a> - counts by constant interval ranges</li>
  <li><a href="http://www.elasticsearch.org/guide/reference/api/search/facets/statistical-facet.html">Statistical</a> - statistical summary of a field (mean, sum etc)</li>
  <li><a href="http://www.elasticsearch.org/guide/reference/api/search/facets/terms-stats-facet.html">Terms Stats</a> - statistical summary on one field (stats field) for distinct
terms in another field. For example, spending stats per department or per
region.</li>
  <li><a href="http://www.elasticsearch.org/guide/reference/api/search/facets/geo-distance-facet.html">Geo Distance</a>: counts by distance ranges from a given point</li>
</ul>

<p>Note that you can apply multiple facets per query.</p>

<h2 id="appendix">Appendix</h2>

<h3 id="adding-updating-and-deleting-data">Adding, Updating and Deleting Data</h3>

<p>ElasticSeach, and hence the Data API, have a standard RESTful API. Thus:</p>

<pre><code>POST      {endpoint}         : INSERT
PUT/POST  {endpoint}/  : UPDATE (or INSERT)
DELETE    {endpoint}/  : DELETE
</code></pre>

<p>For more on INSERT and UPDATE see the <a href="http://elasticsearch.org/guide/reference/api/index_.html">Index API</a> documentation.</p>

<p>There is also support bulk insert and updates via the <a href="http://elasticsearch.org/guide/reference/api/bulk.html">Bulk API</a>.</p>

<h3 id="schema-mapping">Schema Mapping</h3>

<p>As the ElasticSearch documentation states:</p>

<blockquote>
  <p>Mapping is the process of defining how a document should be mapped to the
Search Engine, including its searchable characteristics such as which fields
are searchable and if/how they are tokenized. In ElasticSearch, an index may
store documents of different “mapping types”. ElasticSearch allows one to
associate multiple mapping definitions for each mapping type.</p>
</blockquote>

<blockquote>
  <p>Explicit mapping is defined on an index/type level. By default, there isn’t a
need to define an explicit mapping, since one is automatically created and
registered when a new type or new field is introduced (with no performance
overhead) and have sensible defaults. Only when the defaults need to be
overridden must a mapping definition be provided.</p>
</blockquote>

<p>Relevant docs: <a href="http://elasticsearch.org/guide/reference/mapping/">http://elasticsearch.org/guide/reference/mapping/</a>.</p>

<h3 id="jsonp-support">JSONP support</h3>

<p>JSONP support is available on any request via a simple callback query string parameter:</p>

<pre><code>?callback=my_callback_name
</code></pre>



