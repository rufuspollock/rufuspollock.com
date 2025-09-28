---
title: >-
  Experimental Games
slug: experimental-games
date: 2008-02-29T17:52:32
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - page_id: 278
---

{{< toc >}}

## Ultimatum Game

GÃ¼th, Werner, Rolf Schmittberger, and Bernd Schwarze (1982) "An Experimental Analysis of Ultimatum Bargaining", Journal of Economic Behavior and Organization, 3:4 (December), 367-388.

Two players A (proposer) and B (responder)

  0. A is endowed with some amount (x) of a good (usually money).
  1. A makes an offer to B consisting of a transfer of y < x.
  2. B accepts or rejects the offer.
  3. Payoffs:
     * B accepts: A: x-y, B:y
     * B rejects: everyone 0

Prediction: (SPNE) y=0, B accepts.

Observed Outcome: (roughly) y<0.2x are rejected and offers are usually in range 0.2x-0.6x with extra weight around 'fair' splits (50:50).


### Variations

  1. Multiple proposers with responder selecting at most one offer. Results in competition among proposers and convergence towards 0 for proposer everything for responder (as predicted by theory).

## Reverse Ultimatum Game

Gneezy, Haruvy, & Roth (2003)

2 players, A (responder) and B (responder).

  0. A is endowed with some amount (x) of a good (usually money).
  1. A makes an offer of y <= x
  2. B accepts of rejects this offer
    * B accepts: game ends.
    * B rejects: If A would receive nothing game ends with 0 payoffs all round. A can choose to end game or continue. If continue return to stage 2 but with constraint that offer must exceed existing offer by some increment c.

Predictions: (SPNE) B rejects all offers below x-c and A continues to propose offers up to x-c.

Outcome:  A receives c and B receives x-c.

## 3-person Ultimatum Game

Same as ultimatum game except that a third person C (the dummy) is added. A now proposes a 3-way split. Only B gets a veto with C being entirely passive.

Prediction:
  
  1. (SPNE): same as in ultimatum (0 offer and B accepts)
  2. Preference for fairness: approx equal division
  3. Induced preferences from repeated encounters: some amount to B s.t. they accept but 0 to C

Outcome: 0 to C and same offers to B.


## Dictator 'Game'

Forsythe R, Horowitz JL, Savin NE, Sefton M, 1994 Fairness in simple bargaining experiments. in Games and Economic Behavior

NB: Not really a game since only one person has an action.

Like Ultimatum game. 2 players A (dictator) and B. A proposes a split and that split is then carried out without any further intervention.

Prediction: offers should be zero.

Observed Outcome: (crudely) in general non-zero transfers are made.

### Modifications

Allow dictator to take money from B in addition to giving it. This reduces transfers to almost zero.

## Trust Game

Berg, Joyce, John Dickhaut, and Kevin McCabe, "Trust, Reciprocity, and Social History," Games and Economic Behavior, (10)1995, pp. 122-142,

2 players A and B.

  0. A is endowed with some amount (x) of a good (usually money).
  1. A makes an offer to B consisting of a transfer of y < x.
  2. The sum B has is then multiplied (optional) to ky > y.
  3. B then makes a transfer back to A of z. 
  4. The game ends with payoffs:
     * A: x-y + z
     * B: ky - z

Subgame perfect outome: y=0, z=0

## Public Goods Games

Rather older than the Trust Game but similar:

N players.

  1. All players endowed with some amount of good x(i) (usually x(i) are equal, equal to x)
  2. Players contribute some amount y(i) for a common 'public good' the rest (x(i) - y(i)) going for some private good.
  3. Payoffs are realized. The exact form of the payoffs varies across settings but essentially a player receives:

     * Their private investment
     * Some function of the total public investment (perhaps excluding their own contribution). Usually this takes the form of straight multiplication by some factor k followed by equal division (so each player gets kY/N where Y is total public goods contribution).

     For example, cite{andreoni_1988} has a setting where each player gets their private investment plus half the total public investment.

Remarks: Pareto optimal outcome always involves everyone investing everything in the public good.

Variations: repeat the game multiple times.

NE: invest everything in private good, 0 in public good (free-rider outcome).

Observed outcome (roughly): in one-shot game find that subjects contribute around half-way between pareto optimal and free-rider outcome. Contributions decay as game is repeated and tend towards the free-rider outcome over time (though exact free-riding is not usually realized).

Further empirical results:

  * cite{isaac_ea_1994} find that multiplication factor has a significant effect (unsurprisingly) and interacts with group size. 
  * Those not contributing in one round rarely do so in future rounds.


### Variations

1. Repetition (already mentioned)

2. Punishment option (non-contributors can be punished at some cost to the punisher).

3. Public knowledge of contributions.

### Explanations

As with many of these games the evidence clearly indicates some explanation beyond pure NE (within the game context) is needed. The basic possibilities are:

  1. (Lack of) Contextualization. Subjects carry over behaviour from outside of the lab. For example, used to playing infinitely repeated versions of this game (in which cooperation can be Nash) they "incorrectly" carry this over to one-shot or finitely repeated situations.
  2. Learning. Subjects do not realize what the dominant strategy is and it takes time (repetition) for them to learn. Once they learn they play 0.
  3. Strategic behaviour (with incomplete information). Suppose one has some non-zero belief that other players are "irrational" and will contribute to the public good. Then, *even if rational* oneself, it may pay to contribute early on to prevent the opponents "learning" and starting to play Nash. If everyone has such non-zero beliefs then even if *everyone* is "rational" one can sustain (at least early on) equilibria where there is contribution to the public-good -- though this should unravel as one comes into the final period.


{{andreoni_1988}}[p.294] (citing {{isaac_ea_1988}) points out that "experienced" subjects (i.e. those who had already played at least once) still contributed to the public-good in early rounds even though they had previously "learnt" to free-ride. This provides suggestive evidence against 2 and in favour of 3.

{{andreoni_1988}} goes on to test this in more detail providing more detailed evidence against all views. The setup is as follows: there is one set of subjects whose groups are randomly "mixed" after each repetition (i.e. members of group are randomly reassigned to other groups) while the other set of subjects played normally (i.e. the participants in the group were the same in each period). Subjects in the "mixed" condition were called 'Strangers' to emphasize that they only met by chance while those in the other condition were called "Partners". The set-up of the "Strangers" case should eliminate the strategic play option (every game is, essentially, one-shot). Finally, in addition there was a "restart" in which the basic 10-round experiment was repeated (without pre-announcement) for another 10 rounds (with all the same groupings). The findings are surprising:

  * Strangers consistently give more than Partners
  * Strangers free-ride less than Partners
  * Strangers show a lower decay rate than Partners
  * Restarts only significantly affect Partners who return to (close) to original levels while Strangers are unaffected.

As Andreoni states (p. 301): "These results suggest that we may need to turn to theories of non-standard behaviour."

However, it is noteworthy that a later paper, {{croson_1996}}, goes the other way. Further work summarized in the paper of Croson and Andreoni (2001) (Partners versus Strangers: Random Rematching in Public Goods Experiments) suggests that some of the contradictions (e.g. strangers giving more than partners) is best explained as arising from participant 'confusion' leading to semi-random behaviour.


