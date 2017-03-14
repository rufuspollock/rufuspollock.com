---
title: >-
  Basic data cleaning with Data Explorer
slug: basic-data-cleaning-with-data-explorer
date: 2013-06-28T07:00:00
themes: []
tags: []
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1314
---

<p><a href="http://explorer.okfnlabs.org/">Data Explorer</a> is a client-side web application for
data processing and visualization. With Data Explorer, you can import data,
transform it with JavaScript code, and visualize it on a graph or a map – all
fully within the browser and with your data and code nicely persisted to
<a href="https://gist.github.com/">gists</a>.</p>

<p>This tutorial will get you started using Data Explorer by walking you through
the cleaning of a messy data set. It introduces some of the basic concepts of
the <a href="http://okfnlabs.org/recline/">Recline</a> library which provides Data Explorer’s model of data
and highlights why it’s nice to be able to use JavaScript to wrangle data.</p>

<h2 id="getting-started">Getting started</h2>

<p>For this tutorial, we’re going to use a set of <a href="http://static.london.gov.uk/gla/expenditure/docs/2012-13-P12-250.csv">Greater London Authority (GLA) financial data</a>,
a report of payments made by the GLA for property worth more than £250 over a one-month
period in 2013. Conveniently for our purposes, this dataset is a little buggy.</p>

<p>To get started, go to the <a href="http://explorer.okfnlabs.org/">Data Explorer</a> website, and click <strong>Get
started with your own data</strong> to proceed to the <em>Import</em> page. From there, you will be
able to load the data in a number of ways: uploading a local file, pasting in a URL, or
pasting the data itself into a text box. Choose your preferred method and hit the appropriate
<strong>Load</strong> button, which will take you to the <em>Preview &amp; Save</em> page.</p>

<p>The <em>Preview</em> shows what the data will look like as a grid. Already some
fiddling is necessary to get things started. The row containing the names of fields is six rows
down, and the fields are all nameless – except for one with an erroneous name! To fix this,
change the <strong>Skip initial rows</strong> value to 6.</p>

<p>You can also see that there is a blank column, but you can’t do anything about this yet.
Just choose a name for the dataset, click <strong>Save</strong>, and move on to actually working with the data.</p>

<h2 id="the-grid-and-the-graph">The grid and the graph</h2>

<p>Once the data has been loaded and named, you are taken to the Data Explorer proper. Your
first view of the data will be the <strong>Grid</strong>, a tabular display identical to what was already
shown in the <em>Preview</em> screen.</p>

<p><img src="http://i.imgur.com/B48sGc9.png" alt="The initial grid" /></p>

<p>Data visualizations are constructed with the <strong>Graph</strong>. Let’s try to make a graph
of the data. Click <strong>Graph</strong> to go to the graph screen, which will ask you to choose
which of the data’s fields to bind to the two axes, Axis 1 (= x) and Axis 2 (= y). First
change the Graph Type to <strong>Points</strong>. Then, for Group Column, choose “Clearing Date”, and
for Series A, choose “Amount”. You should get a graph that looks like this.</p>

<p><img src="http://i.imgur.com/NDPFkLN.png" alt="First graph" /></p>

<p>This graph is useless. There are no points with an Amount higher than about £990.
A quick look at the grid will tell you that in fact many points have Amounts
running into the millions of pounds. Also note that the x axis is completely unlabeled. If you scan
your cursor over the data points, which displays their underlying value, you’ll see that
their horizontal arrangement is meaningless.</p>

<p>The problem is that the dataset is formatted badly. All of the values in the Amounts field
that run higher than £999.99 include a comma, which prevents them from being parsed as
numbers. The dates, too, are not being treated as dates but just as ordinary strings,
making it impossible to put them on a scale.</p>

<p>To fix these problems, we’ll write some code. Roll up your sleeves and get ready.</p>

<h2 id="basics-of-de-coding">Basics of DE coding</h2>

<p>To pull up Data Explorer’s tool for editing and running JavaScript code, click <strong>Code</strong>
at the top right of the page. This will cause the <strong>JavaScript console</strong> to drop down.
This console consists of a panel for editing code and, beneath it, an area where
messages are printed.</p>

<p>A bit of code is included in the edit panel by default:</p>

<pre><code>loadDataset("current", function (error, dataset) {
  // error will be null unless there is an error
  // dataset is a Recline memory store (http://reclinejs.com//docs/src/backend.memory.html).
  console.log(dataset);
});
</code></pre>

<p>This code loads up the current dataset by calling the function <code>loadDataset</code>
on the string <code>"current"</code> (the name of the current dataset) and an anonymous
callback function which binds a representation of the dataset to the name <code>dataset</code>.
The callback function, as defined, prints the dataset to the console’s
message area by calling <code>console.log</code> on <code>dataset</code>.
Watch this code work by clicking <strong>Run the Code</strong>.</p>

<p>The console output might surprise you. The dataset is represented as a JavaScript
object with attributes <code>"records"</code> and <code>"fields"</code>, the first of which is an array
of objects with attributes for each of the top-level object’s <code>"fields"</code>. This is
an instance of the <a href="">Recline memory store</a>. A dataset is a collection
of records, and a record is just an object.</p>

<p>If you understand that, you’re ready to clean the dataset.</p>

<h2 id="cleaning-with-javascript">Cleaning with JavaScript</h2>

<p>The full gamut of JavaScript tools and tricks are available to you when you
clean data in Data Explorer. Besides handy core JavaScript functionality like
regular expressions, Data Explorer makes the <a href="http://underscorejs.org/">Underscore.js</a>
suite of functional programming utilities available for data cleaning.</p>

<p>To clean a dataset, write code inside a <code>loadDataset</code> call that modifies the dataset
in the appropriate way, and finish by calling <code>saveDataset</code> on the modified dataset.
All code presented in this section is to be placed inside the curly brackets of the <code>loadDataset</code>
callback function.</p>

<p>Let’s start by getting rid of that annoying blank column we noticed earlier. To do this,
we have to delete <code>_noname_</code> from the dataset’s fields. We must also drop the <code>_noname_</code>
attribute from every record in the dataset.</p>

<p>To get rid of the bad field, set the dataset’s field attribute to be the old value
of the attribute minus the field named <code>"_noname_"</code>.</p>

<pre><code>dataset.fields = 
  _.reject(dataset.fields,
           function (f) {
             return f.id === "_noname_";
           }) ;
</code></pre>

<p>Erasing the bad field from each record can be done with an application of <code>each</code>,
which calls a function with side effects on each item in a collection.</p>

<pre><code>_.each(dataset.records,
       function (r) {
         delete r._noname_ ;
       }) ;
</code></pre>

<p>Now let’s look at the next problem: the unparsed Amounts with commas. To fix these,
we need to eliminate the commas and then parse the resulting string as a float.
Since we’re already iterating over every record in the dataset, we can add to the
anonymous function in the <code>each</code> call:</p>

<pre><code>if (typeof r.Amount === "string") {
  r.Amount = parseFloat(r.Amount.replace(/,/g, "")) ;
}
</code></pre>

<p>Finally, we can fix the dates. There are two problems with these. The first is that
the Recline dataset object needs to know that the type of their field is <em>date</em>.
The second is that the dates haven’t been parsed. To fix the first problem, add
to the <code>loadDataset</code> callback function:</p>

<pre><code>_.find(dataset.fields,
       function (f) {
         return f.id === "Clearing Date" ;
       })
 .type = "date" ;
</code></pre>

<p>Next, add another bit to the anonymous function in <code>each</code>:</p>

<pre><code>if (typeof r["Clearing Date"] === "string") {
  r["Clearing Date"] = new Date(r["Clearing Date"]) ;
}
</code></pre>

<p>That’s it! All that remains is to save the modified dataset. At the bottom of
the <code>loadDataset</code> callback function, add a line to save the data:</p>

<pre><code>saveDataset(dataset) ;
</code></pre>

<p>Click <strong>Run the Code</strong> and watch the data transform before your very eyes.
The new graph view of the data is now meaningful, correct, and fully consistent
with your expectations. Awesome!</p>

<p><img src="http://i.imgur.com/Bl1cxL8.png" alt="Fixed graph" /></p>

<p>You can also have another look at the grid, which will show you exactly what
has changed in your data.</p>

<p><img src="http://i.imgur.com/WfQxGdV.png" alt="Final grid" /></p>

<p>If you have logged in to GitHub, you will be able to save the result of your
work. To share the work, simply copy the URL of your project. An example of
a project constructed according to the instructions above can be found <a href="http://explorer.okfnlabs.org/#nmashton/e4f4ab6a21471e1aa1b8/view/graph">here</a>.</p>

<h2 id="conclusion">Conclusion</h2>

<p>With Data Explorer, the full power of arbitrary JavaScript code (enhanced
with Underscore functionality) can be brought to bear on tough data cleaning
problems. The cleaning script’s effects are immediately visible in the grid
and graph views of the data, which enables an easy, interactive style of data
cleaning. And it is all done without a backend, in memory and in the browser.</p>



