---
title: >-
  Workshop on Rationality and Emotions: Notes from Day 2
slug: workshop-on-rationality-and-emotions-notes-from-day-2
date: 2008-01-10T20:28:44
themes: []
tags: []
projects: ['Academia', 'Happiness']
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 259
---

Herewith are further (partial, impressionistic) notes from the second day of the two-day [workshop](http://www.robinson.cam.ac.uk/academic/lectures.php) ([programme](http://www.robinson.cam.ac.uk/academic/robinson_rationality_programme.pdf)) on *Rationality and Emotions* organized by Miriam Teschl at Robinson College here in Cambridge.

----

### S-Shaped Probability Weighting and Hyperbolic Preference Reversal - An Intimate Relationship by Herbert Walther

Walther has published these results as a 2003 paper in Journal of Economic Behaviour and Organization.

<http://www.robinson.cam.ac.uk/academic/robinson_rationality_walther.pdf>

#### Overview

  * Empirical regularities:
    * hyperbolic discounting
    * sign effect: loss discounted less than gains
    * preference reversal:
    * magnitude effect: preference for losses before gains
    * s-shaped prob weighting (Gonzales and Wu 1999, Fehr-Duda, 2006 et al.)
      * prob weighting can explain Allais paradox
  * How to resolve?
  * Ans: EU maximizer considers *anticipated emotions reactions to resoluton of uncertainty*
    * prob weight derived via intertemporal state dependent EU max
    * using this can explain most empirical effects

#### Model and Results

Part 1: Generating the S-shape prob distbn

  * EU of some binary prospect L(p, w1, w2), w1<w2 is additively separable into:
    * EU of wealth
    * EU of elation (if you win)
    * EU of disappointment (if you lose)
    * last two both fade away over time
  * Implied prob q(p) is as follows:
    * $$q(p) = p \frac{1 + (1-p)\mu}{1 + (1-p)p(\gamma + \mu)}$$ where
    * $$\gamma = \frac{\delta \alpha}{\delta + \theta}$$ where $$\delta$$ is discount rate, $$\alpha$$ is weighting of elation and $$\theta$$ is the exponential rate of elation decay
    * $$\mu = \frac{\delta + \beta}{\delta + \rho}$$ where $$\beta$$ is weighting of disappointment and $$\rho$$ is exponential rate of disappointment decay.
  * Really recommend looking at Walther's paper (fig 1) which is on Robinson website
  * Generates the S-shaped effect
    * furthermore have testable empirical predictions: higher time preference (i.e. more impatient) should be associated with more pronounced S-shape (i.e. more risk-loving). So e.g. people who are gamblers should be saving less. 

Part 2: Empirical regularities 

Having generated the S-shaped result Walther goes on to show how this can generate most of the empirical regularities we are interested in.

  * Look at some payment/contract whose probability of payment fulfilment is falling over time (this way we get probability in which we need)
  * Now have some S-shaped setup and probability that goes into this S-shape is dropping over time (contract is less likely to be fulfilled).
  * Hyperbolic discounting: can also now generate hyperbolic discounting within this same framework (other explanations e.g. Souzou 1998, Dasgupta and Maskin (2005) only do it on its own).
    * Logic underlying hyperbolicity: at start contract is very likely to be fulfilled so if it does not lots of disappointment -- so (exp) discount rate is very high. Over time prob falls and S-shape prob distbn kicks in (so elation outweighing disappointment) and discount rate falls.
    * prediction: poor will show more hyperbolicity than rich
  * The sign effect: gains discounted more than losses
    * Logic: again simple. If loss is very likely little disappointement but a very certain gain has lots of potential for disappointment.
    * prediction: again the sign effect is more pronounced for poor than the rich.
    * magnitude effect for losses: higher losses have higher impact that lower losses (because straightforward wealth utility becomes more important than disappointment/elation effect).
  * preference reversal
    * poor will prefer losses before rich subject but gains after rich subject
    * preferences are same but marginal utility of wealth is different

#### Summary

  * Simple model that is a small extension of basic EU maximization most of the empirical regularities.
  * If diminishing marginal utility of wealth poor people will behave 'less rationally' than rich people despite having same preferences
  * For the future: Why is prob weighting evolutionary sustainable?
    * potential answer: in hunter gather society there are externalities in that (large) gains and losses are shared (this would => S-shaped prob distbn).

----

### "It's a boy! Behavioural and Neural Evidence on Self Delusion" by Danica Mijovic-Prelec

  * Deficits (due to lesion) on right side of brain lead to deficits in left hemisphere
  * Furthermore these patients are not aware of the deficit and *deny its existence* (to the extent of confabulating experiences)
  * Sackheim-Gur 1979: self-deception in social psychology
    * played people mixture of their own phone and others
    * averse to your own voice
    * people would not hear their own voice and furthermore physiological measure of stress indicated it went up when 'not hearing their voice (when it was there) -- i.e. when people were self-deceiving
  * Sackheim-Gur criteria:
    * individual holds 2 contradictory beliefs
    * beliefs held simultaneously
    * individual is not aware of of holding one of the two beliefs
    * nonawareness of this belief is motivated

#### Experiment

  * shown korean figures and asked to classify as male/female
  * first stage: get figures and must classify (5c for each correct prediction -- correct measured against classification by some control group)
  * second stage: must also predict gender of next figure (and then classify)
    * paid like before for classification but bonus for being in top x% of predictors

#### Results

  * Focus on items  that were 'well-classified' by control
  * First classification: 65% accurate
  * Anticipation: 50% accurate (as expected since randomized)
  * Second classification: <65%
    * anticipation effects classification 
  * stronger for males: anticipated as male results in classification as male 72% (for females like first time round)
  * calculate self-delusion index for each subject
    * four options for response pattern (starting with female) of form 1st classif, anticipation, 2nd classif:
      * FMF: honest
      * FMM: self-deluding
      * FFM: inconsistent
      * FFF: consistent
    * need to subtract inconsistency from self-delusion percentage to get 'true' self-delusion
    * index = % self-delusion / % inconsistency (could use difference)
  * fMRI
    * expect that self-deluding subjects behave differently from inconsistent (and honest and consistent)
      * notably don't show this activation on consistent trial (when they also confirm their prediction)
    * this is what they find (v. significantly)
    * in attentional and cog. control regions
      * self-deluding and inconsistent is similar
      * however big difference in parahippocampal gyrus (associated with memory)
  * [rp] question: could some of this come from a priming effect combined with better recall. I anticipate X, which primes me. Then suppose I see the figure and have a vague recall from before. Suppose that people experience different priming effects -- then those with a strong priming effect feel conflicted and have more stress (i remember Y sort of but do I really or I just doubtful because of having seen X) which means more fMRI anomalies *and* and means they are more likely to 'self-delude' while those with weak priming simply aren't sure what they think (not really excited/conflicted) and just go randomly with M/F (so 'self-delusion' or 'inconsistency' are equally likely).

----

### Herding and Social Influence in Economic Decision Making by Michelle Baddeley

  * Solomon Asch
    * Length of line experiments (everyone says line is B when actually A) 
  * Task design: stock-picking
    * two charts for past prices of a stock
    * shown faces along with their associated choice (controlled by experimenter)
  * Results:
    * strong effect of other decisions on own decision (on average 72% vs. 50% choose the one chosen by herd) 
    * perhaps not very surprising here given the lack of info about stocks (and their underlying equivalence) -- a small piece of information should have a dramatic effect


