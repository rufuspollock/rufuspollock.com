---
title: >-
  The SEC EDGAR Database
slug: the-sec-edgar-database
date: 2014-03-04T00:00:00
themes: []
tags: []
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1299
---

<p>This post looks at the Securities and Exchange Commission (SEC) EDGAR database.
EDGAR is a rich source of data containing regulatory filings from
publicly-traded US corporations including their annual and quarterly reports:</p>

<blockquote>
  <p>All companies, foreign and domestic, are required to file registration
statements, periodic reports, and other forms electronically through EDGAR.
Anyone can access and download this information for free. [from the <a href="http://www.sec.gov/edgar.shtml">SEC
website</a>]</p>
</blockquote>

<p>This post introduces the basic structure of the database, and how to get access
to filings via ftp. Subsequent posts will look at how to use the structured
information in the form of XBRL files.</p>

<div class="alert alert-success">
<strong>Note</strong>: an extended version of the notes here plus additional data and scripts
can be found in this <a href="https://github.com/datasets/edgar">SEC EDGAR Data
Package on Github</a>.
</div>

<h2 id="human-interface">Human Interface</h2>

<p>See <a href="http://www.sec.gov/edgar/searchedgar/companysearch.html">http://www.sec.gov/edgar/searchedgar/companysearch.html</a></p>

<p><img src="http://webshot.okfnlabs.org/api/generate?url=http%3A%2F%2Fwww.sec.gov%2Fedgar%2Fsearchedgar%2Fcompanysearch.html" /></p>

<h2 id="bulk-data">Bulk Data</h2>

<p>EDGAR provides bulk access via FTP: <a href="ftp://ftp.sec.gov/">ftp://ftp.sec.gov/</a> - <a href="https://www.sec.gov/edgar/searchedgar/ftpusers.htm">official
documentation</a>. We summarize here the main points.</p>

<p>Each company in EDGAR gets an identifier known as the CIK which is a 10 digit
number. You can find the CIK by searching EDGAR using a name of stock market
ticker.</p>

<p>For example, <a href="http://www.sec.gov/cgi-bin/browse-edgar?CIK=ibm&amp;action=getcompany">searching for IBM by ticker</a> shows us that
the the CIK is <code>0000051143</code>.</p>

<p>Note that leading zeroes are often omitted (e.g. in the ftp access) so this
would become <code>51143</code>.</p>

<p><img src="http://webshot.okfnlabs.org/api/generate?url=http%3A%2F%2Fwww.sec.gov%2Fcgi-bin%2Fbrowse-edgar%3FCIK%3Dibm%26action%3Dgetcompany&amp;width=1024&amp;height=768" /></p>

<p>Next each submission receives an ‘Accession Number’ (acc-no). For example,
IBM’s quarterly financial filing (form 10-Q) in October 2013 had accession
number: <code>0000051143-13-000007</code>.</p>

<h3 id="ftp-file-paths">FTP File Paths</h3>

<p>Given a company with CIK (company ID) XXX (omitting leading zeroes) and
document accession number YYY (acc-no on search results) the path would be:</p>

<p>File paths are of the form:</p>

<pre><code>/edgar/data/XXX/YYY.txt
</code></pre>

<p>For example, for the IBM data above it would be:</p>

<p><a href="ftp://ftp.sec.gov/edgar/data/51143/0000051143-13-000007.txt">ftp://ftp.sec.gov/edgar/data/51143/0000051143-13-000007.txt</a></p>

<p>Note, if you are looking for a nice HTML version you can find it at in the
Archives section with a similar URL (just add -index.html):</p>

<p><a href="http://www.sec.gov/Archives/edgar/data/51143/000005114313000007/0000051143-13-000007-index.htm">http://www.sec.gov/Archives/edgar/data/51143/000005114313000007/0000051143-13-000007-index.htm</a></p>

<h3 id="indices">Indices</h3>

<p>If you want to get a list of all filings you’ll want to grab an Index. As the help page explains:</p>

<blockquote>
  <p>The EDGAR indices are a helpful resource for FTP retrieval, listing the
following information for each filing: Company Name, Form Type, CIK, Date
Filed, and File Name (including folder path).</p>

  <p>Four types of indexes are available:</p>

  <ul>
    <li>company — sorted by company name</li>
    <li>form — sorted by form type</li>
    <li>master — sorted by CIK number</li>
    <li>XBRL — list of submissions containing XBRL financial files, sorted by CIK
number; these include Voluntary Filer Program submissions</li>
  </ul>
</blockquote>

<p>URLs are like:</p>

<p><a href="ftp://ftp.sec.gov/edgar/full-index/2008/QTR4/master.gz">ftp://ftp.sec.gov/edgar/full-index/2008/QTR4/master.gz</a></p>

<p>That is, they have the following general form:</p>

<pre><code>ftp://ftp.sec.gov/edgar/full-index/{YYYY}/QTR{1-4}/{index-name}.[gz|zip]
</code></pre>

<p>So for XBRL in the 3rd quarter of 2010 we’d do:</p>

<p><a href="ftp://ftp.sec.gov/edgar/full-index/2010/QTR3/xbrl.gz">ftp://ftp.sec.gov/edgar/full-index/2010/QTR3/xbrl.gz</a></p>

<h3 id="cik-lists-and-lookup">CIK lists and lookup</h3>

<p>There’s a full list of all companies along with their CIK code here: <a href="http://www.sec.gov/edgar/NYU/cik.coleft.c">http://www.sec.gov/edgar/NYU/cik.coleft.c</a></p>

<p>If you want to look up a CIK or company by its ticker you can do the following query against the normal search system:</p>

<p><a href="http://www.sec.gov/cgi-bin/browse-edgar?CIK=ibm&amp;Find=Search&amp;owner=exclude&amp;action=getcompany&amp;output=atom">http://www.sec.gov/cgi-bin/browse-edgar?CIK=ibm&amp;Find=Search&amp;owner=exclude&amp;action=getcompany&amp;output=atom</a></p>

<p>Then parse the atom to grab the CIK. (If you prefer HTML output just omit output=atom).</p>

<p>There is also a full-text company name to CIK lookup here:</p>

<p><a href="http://www.sec.gov/edgar/searchedgar/cik.htmL">http://www.sec.gov/edgar/searchedgar/cik.htmL</a></p>

<p>(Note this does a POST to a ‘text’ API at <a href="http://www.sec.gov/cgi-bin/cik.pl.c">http://www.sec.gov/cgi-bin/cik.pl.c</a>)</p>



