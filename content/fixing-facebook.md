---
title: "Fixing Facebook: How to Resolve the Facebook Monopoly and Make the Social Network Open (Again)"
---

*First version: July 2018, updated Sep 2018. Posted publicly in this form Jan 2020. This originated as a series of Q&As arising from the publication of [The Open Revolution][or] in June 2018.*

# Summary: Facebook could be open -- just like the Internet

Facebook could be open just the Internet was and is. This can be achieved by:

* Making the key protocols that underlie Facebook (identity/profiles, friending, posting, feed) open along with high quality implementations in software.
* Establish federated core profile database -- analogous to DNS for domain names on the Internet.
* Content such as photos and posts should be hosted at individual service nodes -- analogous to websites on the Internet (your facebook profile *is* many people's modern website).
* Permit Social Service Providers to be the hosters of these services nodes, both hosting content and acting as gateways onto the social network. These are like ISPs but for this new social network layer. These  service providers use the open protocols to access and hosting of social profiles and connectivity to the "OpenSocial" network.
* Allow anyone to innovate and build on top of OpenSocial, regulate content and behaviour according to local social norms and regulations (just like the net). Ensure that Facebook provides access to these new Social Service Providers on standard, regulated and nondiscriminatory terms.

Finally, and crucially, put in place remuneration rights as a way to pay for future innovation of the protocols and software so as to ensure continued incentives for innovation, freedom of enterprise, and that the platform continues to be open.

[or]: https://openrevolution.net/

{{<toc>}}

# In your book ["The Open Revolution"][or] you argue that the Facebook monopoly is a problem? Why is that?

Facebook's monopoly of dominant social networks undermines fundamental freedoms and fairness -- of choice, of speech, of association, of enterprise and innovation. It means control of those freedoms lie in the hands of an unregulated monopolist who has demonstrably abused their power and our trust. Furthermore, we have a better "open" way that would provide all the benefits of a well-functioning social network whilst restoring those essential freedoms of choice, participation and enterprise.

Two billion people are on Facebook. Facebook has become *the* place where many "live online". With its current monopoly, Facebook get to make the rules of who gets to participate and how -- and we have no say in that process or even visibility into it. Cf the napalm girl affair, Cambridge Analytica etc.

This is deeply problematic. Facebook's monpoly of essential common communication infrastructure gives them an unacceptable degree of unsupervised, undemocratic power and control over our social and political affairs. We never allowed our phone and postal systems this degree of unregulated, unsupervised monopoly and those systems had nothing like the control over the *content* that Facebook has with, for example, the newsfeed.

Second, there is the [Kronos effect][]. A monopoly like Facebook has a major detrimental impact on innovation and opportunity because Facebook have huge incentives to take over or destroy any innovation that threatens its monopoly -- and in particular to deny competitors access to its platform (for example, Instagram and WhatsApp). That is bad for innovation and bad for competition.

Third, there is the simple cost of monopoly: Facebook as a for-profit enterprise will have strong incentives to overcharge us in the sense of selling too much attention to advertisers (and over-charge the advertisers too).

Fourth, the basic impact on freedom choice. I just have no choice but to accept Facebook's rules on what I can say and do on their platform because they are the only game in town. There is no democratic system of appeal or oversight and that is a huge loss of freedom of choice and freedom of expression.

[Kronos effect]: https://openrevolution.net/kronos-effect/

# Let's assume that the Facebook monopoly is a problem, what do you suggest we should do about it?

Let's start by setting out the options:

1. Leave Facebook alone - allowing it to continue to grow and (ab)use its monopoly unchecked. For our purposes here,  we've already established this is unacceptable.
2. Intervene in some way ...

We're obviously pursusing 2. What are the options here?

1. Build some alternative to Facebook either "bottom-up" in the community or with government support and have that take over
2. Regulate Facebook in some way
3. Take the "open" approach

I'm very sceptical of (1) because getting to scale with a platform like this is really hard, and its exceptionally hard when you are doing that in the face of an entrenced monopolist. The only chance of (1) succeding in my view is with regulatory intervention both to prevent Facebook taking aggressive counter-action (as the Anti-trust suit against Microsoft hampered them in killing off alternate browsers) and to push Facebook to support some kind of interoperability (essential if you are to get round the empty dance-floor problem with your new network). Both of these take us towards regulation which is option (2).

However, the regulation option is not super clear. What exactly would be invovled in regulation? Platforms like social networks naturally tend to one system (cf the Internet) and trying to foster many competing social networks with different (incompatible) protocols would actually be counter- productive (who wants to log into ten different services all the time?). As such, the opportunity for classic horizontal competition seems limited. Facebook looks like an old-fashioned phone network in many ways and those always ended up as one system and then either nationalised or regulated e.g. AT&T.

Perhaps the latter "AT&T" option could work? Have FB regulated like a monopoly utility. The problem is that FB is in a fast-moving technologically complex space. Plus our past experience of regulation with e.g. AT&T can't inspire us too much: lots of regulatory capture, blocking of innovation by the incumbent etc.

Another regulatory option could be to try and induce competion. Specifically, the regulator could introduce rules to force FB to allow competitors to interoperate with Facebook -- i.e. if I start a new social network OpenNet my users can connect and correspond with FB users just as if they were on Facebook. This is probably the stronger idea. However, done properly would start to amount to the open approach but with the disadvantage that some regulatory agency would have to supervise all the technical details of full interoperation with the Facebook platform (what APIs they must expose etc), handle all the relevant privacy issues etc. 

# The "open" approach

## Preliminaries: Facebook as the Internet and Platform Economics

tl;dr 1) It's useful to think about the analogies of Facebook and the "Internet". 2) Understanding platform/network businesses and their feedback effects. cf section in [The Open Revolution][or] on Spotify story or [Ubernomics][].

[Ubernomics]: https://rufuspollock.com/ubernomics/

We've had one recent network that achieved global take up at a scale similar to Facebook: the Internet. The Internet is and was as complex in features and functionality as Facebook but unlike Facebook it is open: it is not owned by anyone, rather the protocols and software that run it are open and free, and anyone can operate a service to provide internet access (be an Internet Service Provider). The Internet is therefore existence proof that open platforms are possible.

3 types of (dominant) platform:

* Platform is proprietary - owned by one entity (for-profit)
* Platform is open: platform can be connected to by anyone
* Platform is cooperatively owned by either sellers or buyers

Difference between physical and digital platforms: in physical world *someone* e.g. gov, a committee etc would have to actually run the marketplace even if it were "neutral". It's a physical piece of land and there's a limit to who can be there etc. In digital world you can make the platform "open" (if there is an order book that may be rival like land unless you decentralize that too).

Even with open digital platform you will still need some governance to determine how you evolve the platform -- what new protocols do you create. [Remuneration rights][rr] could help decentralize even this ...

## Social Networks as Platforms

We need to distinguish Social Network (SN) system (protocols, software etc) vs Social Network service (that software running on servers somewhere that users can access). cf Internet vs Internet Service Providers. It is the Social Network that is the platform. When we say "Facebook" we describe both: both the protocols and the service; so it is crucial we distinguish them. (NB: FB itself will likely already have this separation internally).

If a system is open you can a) have competition in service provision and b) unleash innovation on top of the platform (anyone can build).

There may be some key "central" databases, for example the list of user profiles. To resolve this, you either need to adopt a decentralized system *or* you need a regulated central "exchange/database".

Whilst the decentralized option is attractive longer-term, short-term a regulated exchange may be fine. For example, crucial to a social network (or the internet) is some registry of identity. On Facebook this is your login, on the Internet it is your domain name. The Internet's system is decentralized whilst, obviously, FB's identity system is centralized. In a transition it may be wise to start by simply regulating and "opening" up the central FB identity registry rather than trying to build a decentralized system from scratch fright now.

## OpenSocial: the Open version of FB and How it Works

First, we must distinguish the platform itself (key protocols) from the service of providing a live network.

Next, identify key protocols (e.g. identity, friending (and associated sharing parameters), posting/sharing, newsfeed)

Then, identify essential shared databases e.g. identity (maybe including social graph but would prefer not).

Make the protocols open and have high quality open source implementations. If concerned about "unfair taking" from FB enter arbitration procedure to agree fair value of those assets (distinct from the monopoly power this value is probably quite low -- FB did not do a lot of innovation here)

A key question arises: how would we resource the continue development of these protocols and software? Answer: use remuneration rights. See https://openrevolution.net/remuneration-rights/

Federate the identity (and friending) system (or start with regulated access to FB by approved third party competitors)

Finally, enable the entry of new social service providers to run the OpenSocial (previously FB) software and protocols by ensuring they can interconnect with FB system and central identity and friending service. These providers take on hosting their users content e.g. photos, posts etc and managing their identity.

[rr]: https://openrevolution.net/remuneration-rights/

## Facebook as Marketplace and how to make it an Open One

An Analogy: Facebook is current the monopoly owner of the town marketplace and owns all the store space and can control who comes to the market, what they sell or buy and controls everything that is shown (including adverts) to those who come.

We want to make the marketplace "open" in the sense of owned by all / no-one, allowing FB and anyone else to continue to provide "hosting" services to stallholders but no longer controlling who gets to be a stallholder, who comes to the market or what gets shown to them. Instead we will establish standard "open" rules for the economics side of how to participate in the market (show up at X time, book your slot using this sheet) and allow local rules to determine what is allowed to be offered or exchanged there (e.g. no pornography, no pork); finally establish a subscription paid either by everyone in the local community (as part of taxes) or on those who participate in the marketplace and use that money to pay for maintenance of the rulebook (note maintenance of the market space itself is delegated to market space providers companies who compete to offer their services to sellers or buyers).

## Open Facebook in a paragraph from [The Open Revolution][or]

> Now, it is important to emphasize that convergence on a single platform need not automatically mean monopoly for a single firm. This is something that is easy to forget when we are surrounded by monopoly platforms like Google, Facebook, Microsoft etc. However, an alternative is where the platform is a protocol or is otherwise neutral and non-owned. The classic example of this is the Internet and the World Wide Web. Here we have converged on a single network and single set of protocols but it is not owned or controlled by any single firm. As long as you adhere to the technical rules of the Internet protocols - and any relevant legal rules - you can connect to the Internet and to other users - the Internet is a platform that intermediates between all its users.
>
> It is interesting to contrast this with Facebook to see how different things could be: Facebook is a platform that intermediates between its users, primarily providing media sharing, communication, identity and spam management services. The protocols and platform Facebook provides are largely proprietary and controlled by them and they get to determine, ultimately, who connects to their platform. But there is no reason Facebook could not have been like the Internet with the key protocols being open and universally accessible. Instead of a proprietary social network controlled by one corporation we would have had an open social network owned and controlled by its users - in the same way the Internet is ultimately owned and controlled by its users. In an open social network world, anyone - suitably identified - could connect and innovate on the platform.

# Appendix

## A Taxonomy of Platforms

### Factual Dimensions

* Order book vs no order book (common "live" DB vs non-live common DB). In other words: Can buyers and sellers transact "one to one" or do we need a clearing house
  * No order book: Food marketplaces, Operating Systems (Microsoft Windows), Telephone network, Internet, Google (as search engine), Electricity networks, Academic Journals, Electrical sockets
  * Order book: Stock markets (Nasdaq), Uber, Airbnb, eBay etc
* Physical vs virtual (digital?). Physical platforms tend to have more issues with congestion, distance, etc

### Choice Dimensions

* Open vs Closed
* Centralized vs Decentralized

### Features (Outcomes)

* Who gets charged (buyers, sellers, community)
* Who decides who connects to the platform
* Who decides who builds on the platform
* Who decides how the platform itself evolves?

## Platform Laws

1. The law of one: platforms tend to one (because of the snowball effect)
2. Go for broke: size matters to it's all about who gets there first (platform competition is a tournament)
3. Charge the stronger, subsidize the weaker (whomever you need to get to liquidity ...) aka Charge the one who charges fees
4. Chickens and eggs ... (platforms are tough to get started because you need both buyers and sellers together)
5. Open is best, coop is staid, proprietary is bad
6. Monopolists always start nice (in fact they treat you to a free dinner) but they end up nasty ... (don't take free crack from your friendly neighbourhood crack dealer),

## Notes to Self

### Blockchain, ICOs and platforms ...

ICOs are a way of betting on platforms ... -- in the past you could only do this via VC funds. Its a type of crowdfunding with all the advantages and disadvantages of that model. It has one additional advantage: payment is tied to use of the platform -- people investing have to spend their tokens in the system so it ties investment to usage (and allows users and those investing service capacity to benefit from the success of that platform). It's as if Uber issued equity to its early drivers with the amount of equity diminishing as the platform grows. The benefit of the blockchain model, in theory, is that you do *not* need a central issuer of that equity (i.e. Uber inc) but you can use the platform itself to do the issuing (via the algorithm).

ICOs and Blockchain may help the initial investment problem but they don't make clear how you support continuing innovation.

Bitcoin has a decentralized model for paying those who maintain the network (in a more centralized model you could also just have service fees). But what about Internet - that was not blockchain / bitcoin but it had a sutainable ISP model?

### Random ideas

A story about a nice guy who at beginning is really decent and then gets more and more controlling (metaphor for proprietary platforms)


