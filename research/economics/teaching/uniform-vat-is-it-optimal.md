---
title: >-
  Uniform VAT: Is It Optimal?
slug: uniform-vat-is-it-optimal
date: 2009-10-15T17:55:02
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - page_id: 448
---

Newbery has stated that a uniform commodity tax is optimal:

> Ramsey prices were also the answer to the first optimal tax problem -- what is the efficient way of raising revenue if lump sum taxes (LSTs) are not available? This optimal tax interpretation is not much use as one should think of optimal tax systems in which other taxes and the expenditure side deal with e.g. distribution and progressivity -- hence with labour separability uniform VAT is optimal. ["Questions Arising from Lectures and Advice for Answering Exams", p.2 para 2]

Several of you have found this a bit surprising in light of e.g. Ramsey results.

Below I provide a (fairly) detailed explanation of why this is (approximately) correct.

### The Theory

Standard theory, e.g. as in the Ramsey analysis, implies differential commodity taxes (crudely Ramsey taxes vary inversely proportionately with the elasticity of demand).

However, observe that if there were one perfectly inelastic good Ramsey would imply taxing that good alone. If this good were labour (leisure) this would mean taxing labour alone. Furthermore, a tax on labour is equivalent to a uniform tax on all other (consumed) commodities (why? Think about the budget constraint: wL = x.p. A proportional tax of t on labour equates to a (1/1-t) markup on all prices). This is an important point so let me reiterate it:

FACT 1: a uniform commodity tax (on consumption goods) is equivalent to just having an income tax (a tax on labour) and vice versa.

Now, in general, this is unlikely to be the case and therefore a uniform tax rate is *not* optimal. (In fact things can get much worse: there may be multiple solutions to the optimal tax problem, and intuitive relationships such as the same FOCs implying the same tax rates may prove to be false. For more of the gory details see Stiglitz and Atkinson 372 ff.)

Now, of course, the Ramsey case ignores equity considerations (it is a pure "efficiency analysis). Does introducing these have an impact on its own? The answer is no: "horizontal equity" does not require uniform taxation of commodities. (see SA p. 392).

Finally, what about if we have a general "tax system" in which we have:

  1. Commodity taxes
  2. (possibly nonlinear) income taxation (i.e. a tax on labour/income which can vary with the level of income)
  3. These taxes vary with (observable) characteristics of the individual
  4. A poll-tax/subsidy, i.e. a lump-sum tax/subsidy to individuals constant across individuals.

NB: if income taxation is linear we may ignore since WLOG it can be set to zero  by FACT 1 (tax on income is equivalent to uniform tax on all other commodities).

A poll-tax/subsidy is a form of lump-sum taxation (though a highly restricted one in that it is usually assumed that it cannot be varied across individuals). As it is non-distortionary, assuming there are no equity considerations, we would just use the poll tax and have no other taxes.

What about if there are equity considerations? In this case commodity taxes will have a role to play.

How exactly these taxes vary is not trivial and non-intuitive. For example, one might think that having a poll tax/subsidy might mean that commodity taxes are only there for redistributional purposes and hence we should tax luxuries heavily and necessities little. However, indirect taxes not only affect redistribution but also raise revenue. As they raise revenue they reduce the level of the poll-tax (or even convert it into a poll-subsidy). But in their role as revenue raising we want commodity taxes to be *efficient* -- which implies classic inverse-elasticity form (and which may well involve taxing luxuries at a low rate and necessities at a high one).

To illustrate these countervailing effects: in the case of the linear expenditure system (u ~ sum log x + log l) these effects exactly cancel out and you end up with a uniform tax rate (equivalent to an income tax by FACT 1!).

Introducing a non-linear income tax one can show that this result generalizes to the case where the utility function is weakly separable between labour and all goods (formally: the marginal rate of substitution between good j and k is independent of labour L for all j and k). For the gory details see AS 435 ff. Note also this assumes individuals only differ in their wage rates.

Crudely, the intuition (if one exists), is that the separability condition just mentioned is exactly that which means that the 2nd-best distortion introduced on labour supply (by the income tax) does not spread to the allocation between goods.

RMK: the obvious violation of separability is for *leisure* goods (leisure being the 'other-side' of labour supply).

RMK: the result assumes individuals differ only in wage rate. Where other heterogeneities exist this result need no longer apply. In fact this feature is crucial to the results: (roughly) heterogeneity in individuals was confined to the labour side of things (the wage rate) and hence with separability one could address this heterogeneity purely on that (labour) side of things without messing with differential commodity taxes.


CONCLUSION: Newbery's comment is correct assuming non-linear income taxes and weak separability.

