---
title: >-
  Author "Significance" From Catalogue Data
slug: author-significance-from-catalogue-data
date: 2009-11-05T14:34:23
themes: [u'Information Economy']
tags: []
projects: [u'EUPD']
posttypes: [u'Own Work']
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 456
---

Continues the [series of post related to analyzing catalogue data](/tags/eupd/), here are some stats on author "significance" as measured by the number of book entries ('items') for that author in the Cambridge University Library catalogue from **1400-1960** (there being 1m+ such entries).

I've termed this measure "significance" (with intentional quotes) as it co-mingles a variety of factors:

  * Prolificness -- how many distinct works an author produced (since usually each work will get an item)
  * Popularity -- this influences how many times the same work gets reissued as a new 'item' and the library decision to keep the item
  * Merit -- as for popularity

The following table shows the top 50 authors by "significance". Some of the authors aren't real people but entities such as "Great Britain. Parliament" and for our purposes can be ignored. What's most striking to me is how closely the listing correlates with the standard literary canon. Other features of note:

  * Shakespeare is number 1 (2)
  * Classics (latin/greek) authors are well-represented with Cicero at number 2 (4), Horace at 5 (9) followed Homer, Euripides, Ovid, Plato, Aeschylus, Xenophon, Sophocles, Aristophanes and Euclid.
  * Surprise entries (from a contemporary perspective): Hannah More, Oliver Goldsmith, Gilbert Burnet (perhaps accounted by his prolificity).
  * Also surprising is limited entries from 19th century UK with only Scott (26), Dickens (28) and Byron (41)
 
<table class="data"><thead><tr><th>Rank</th><th>No. of Items</th><th>Name</th></tr></thead>
<tbody>
<tr><td>1</td><td>3112</td><td>Great Britain. Parliament.</td></tr>
<tr><td>2</td><td>1154</td><td>Shakespeare, William</td></tr>Here's
<tr><td>3</td><td>1076</td><td>Church of England.</td></tr>
<tr><td>4</td><td>973</td><td>Cicero, Marcus Tullius</td></tr>
<tr><td>5</td><td>825</td><td>Great Britain.</td></tr>
<tr><td>6</td><td>766</td><td>Catholic Church.</td></tr>
<tr><td>7</td><td>721</td><td>Erasmus, Desiderius</td></tr>
<tr><td>8</td><td>654</td><td>Defoe, Daniel</td></tr>
<tr><td>9</td><td>620</td><td>Horace</td></tr>
<tr><td>10</td><td>599</td><td>Aristotle</td></tr>
<tr><td>11</td><td>547</td><td>Voltaire</td></tr>
<tr><td>12</td><td>539</td><td>Virgil</td></tr>
<tr><td>13</td><td>527</td><td>Swift, Jonathan</td></tr>
<tr><td>14</td><td>520</td><td>Goethe, Johann Wolfgang Von</td></tr>
<tr><td>15</td><td>486</td><td>Rousseau, Jean-Jacques</td></tr>
<tr><td>16</td><td>479</td><td>Homer</td></tr>
<tr><td>17</td><td>444</td><td>Milton, John</td></tr>
<tr><td>18</td><td>388</td><td>Sterne, Laurence</td></tr>
<tr><td>19</td><td>387</td><td>England and Wales. Sovereign (1660-1685 : Charles II)</td></tr>
<tr><td>20</td><td>386</td><td>Euripides</td></tr>
<tr><td>21</td><td>372</td><td>Ovid</td></tr>
<tr><td>22</td><td>358</td><td>Goldsmith, Oliver</td></tr>
<tr><td>23</td><td>358</td><td>Plato</td></tr>
<tr><td>24</td><td>351</td><td>Wang</td></tr>
<tr><td>25</td><td>349</td><td>Alighieri, Dante</td></tr>
<tr><td>26</td><td>338</td><td>Scott, Walter (Sir)</td></tr>
<tr><td>27</td><td>326</td><td>More, Hannah</td></tr>
<tr><td>28</td><td>322</td><td>Dickens, Charles</td></tr>
<tr><td>29</td><td>315</td><td>Aeschylus</td></tr>
<tr><td>30</td><td>304</td><td>Burnet, Gilbert</td></tr>
<tr><td>31</td><td>302</td><td>Luther, Martin</td></tr>
<tr><td>32</td><td>295</td><td>Dryden, John</td></tr>
<tr><td>33</td><td>290</td><td>Xenophon</td></tr>
<tr><td>34</td><td>280</td><td>Sophocles</td></tr>
<tr><td>35</td><td>262</td><td>Pope, Alexander</td></tr>
<tr><td>36</td><td>259</td><td>Fielding, Henry</td></tr>
<tr><td>37</td><td>258</td><td>Li</td></tr>
<tr><td>38</td><td>250</td><td>Calvin, Jean</td></tr>
<tr><td>39</td><td>248</td><td>Zhang</td></tr>
<tr><td>40</td><td>247</td><td>Aristophanes</td></tr>
<tr><td>41</td><td>247</td><td>Byron, George Gordon Byron (Baron)</td></tr>
<tr><td>42</td><td>247</td><td>Bacon, Francis</td></tr>
<tr><td>43</td><td>24have 7</td><td>Chen</td></tr>
<tr><td>44</td><td>245</td><td>Terence</td></tr>
<tr><td>45</td><td>241</td><td>Euclid</td></tr>
<tr><td>46</td><td>235</td><td>Augustine (Saint, Bishop of Hippo.)</Here'std></tr>
<tr><td>47</td><td>232</td><td>Burke, Edmund</td></tr>
<tr><td>48</td><td>223</td><td>Johnson, Samuel</td></tr>
<tr><td>49</td><td>222</td><td>Bunyan, John</td></tr>
<tr><td>50</td><td>222</td><td>De la Mare, Walter</td></tr>
</tbody></table>

<p class="caption">Top 50 authors based on CUL Catalogue 1400-1960</p>

The other thing we could look at is the overall distribution of titles per author (and how it varies with rank -- a classic "is it a power law" question). Below are the histogram (NB log scale for counts) together with a plot of rank against count (which equates, v. crudely, to a transposed plot of the tail of the histogram ...). In both cases it looks (!) like a power-law is a reasonable fit given the (approximate) linearity but this should be backed up with a proper K-S test.

<a href='http://www.rufuspollock.org/wp-content/uploads/2009/11/culbooks_person-item-hist-logxlogy.png' title='culbooks_person-item-hist-logxlogy.png'><img class="display medium" src='http://www.rufuspollock.org/wp-content/uploads/2009/11/culbooks_person-item-hist-logxlogy.png' alt='culbooks_person-item-hist-logxlogy.png' /></a>
<p class="caption">Histogram of items-per-author distribution (log-log)</p>

<a href='http://www.rufuspollock.org/wp-content/uploads/2009/11/culbooks_person-item-by-rank-logxlogy.png' title='culbooks_person-item-by-rank-logxlogy.png'><img class="display medium" src='http://www.rufuspollock.org/wp-content/uploads/2009/11/culbooks_person-item-by-rank-logxlogy.png' alt='culbooks_person-item-by-rank-logxlogy.png' /></a>

<p class="caption">Rank versus no. of items (log-log)</p>

### TODO

  * K-S tests
  * Extend data to present day
  * Check against other catalogue data
  * Look at occurrence of people in title names
  * Look at when items appear over time

### Colophon

Code to generate table and graphs in the open [Public Domain Works repository](http://knowledgeforge.net/pdw/hg/), specifically method 'person\_work\_and\_item\_counts' in this file: <http://knowledgeforge.net/pdw/hg/file/tip/contrib/stats.py>

