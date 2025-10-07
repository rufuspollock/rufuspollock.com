---
title: >-
  Open Economics: History via Wheat Prices
slug: open-economics-history-via-wheat-prices
date: 2008-09-15T11:11:35
themes: []
tags: ['History']
projects: ['Open Knowledge']
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 298
---

One of the active [Open Knowledge Foundation](http://www.okfn.org/) projects is [Open Economics][oecon]. A substantial part of that effort ends up being data acquisition and 'cleaning': getting hold of economic data, parsing it into (computer) usable form and adding it to the [Store](http://www.openeconomics.net/store/). (Wouldn't it be nice if that data was already nicely [packaged up](http://www.ckan.net) or at least [in a decent raw form][raw] ...).

Once this job is done, the data is there in a nice clean state for others to use -- plus we can draw some nice graphs (as we will see below). As an illustration of this process, we'll look at one particular dataset acquired earlier this year when, motivated by the large increases in commodity prices and the concerns expressed regarding their impact, I decided to see what data I could dig up on food prices (starting with Wheat).

[raw]:http://blog.okfn.org/2007/11/07/give-us-the-data-raw-and-give-it-to-us-now/
[oecon]:http://www.openeconomics.net/

As usual, it was US government material that was most easily available (in a decent format) and I decided to start off with historical information on wheat to be found in the [Wheat Yearbook](http://www.ers.usda.gov/Data/Wheat/WheatYearbook.aspx), in particular the contents of:

<http://www.ers.usda.gov/data/wheat/yearbook/WheatYearbookTables-Recent.xls>

While the data was available (and [open](http://opendefinition.org/) -- since US Govt provided) it was in a format that was not immediately computer usable (lots of blank lines etc). Thus, the first step was to parse this into standard csv file format (see [script here](http://knowledgeforge.net/econ/svn/trunk/data/wheat-us/data.py)) and then upload this to Open Economics. The result:

<http://www.openeconomics.net/store/517d7c4e-3cb7-4e8f-aaa1-745dd665ad1f>

Not only do we now have nice clean data but, thanks to [plotkit](http://www.liquidx.net/plotkit/), [Open Economics][oecon] has javascript graphing so without any more effort we can automatically have graphs of the resulting material. Not only does this allow us to answer our original question (see Fig 4) but **these graphs also tell a fascinating historical story:**

### US Wheat: 1866 - 2007

NB: if the figures are too small click through for the full-size versions on Open Economics (the dates at the bottom run from 1866 to 2007)

#### Figure 1: Output (Millions of Bushels)

<a href="http://www.openeconomics.net/plot/chart/?data_url=http://www.openeconomics.net/store/517d7c4e-3cb7-4e8f-aaa1-745dd665ad1f/data&ycol0=3">
<img class="displayed medium" src="http://m.okfn.org/files/talks/lugradio_20080719/img/wheat_3.png" alt="US Wheat Data" width="500" />
</a>

First up is output. As can be seen here output rose steadily (approximately linearly) up until the First World War. It then stayed flat or even fell during the inter-war period -- the Great Depression and the Dust Bowl can be seen in the sharp dip in the early 1930s. Following the Second World War output rose, accelerating (exponentially?) up until the early 1980s when it has flattened out, even declining (with sharp variations) to the present.

Looking at these raw output figures the immediate question one asks  (at least as an economic historian) is: what underlying causes drove these changes in output. In particular, output is the product of two factors: total acreage in use and yield (average output per acre) so it would be interesting to see time-series for them as well. Fortunately this data is also available:

#### Figure 2: Acreage (Millions of Acres)

<a href="http://www.openeconomics.net/plot/chart/?data_url=http://www.openeconomics.net/store/517d7c4e-3cb7-4e8f-aaa1-745dd665ad1f/data&ycol0=2">
<img class="displayed medium" src="http://m.okfn.org/files/talks/lugradio_20080719/img/wheat_2.png" alt="US Wheat Data" width="500" />
</a>

The first thing to note is that these series start in 1866, the year after the American Civil War ended. This was a period of great westward expansion in cultivation in the United States -- the "Opening of the Prairies". The graph bears graphic witness to these changes: we can see that harvested acreage tripled between 1866 and the outbreak of WWI in 1914.

This massive expansion was to have a profound effect far outside of the US: food prices dropped around the world due to the increase in supply. In Western Europe this lead to a 'Great Depression' in agriculture right up until the First World War (which in turn had a significant effect on European politics creating protectionist alliances between peasants and landowners in many European countries). It also assisted industrialization by keeping the price of bread low for the fast growing industrial proletariat.

However, by the end of WWI most of the acreage that could be cultivated was already in use. After that point, while there has been variation in planted acreage (perhaps driven by substitution between wheat and other crops) there has been no long term trend (whether increasing or decreasing). Thus, while the increase in output up to WWI can be largely explained by increases in acreage under cultivation [^1] the large increases in output in the post-WWII period can't be. This brings us then to the second major factor in explaining changes in output: yields.

[^1]: a crude eyeballing suggests that output increased somewhere between 3-4 times between 1866 and WWI. This is in line with the increase in acreage. That said, diminishing returns arguments (best land is cultivated first) would suggest that to maintain yield per acre on a vastly increased acreage would have necessitated some increase in yields.

#### Figure 3: Yield (Bushels / Acre)

<a href="http://www.openeconomics.net/plot/chart/?data_url=http://www.openeconomics.net/store/517d7c4e-3cb7-4e8f-aaa1-745dd665ad1f/data&ycol0=4">
<img class="displayed medium" src="http://m.okfn.org/files/talks/lugradio_20080719/img/wheat_4.png" alt="US Wheat Data" width="500" />
</a>

One could not ask for a sharper confirmation of our previous hypothesis than Figure 3. As it shows average yields were almost perfectly flat from 1866 up until the end of the Second World War. From that point yields **took off** growing sharply, but at an almost constant rate, up until the mid 70s, following which the growth rate slowed substantially  (though yields still continued to grow albeit with increased variability). In concrete terms this corresponded to a rise in yield from around 12 bushels per acre at the end of WWII to somewhere around 35 bushels per acre in the 70s -- and around 40 today.

To put this most starkly: there was a roughly 3-fold increase in yields in this 30 year period. Again this is a particularly 'graphic' testament to the 'green revolution' of the post-war period which was driven largely by the development and adoption of new corn varieties (hybrid corn), fertilizers etc.

#### Figure 4: Price ($ per Bushel)

<a href="http://www.openeconomics.net/plot/chart/?data_url=http://www.openeconomics.net/store/517d7c4e-3cb7-4e8f-aaa1-745dd665ad1f/data&ycol0=5">
<img class="displayed medium" src="http://m.okfn.org/files/talks/lugradio_20080719/img/wheat_5.png" alt="US Wheat Data" width="500" />
</a>

Lastly we come to price. Here, despite substantial fluctuations the basic trends fit with our historical intuition. There is little change between 1866 and WWI, a sharp rise during the war, a substantial decline in the inter-war period, then another sharp-rise during WWII (wars are good for farmers!) followed by stabilization (or even slight decline) until the mid 1970s when there is another sharp rise. Following that there is substantial variation but no great changes until the present when the line shoots up again (doubling from around $3 per bushel to somewhere near $6 in a year).

As basic economics tell us, price should reflect the interaction of supply and demand. The marked stability of price over long periods (particularly those where supply has increased) suggests then that demand has matched supply (or vice-versa) fairly well over this period (one might also need to take account of the fact that there may also have been substantial government intervention to stabilize prices).

Given that supply has risen substantially through the whole period, and especially since WWII (see Fig 1) this means that demand has also been climbing sharply. This is true: world population has increased at least 5x since 1850 and roughly tripled since WWII (in addition many people, especially in developed countries have increased their per-capita consumption, by eating more and better -- as well as wasting more).

It would be interesting to imagine what would have happened if this kind of population increase, particularly that since WWII, had occurred without the massive increase in yields shown in Figure 3 (part of the answer may be that population would not have increased so much ...). Certainly the price increases seen recently may reflect the kind of growing surplus of demand over supply that we would have seen without the 'green revolution'. As such, they may be signals of the significant readjustments  that will be needed in the near future, whether that be increases in supply, reductions in demand or more efficient use of existing supplies.

