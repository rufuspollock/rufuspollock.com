---
title: >-
  Optimal size of nations and organizations
slug: optimal-size-of-nations-and-organizations
date: 2008-03-02T19:29:05
themes: []
tags: ['Government']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1893
---

This is a topic I've thought about quite a bit before[^1][^2] but on this particular occasion it arose from a discussion yesterday with Jim McCue about the size of Cambridge colleges and the growth of the EU.

Having (many smaller) different competing organizations rather than (fewer/one bigger) organization is:

* Bad because lack of standardization means fewer economies of scale and scope and higher transaction costs (e.g. for trade) and greater free-rider issues *across* jurisdictions/organizations.
* Bad because there are common/public goods with fixed costs and those costs are shared fewer people
* Good because of variation: the average rate of improvement is proportional to the variance in features (cf. Fisher's theorem for natural selection). More states or organizations mean  a greater variety 
of approaches -- institutions, cultures etc -- plus, possibly, fiercer competition (no sclerotic empires). Together these drive forward overall advance at a greater rate.
* Good because smaller means better governance: a smaller polity or organization will be a) more responsive to the preferences of its members b) have fewer transaction costs (e.g. in monitoring and voting) c) lesser problems with collective action / free-rider problems (*within* the entity -- across entities the problems may be worse, but that is the previous item)
* Good because humans 'feel' better within polities and organizations of a smaller size. (more autonomous, more in control of their lives, understand better what is happening to them)

I imagine that getting any empirical information here would be tough and models would have a tendency to give results highly sensitive to their specification.[^3]
One interesting general observation is that simple prison dilemma type arguments would suggest that the "political economy" of polity (or company) formation may result in entities that are too large. Specifically, imagine that polities or companies compete: for example, states engage in wars over territory or rights the inter-country rules of the game in things like trade -- consider the US vs. Burkina Faso in a bilateral trade negotiation. In a cooperative world people would agree not to compete -- not go to war -- and divide up the pie in some peaceful way.

However, the bigger entity would have an incentive to deviate from this "cooperative" equilibrium and seize the weaker entity's share of the pie. Basically might makes right. Knowing this each side has an incentive to get bigger and bigger and there is an escalation in state or company size (if you get bigger I want to get bigger). Ultimately this escalation would stop: at the point when the dis-economies of scale in coordination are started to outweigh the benefits of bigness in warfare (for states) or lobbying or predatory pricing (for companies). You can think of the great empires: benefiting from their ability to levy tribute or the conquer others but often internally bloated and inefficient.

This equilibrium from the point of view of the overall welfare must be inefficient since no account has been taken of the costs in terms of governance or general well-being (our last two bullet points abo
ve). Overall this would imply that polities -- and companies -- are larger than they should be.

[Later] The very day of writing this I came across a review of Alesina and Spolaore, *[The Size of Nations][size]*, while idly flicking through old JEL (March 2005) reviews. It appears from the review to make several similar points (not exactly surprising given how the ideas themselves are fairly obvious ...):

[size]: https://mitpress.mit.edu/books/size-nations

> "The nation-state is defined in terms of a monopoly of coercion and the legal use of force within its boundaries [ed: Weber's definition]. The central tenet of the book is that the size of nations is determined by a trade-off between the benefits of economies of scale in providing public goods (e.g. defense) and the costs of heterogeneity in preferences over the provision of these public goods."
>
> "This raises the question why, instead of a unified nation-state, we do not observe a series of overlapping jurisdictions that best resolve this trade-off for individual public-goods. The authors argue convincingly that such a configuration would face prohibitive transaction costs and fail to internalize economies of scope. The nation-state monopolizes the provision of essential public goods (law and defense) and adopts a host of other function because economies of scope and transactions costs. Some functions are delegated to subnational levels of government, but subnational jurisdictions do not cross national borders." [from Redding's review, p.161]

[^1]: One particular early idea was whether one could 'generalize' some parallel computing 'results' such as Amdahl's law to organizations. The diminishing returns of Amdahl's law occur because only some portion of the program is parallelizable and hence adding more processors provides ever less speedup as one approaches the basic speed constraint set by the remaining serial part of the program. This problem will be made even worse if there is a need for intercommunication between processors (e.g. due to some part of the program having sequential dependencies as would the be the case where there are set of parallelizable tasks that need to be performed sequentially). Thus, while more processors allow for greater application of the divide-and-conquer effect (and therefore specialization and economies of scale) they may require greater transaction costs in terms of communication/synchronization between the processors. At some point the transaction costs become larger than the divide-and-conquer benefits and the system becomes slower. (This also has connections to the transaction costs theory of the firm, though, there the comparison is not between economies of scale and transaction costs but between transaction costs within the firm versus those outside of the firm -- in the market.)

[^2]: A second point was on the empirical evidence on optimal size of such entities. One often hears comments about 5-12 being the optimal size for a team or 300-500 being the optimal size for a community (see e.g. Alexander et al's *A Pattern Language*) but I've never yet come across (though I haven't looked that hard) firm evidence on which these figures are based. [Later]: I imagine reading Alesina and Spolaore's book could prove valuable here.

[^3]: Though see e.g. Christopher Alexander's pattern for states suggesting a size of between 5-15 million citizens -- and compare to the fact that almost all states are significantly larger than this). On the theoretical size there's all kind of stuff including classic Coase work on transaction cost theory of the firm -- which you could also apply to political entities like States. Of course, Coase ideas are studiously neutral on whether firms are too big or too small.

