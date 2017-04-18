---
title: >-
  FLOSS 2008 Workshop on Free/Open Source Software
slug: floss-2008-workshop-on-freeopen-source-software
date: 2008-06-30T10:33:22
themes: ['Information Economy', 'Notebook']
tags: []
projects: ['Academia']
posttypes: ['Own Work', 'Talks']
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 327
---

Last week I attended [FLOSS 2008](http://e.darmon.free.fr/floss/workshop.html), the second international workshop/network meeting on FLOSS (Free/Libre/Open Source software) in Rennes, France. I was [presenting](http://rufuspollock.org/economics/papers/innovation_and_imitation_talk_rennes_2008.pdf) my paper [Innovation and Imitation with and without Intellectual Property Rights](/economics/papers/innovation_and_imitation.pdf) (and would have offered discussant comments but the author of the paper I was scheduled to discuss had to pull out at the last minute). In addition to this I got to hear a variety of interesting talks. On some of these I was able to take notes which I have included below for the 'delectation' of anyone else who is interested.

## Mikko Valimaki: IPR and Open Source Software

  * Goodman and Myers (2005) -- the 3G standard.
  * Leveque and Meniere 2007: what does RAND mean
    * reasonable royalty is R = c (v1-v2)p where c is incremental costs of licensing, v1-v2 is gain from using this pattern over second-best.
  * Other questions for royalty-setting
    * quality of volume of patents
    * early or late innovators
    * cumulative royalties or one-time fees
  * But all models he knows of have non-zero royalty fees
    * [ed]: not surprising given that you will always get interior solutions
  * Windows/Samba discussion
    * specific sets of terms
    * provide RF for the open source community
  * Commission Decision para 783
    * "On balance, the possible negative impact of an order to supply on Microsoft's incentives to innovate is outweighed by its positive impact on the level of innovation of the whole industry."
  * Nokia to acquire Symbian:
    * "a full platform will be available ... under a royalty-free license ... from the Foundation's first day of operations ... the Foundation will make selected components available as open source at launch."
    * [ed]: Motivation here is clear: Nokia care about the hardware and for them software is a complementary good -- which they therefore wish to be as cheap as possible. But this raises question as to what is being made open: is hardware patents or pure software patents (and if so how big a deal is this)

### Stefan Koch: Efficiency of FLOSS Production

  * Question of efficiency of open source development
  * How much software did we get for our effort
    * Is OS a waste of resources?
  * Discussion without much empirical basis
    * Claim: fast and cheap, high quality, finding bugs late is inefficient (actually large effort) -- see IEEE Software 1999
  * Completely unknown as no-one keeps time-sheets. So
    * Effort based on participation data
    * Effort based on product -- look at software and ask how much effort would be needed in commercial environment
  * Empirical research in open source
    * Mainly case studies
    * Helpful but need proper large-scale analysis
  * Mined software repositories [ed: cf. today FLOSSMatrix, FLOSSMore]
    * 8,261 projects
    * 7,734,082 commits
    * 663M LOCs
    * resources and output is skewed: top decile of programmers: 79% of code base, second decile: 11%
  * Effort estimation based on actual participation
    * active programmer months (define active as committing in a given month)
    * high correlation with LOC added in month
  * Cumulate this number for each project
    * But not equal to a commercial person-month
    * How do we scale: use 18.4 h/w taken from stats for committers on Linux kernel
    * [ed:] this is the key assumption. The whole point is that FLOSS effort is not observed and they are using a measure of output (committing) and trying to infer actually activity
  * Manpower function modelling:
    * Norden-Rayleigh model (1960)
    * Some set of problems N (unknown but finite)
    * Probs are solved independently and randomly (following Poisson)
    * This fits ok but has eventual decline in participation which does not occur
    * Modify this: in particular to allow introduction of new problems
        * Introduce in prop to original no. problems, in prop to current set of problems etc
        * Also have different learning rates
        * [ed: but isn't the setup a little different. Really it is a question of success vs. non-success in terms of acquiring users + some kind of bound on amount of participation due either to fission or complexity]
  * Product-based estimation
    * COCOMO 81 and COCOMO 2
  * Results:
    * Comparison COCOMO - Norden-Rayleigh
    * For COCOMO 81 cannot find parameters favourable enough to explain Norden-Rayleigh curve
    * For COCOMO 2 can find parameters but very favourable
    * Suggest (roughly) that FLOSS very efficient (but not very rigorous)
  * More formal estimation using all models etc
    * Norden-Rayleigh significantly below prodcut-based estimates (factor of 8 in mean)
  * Interpretation
    * FLOSS v. efficient (self-selection for tasks etc)
    * Extremely high amount of non-programmer participation (1:7 relation ...)
  * [ed]: not sure about this generous view. Other explanations
    * No quality measurement (also mentioned by Koch)
      * OK: lot of code but low quality
    * (Related) Many sourceforge projects are incomplete, easy bit at the start 
      * Later comes a lot of refactoring/writing documentation. This may display significant diminishing returns
    * Many FLOSS projects come from what were originally commercial projects. In that case:
      * code may have already been written
      * conceptual components have been done already
    * Trade-off of time vs. productivity
      * May be more productive to only work 10h a week but then product might not be ready for 10 years
  * Form discussion
    * interesting point: Nokia thinking of moving to more FLOSS in-house because they can't manage their 5-10k programmers centrally any more


### Mickael Vicente: Shift to Competences Model: A Social Network Analysis of Open Source Professional Developers

  * Robles 20007
    * Statistics on Debian showing increasing corporate involvement
  * Social network extraction
    * Get repo logs
    * Create link between 2 developers if they have committed on the same file (non-directed graph)
      * Simplification: the best collaboration of each developer (directed graph) -- pick other developer with whom they have committed most files in common
    * Longitudinal analysis
      * extract clusters
  * Correlation with professional career
    * CV collected on Internet, personal web page etc (96% collected)
  * Interesting data

### Nicholas Radtke: What Makes FLOSS Projects Successful: An Agent-Based Model of FLOSS Projects

  * Positive Characteristics of FLOSS
    * High quality (Low defect count: Chelf 2006)
    * Rapid development
    * Violates Brooks law (Rossi 2004)
 * Risky Business 
  * for every successful FLOSS project there are dozens of unsuccessful projects
  * Corporate IT manager survey (2002)
    * 41% mention inability to hold someone responsible for software
  * Attempts at Simulating FLOSS
    * SimCode (Dalle and David 2004)
    * OSsim (Waggstrom et al 2005)
    * ...
    * K-Means stuff
  * Simulate across landscape
    * Not social network
    * Focus on developer decision to join/contribute to projects (Agent-Based Modelling)
  * Defining Success and Failure
    * Traditional metrics do not work well (on budget?)
    * Completion (Crowston et al. 2003)
    * Progression through maturity stages (Crowston and Scozzi 2002)
    * Number of developers
    * Mailing list activity
    * Project outdegree, Active developer count (Wang 2007)
  * The Model Universe
    * Agents and projects
    * Agents:
      * Consumption: 0-1
      * Producer: 0-1
      * Resource: 0-1.5 (1=40h)
      * Memory: agents only aware of some subset of projects
      * Needs vector (preferences)
      * utility: linear sum of: similarity match + current popularity (current resources) + cumulative resources + download + f(maturity)
    * Projects:
      * resources needed
      * current resources
      * cumulative resources
      * download count
      * preferences: same as agent but converges towards those had by agents working on it
  * Agents choose between projects each time period
     * have some randomness in that use multinomial logit: prob choose project i ~ exp(mu * Utility of project i)
  * Results
    * Simulate over 250 time steps ~ 4 years
    * calibrate [ed: in a way I was not quite clear about]
    * compare simulation with empirical data from sourceforge
      * developers per project
      * projects per developer
    * Find that (from simulation data) downloads and cumulative resources are not important

### Fabio Manenti: Dual Licensing in Open Source Software Markets

  * Benefits of Going Open Source
    * feedback from community
    * network effects (usage)
    * competitive pressures (e.g. Netscape) [ed: not sure this is a benefit]
  * Dual-licensing
    * Kosky (2007): 6% of representative sampl of European OSS business firms employ DL strategies


### Alexia Gaudeul: Blogs and the Economics of Reciprocal (In-)Attention

  * What blogs are 
  * Reasons for blogging
  * Question: do you befriend (link) because of content produced or do you produce content because of friends
  * General points
    * Market interactions only part of wider class of reciprocal relations
    * Time vs. money economics
    * Unique dataset, very detailed and complete, to test networked relations
  * Model -- but left out due to time
  * Dataset: livejournal 2006
    * Sociology: teenagers to young adults (15 to 23), female (67\%), Americans (70\%)
    * Fast growth: created in 1999, 8M accounts, 1.3M active
    * FLOSS but for-profit (SaaS)
    * Great part from self-referential
    * Lively: 4 comments per post on average
    * Federated by communities: no. of communities per person 15
    * Journals updated for more than 2 years on avg
    * 70\% have posted in last 2 months
    * No. of entries: 1 every 2 days
    * No. of friends: 50 avg
    * Balance between friends and friends of
    * Balance between comments received / made
  * Friendship patterns
    * May be balance but does not explain no. of friends of diff. individuals
    * Need to distinguish
      * Norm of reciprocity: more promiscuous bloggers accumulate friends
      * Content attractiveness
        1. Quality/freq. of posts
        2. Interactivity (comments per post)
  * Regressions
    * Reciprocity: No. blogs read (friend) = b * number of readers (friend of) + error
    * Activity: No. readers = cX + error -- X = matrix of ind. variables
    * Endogeneity issues [ed: all over the place)
    * Regress: ln(Friends) = ln(Friend of) + ... (with instrumenting Friends Of on Activity so solve endogeneity issues)
      * Saturation around 400 friends seemingly (few with more)
    * Max no. of friendship when your no. friends = no. friends of (maybe)
      * A norm of reciprocity
    * Issues with endogeneity of activity (which was used to instrument friends of) 


### Sylvain Dejean

  * Does ICT lead to the Internet lead to a global village or a cyber-balkan
  * What leads to emergence of virtual commmunities
  * Is the heterogeneity of contributions an impediment to self-organize
  * How to manage virtual communities
  * Agent-based model:
    * Individuals defined by some characteristics
    * Herfindahl index measures degree of self-organization [ed: why self-organization]
    * Communities change via selection and variation


