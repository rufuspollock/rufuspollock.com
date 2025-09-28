---
title: >-
  2007 International Industrial Organization Conference (IIOC)
slug: 2007-iioc-conference-savannah-georgia
date: 2007-04-15T19:50:09
themes: []
tags: []
projects: ['Academia']
posttypes: ['Talks']
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 176
---

This weekend I've been at the [International Industrial Organisation Conference (IIOC)](http://ceps.georgiasouthern.edu/conted/IIOC2007conference.html) in Savannah, Georgia. I presented the [latest version of *Cumulative Innovation, Sampling and the Hold-Up Problem*](http://www.rufuspollock.org/economics/papers/holdup_and_sampling.pdf) and provided [discussant comments](http://www.rufuspollock.org/economics/papers/gilbert_and_katz_comments_iioc_2007.pdf) on Richard Gilbert and Michael Katz's paper on the [*Efficient Division of Profit for Complex Technologies*](https://zeus.econ.umd.edu/cgi-bin/conference/download.cgi?db_name=IIOC2007&paper_id=444). In addition I include below some very partial notes on some of the sessions I attended.


### Merchant or Two-Sided Platform (Andreu Hagiu)

Interesting paper on what distinguishes a 'Merchant' from a 'Two-Sided Platform' -- a merchant being distinguished by it taking possession (and then reselling) the goods while a platform remains just that (it just charges an access fee or royalty). Most of results, while no doubt involving some hairy algebra, were fairly intuitive. In a sense the paper is really another look at existing 'boundary of the firm' questions. After all the Merchant/Platform dichotomy is really just the Firm/Market one in a new wrapping. In that sense it is not surprising that larger externalities (whether in the form of complementary goods, or larger 'network' effects) imply greater benefits of internalization in the form of a Merchant (firm in the old literature).


### Too Many Complementors? Evidence from Software Developers (Kevin Bourdreau)

Saw this paper presented back at Toulouse Software and Internet Conference back in January. Was not convinced then by his argument that too many complementors can be bad for a platform because I didn't buy the identification strategy (or lack thereof). Since then has narrowed its focus and bolstered the underpinnings however I'm still not convinced by the conclusion. All he has shown is that no of new titles developed is an inverted u function of the number of the developer firms -- but to my mind this is a simple result of diminishing returns: as you have more developers you have more titles which means the rate of new title development should fall (since it generates less surplus both socially and privately). I don't see why this means that a platform would not would want to maximize the number of developers (and titles) on itself.


### Production Innovation Incentives: Monopoly vs. Competition (Marius Schwartz)

Extend standard results of replacement vs. efficiency effects to case of introduction of a new differentiated product.


### Fundamental Patent Reform and the Private Returns to R&D - The Case of Indian Pharmaceuticals

  * Claim: Product patents increase market value of Indian Pharma firms
  * Paper at a rather early stage
  * Too much going on in the data for one to be convinced Claim is true
  * Also concerns about basic idea: introduction of product patents known since 1995 so why should effect be seen in 1999-2005?


### Patent Damages and Spatial Competition (Matthew Henry and John Turner)

Model:

  * Hotelling ('spatial') competition with symmetric imitator and infringer at either end of unit line and linear transport costs (linearity turned out to be crucial to staying tractable)
  * Consider three types of damages regime:
    1. Reasonable Royalty
    2. Lost Profits
    3. Unjust enrichment (infringer disgorges all profits)
  * Patents which are valid with known exogenous probability gamma
  * Firms engage in Coasian bargaining in the shadow of the damages regime

Results:

  * Optimal regime is not unique
  * Lost profits:
    * For large V (value of innovation) this maximizes incentives to innovate
    * Does not maximize static welfare (imitator prices too high and serves under half the market)
  * Reasonable Royalty:
    * Maximizes static welfare as firms serve optimal amount of market (1/2 each) and thus minimize transport costs
    * For medium V this maximizes incentives to innovate
  * Unjust enrichment
    * Poor for welfare
    * Poor for incentives to innovate (incentives do not change with V)


### An Empirical Analysis of Patent Litigation in the Semiconductor Industry (Bronwyn Hall and Rosemarie Ziedonis)

Polanyi (1944)

> "Floods of patents are issued ... the validity of which is uncertain. At the meeting of the British Association, held in 1931 we hear patents described as 'lottery tickets'. Manufaturers can never tell whether they are infringing on some patent and becoming liable to heavy damages. 'A bad patents system ... is a fetter on the hands of industry and an instrument of blackmail.'"

  * NTP patents were actually overturned post RIM settlement
  * Ref: Shapiro (2001), Cohen et al. 2000 
  * Litigation risk increased relevant to R&D spending (Zidonis 2003; Bessen and Meurer 2006) but fell or remained the same on a per-patent basis (Lanjouw and Schankerman 2004)
  * More aggressive enforcement of patents by "trolls" in some sectors (Lerner 2006 on financial patents -- I [discussed this paper](http://www.rufuspollock.org/archives/156) at the Toulouse Software and Internet conference back in January).
  * Levi-Straus example (failing firms enforce their IP)
    * patent number: 6138595 (2001) for 5 cornered pocket
    * seems very similar to original patent from 1981 ...

The paper:

  * Semiconductor firms
  * Estimate per-firm hazard rates
  * Distinguishes between rival and non-rival litigation (rivals are those with sales in the same IC segment)
  * Data:
    * Patent law suits filed in US district courts and ITC (ITC, Derwent, 10-ks, press releases)
    * Semiconductor product market data (ICE)
    * Patents (NBER, Delphion)
    * Financials (Compustat)
    * 282 obs of 547 litigation events
  * Results:
    * Design firms more likely to litigate (controlling for R&D intensity)
    * ... (see the paper)
    * Despite increased strength of patents stable enforcement rates 
    * Residual growth (controlling for R&D intensity etc) in prob of being a target has grown significantly 1980 - 2001 (by about 10%)
    * Sharp upturn in prob of being a target of a nonrival at end of period 1998-2001

### Research Joint Ventures and Leniency Policy (Michelle Goeree)

  * Research joint ventures could be a way to collude since frequently members of a given venture are rivals in the end product market
  * Change in Antitrust rules made it harder to collude in the product market (1993: made it easier for whistle-blowers)
  * Identification strategy: if RJV are used for collusion then this change should increase RJV activity but if not used for collusion should see no effect
  * Data construction: another interesting story
    * RJV data from Link (1996)
    * But that does not list firm names so you need to go to federal register to get firm names to link them in
    * Then you add in compustat data ...
  * Result:
    * '1993' effect for Telecom, weak for Transport, weak for Pharma
    * no effect in other industries such as Software

