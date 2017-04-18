---
title: >-
  Reflections on the Blockchain
slug: reflections-on-the-blockchain
date: 2016-07-02T13:16:47
themes: ['Bitcoin', 'Blockchain', 'Information Economy']
tags: []
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 2032
---

I am not a blockchain believer. I am sceptical of the grandiose claims made for the impact of the blockchain: that it will revolutionise our economies, governments and organizations making them flatter, fairer and more democratic.

The blockchain hype reflects an increasingly prevalent techno-solutionism -- a techno-fadism if you will -- where we imagine that some sprinkling of tech pixie-dust will solve some hard and important social problem: coordination vs decentralization, equality vs hierarchy etc. Not only is this mistaken, but this obsession with tech distracts us from the hard and less glamorous work needed to make real change -- as well as generating disillusion when our new tech god inevitably fails us.

This is not to dismiss blockchain as a technology. There are clearly important use cases: financial ledgers, robust provenance sysetems and more. However, these discard the most innovative components be that elaborate smart contract systems or distributed "trustless" consensus via proof of work. Without these, blockchain is really a fairly old set of ideas -- merkle hash trees, distributed databases etc. The novelty then, if any, is is in a convergence of different methods and new levels of efficiency. This is the stuff of solid, and valuable, progress. But it isn't a revolution in governance, production or the structure of society.

[toc]

<img src="http://rufuspollock.org/wp-content/uploads/2016/07/broken-chain.jpg" alt="" />

## The DAO: Code is not Law -- and It's Dangerous to Think So

A [code flaw in the Ethereum-based DAO contract system][code-flaw] has allowed a hacker to make off with around $50m. As a result, this community appears to be gradually waking up from a tech-induced mania. In that mania people thought that old and hard social and political coordination problems would suddenly dissolve away in a puff of blockchain crypto magic.[^dao-hubris]

[code-flaw]: https://blog.ethereum.org/2016/06/17/critical-update-re-dao-vulnerability/

[^dao-hubris]: Some of the early -- and I mean just two months ago -- hubris is painful to read. For example, consider this from [a post by one of the DAO founders][early-dao]: "The cat is out of the bag: a **provably fair, 100% decentralized governance model** is now publicly available for anyone to copy, improve on and reproduce. This includes its smart contracts and the Token Creation module itself, all provided free and open source under the LGPL. Major exchanges have backed this model, while the code has been audited by the best minds in the field, the greater daohub.org community and even the company that audited Ethereum itself." [emphasis added]

Some people [pointed out in advance][larimer] that the hard part of the DAO is not the tech but the social processes. Here's Dan Larimer writing in early May (Dan is a founder of BitShares and one of the originators of the concept of DAOs):

> ... success and failure of a DAO/DAC depends not on the technology used, but entirely on how a community interacts with the technology and each other.
>
> ...
>
> One of the first things we learned from BitShares is that the vast majority (90%+) of stakeholders did not participate in voting. This is due to the fact that voting requires time, energy and skills that most investors lack. How many people have the economic, technical and entrepreneurial skills to vote responsibly?
> 
> The DAO currently requires a level of voter participation that is much higher than BitShares has ever seen for a worker proposal. ... The DAO is expecting much higher levels of participation of voters without using proxies. Unless the majority of DAO stake is held in a few active hands, this will be very hard to achieve. [Ed: note the DAO has so far not even got to voting on anything and is now perhaps permanently crippled by its hack]
> 
> ...
> 
> The DAO has tentatively raised $100 million dollars worth of ETH, but so far the investors have taken no real risk. Every single person who has purchased DAO tokens has the ability to reclaim their ETH so long as they never vote. The end result is a massive marketing campaign that totally misrepresents what has been invested and what hasn’t.

[larimer]: https://steemit.com/crypto-news/@dan/is-the-dao-going-to-be-doa
[dao-debate]: http://www.coindesk.com/amid-huge-fundraise-thedao-sparks-a-public-debate/

People have been proposing more "cooperative" technology funding mechanisms especially for open source [for years][cofundos] (I've even proposed one myself called Open Offsets). What's hard about such mechanisms is a) sustaining contribution levels (avoiding free-riding) b) deciding how to allocate funds c) incentivising good work.

The DAO managed to take advantage of a "gold-rush" mentality to do an extraordinary crowdraise. But this addresses only (a) in the list above -- and does so only on a very temporary basis and with the assistance of a speculative mania. It does almost nothing on (b) or (c).

Fundamentally "cooperative" efforts to fund tech faces a hard collective action / public good / free-rider problem. Over thousands of years we have come up with solutions to these problems: they are called things like states or companies or cooperatives. They are messy and difficult and have annoying voting or governance systems. We geeks, especially those with libertarian tendencies and crypto PhDs, like to sneer at these institutions as archaic and incredibly inefficient -- "democracy is broken", the "state does not work" etc. But it is  worth stopping for a moment and reflecting on why we think we are so smart and these institutions so dumb.

As far as I can tell there is *nothing* about the DAO or most of the other "exciting" blockchain efforts be they replacements for Uber or new prediction markets that actually require the blockchain. The DAO could have been run as a completely traditional company with a voting system base on share ownership. Of course, it wouldn't have been very sexy. However, it would have had the substantial advantage of focusing people on the real challenges here namely governance and management of large groups rather than distracting with a sprinkling of blockchain fairy-dust.

As Larimer writes in his excellent piece:

> Fancy technology can obscure our assessment of what is really going on. The DAO solves a single problem: the corrupt trustee or administrator. It replaces voluntary compliance with a corporation’s charter under threat of lawsuit, with automated compliance with software defined rules. [Ed: and it has turned it has not even done that as we see the hack precipitating a turn to human governance] ... but it doesn’t solve most of the problems the regulations were attempting to address.
> 
> **What The DAO doesn’t solve is all of the other problems inherent with any joint venture. These are people problems, economic problems, and political problems**. In some sense, The DAO creates many new problems caused by its ridged rules and expensive machine-enforced process for change.
> 
> The DAO doesn’t solve the “group trap” where by losers subsidize winners. It disempowers the individual actor and forces him to submit to group decision making. It doesn’t make raising money cheaper for companies, it just adds blockchain-enforced bureaucratic and political processes.

My concern ultimately is that we are, once again, off down a path of technology-obsession. We start thinking digital tech can solve just about everything. Yes, Moore's law *is* pretty amazing but that does not justify these kind of category errors: tech is good at solving engineering-style problems like building a better mousetrap and not especially good at solving social coordination problems (aka politics).

Furthermore, as a result of our tech obsession we are diverted from the more important -- but less exciting -- social, political and personal work to actually change ourselves and our societies for the better. Moreover, when, as it inevitably will, the hype dies down we will be left with disappointment and disillusion. These will act as an obstacle to the slow, gradual efforts we actually need if we are to make a fairer, more collaborative and more open world -- digital or otherwise.

[cofundos]: https://lists.okfn.org/pipermail/okfn-discuss/2007-October/005851.html
[early-dao]: https://blog.slock.it/the-inexorable-rise-of-the-dao-2b6e739b2615#.ce1p138oq
[ft-sceptics]: http://ftalphaville.ft.com/2016/05/17/2162084/more-decentralised-autonomous-organisation-dao-mysticism/
[legal-sceptic]: https://prestonbyrne.com/2016/05/17/thedao-dont-walk-away-restructure/

## The Internet changed the world - surely the Blockchain will too?

The claim that the blockchain is the "next Internet" in terms of its importance and impact is quite common. And the claims are, if anything, even stronger in the area of governance and how we organize and cooperate (or compete) -- after all, isn't the blockchain all about "trustless" decentralized systems?

There are several points to make. First, (sadly) the Internet's impact on improving governance and/or enabling new or better organizations is and probably will be relatively limited. I will not dwell on this here and recommend reading [this post of mine from 2012][managing] and [this prescient Wired piece from 1995][wired-dejavu]. (I emphasize if you think I'm wrong don't worry: this point will not matter much for what follows).

Second, we need to think about what the Internet actually did. The Internet was a technology that reduced communication costs. Now communication is central to creating and running organizations. Thus, the Internet had a direct and very large impact on the key activity involved in connecting and coordinating groups of people, especially where they are geographically distributed.

[wired-dejavu]: http://www.wired.com/1995/05/dejavu/
[managing]: https://blog.okfn.org/2012/09/13/managing-expectations-ii-open-data-technology-and-government-2-0/

This was especially true for more informal and/or less well resourced groups. From the early 2000s, as the Web/Internet matured, we got free and easy-to-use VoIP, online video chat etc. The cost of rich long-distance communication dropped torwards zero not just one to one but for groups too (though it is still not zero: getting decent video conferencing for 30+ people at a reasonable price). We should also be mindful of non-Internet factors such as low-budget flights that have also played an important role in enabling organizations to be more distributed -- in person still matters a lot (and more than we think).

If the blockchain is to be like the Internet then the question we need to ask is *which* costs the blockchain reduces and *where* those matter for organizing human activity. Currently, the answers out there are pretty fuzzy. It is, of course, good to be optimistic and see possibility. At the same time, blind optimism and a lack of reflection undermine the chance of real progress -- and hype diverts energy from other efforts which may be less sexy but more impactful.

### An Example of Overblown Claims

To illustrate here's some commentary on a [recent piece entitled "The DAO - An MVP of a Political System"][dao-mvp]:

[dao-mvp]: https://medium.com/outlier-ventures-io/daos-the-mvp-of-a-political-system-5797ddf45d2f 

> A DAO 2.0 can provide a third way between state ownership and market ownership of production?—?community ownership. A communal model is not a new idea, cooperatives, mutuals, building societies and credit unions have been around for some time. But these organisations were limited in their scale and so were organised around job or location. The Internet, blockchain, smart contracts and DAOs mean cooperatives can have members from anywhere in the world who can communicate, lend, borrow, and vote on how to allocate shared resources.

As this notes, the communal / cooperative model is not new - they have been around for hundreds if not thousands of years. So, what exactly, is the blockchain going to solve? And I focus here on the blockchain: the ellision in this article between the Internet and the blockchain in one simple sentence is something of a sleight of hand -- and a common one. Of course, the blockchain may be a complement to the Internet, an essential missing piece that will suddenly combine with it to deliver us the holy grail of decentralized, democratic governance. But if so, the mechanism better be spelt out clearly -- otherwise we are just exploiting the Internet's halo effect.

And I have my concerns. The hard things about communal models is the governance and coordination problems: how do you incentivise team production and divide rewards in ways that reflect contribution, how do you manage shirking and free-riding, how do you avoid decision-making gridlock without reverting to hierarchy or dictatorship, how do you (and do you) separate ownership (equity) and control (management and voting power)?

Let me be clear I'm a *big fan* of "co-x" models (coliving, co-producing, coops and collaboratives). In fact, I spent a lot of my time thinking about them at the moment. However, I just don't see a big way that blockchain makes a *lot* of difference to organizing or running them (it might make a *bit* of difference but it's pretty minor). To quote Larimer again from above re the DAO:

> Fancy technology can obscure our assessment of what is really going on. The DAO solves a single problem: the corrupt trustee or administrator. It replaces voluntary compliance with a corporation’s charter under threat of lawsuit, with automated compliance with software defined rules ... but it doesn’t solve most of the problems the regulations were attempting to address.
> 
> What The DAO doesn’t solve is all of the other problems inherent with any joint venture. These are people problems, economic problems, and political problems. In some sense, The DAO creates many new problems caused by its ridged rules and expensive machine-enforced process for change.

If we are serious about the potential impact of blockchain on governance and organizations then I would suggest we need to spell out *in detail* a particular organizational model and how the blockchain helps. Having done that I'd recommend doing some "lab experiments" to see how these would work.

Returning to the [DAO MVP arcticle][dao-mvp], here's some more:

> A DAO 2.0 as a global cooperative organised around values would stand in contrast to a nation-state organised around where you happened to be born, or a trade union organised around a specific job. Platform cooperatives can take advantage of the global scale of the Internet and blockchains. There could be Digital Nomad DAO, or a Minecraft DAO, or a Greenpeace DAO. They can be as big or small as the community needs. Members lend, borrow, and collaborate fluidly with projects and businesses. Individuals are both owners and labour. The owners, management, and employee divisions can be broken down to better serve society as a whole. If there is no work for a particular worker one week, then they still receive a dividend from the DAO.

Wow! A bold vision. The question again is *where* is the blockchain making a difference here? Using the Internet and very cheap "off-the-shelf" corporate structures we can already bring people together from all over the world and "leadn, borrow, and collaborate fluidly wirht projects and businesses." What is the friction that the blockchain is eliminating exactly?

And when we start saying things like: "owners, management and employee divisions can be broken down" I start getting really suspicious! It sounds exciting but how, exactly? How will blockchain make a difference to all the traditionally hard problems of dividing rights and responsibilities? Role differentiation such as owner vs employee encapsulates a whole bunch of complex differences ranging from skills to risk preferences. How is the blockchain going to help with that? I've been in a variety of organizations over the years, I've even run one. I've spent a lot of time looking at these issues practically and theoretically and they are **hard and complex**. Of *all* the things that smart contracts might help with these kind of things are the last thing I would be looking at. 

> The First and Second Industrial Revolutions ushered in new intellectual and political paradigms centred around capitalism and socialism. It would be arrogant of us to believe that today is different and that we live in the final intellectual and political paradigm. 

This is revealing in its assumption that technological change (the industrial revolutions) created new political paradigms. That is far from clear and in fact the direction of causation may be the other way round. I'm not arguing that we live in the "final" paradigm, but I would point out that despite thousands of years of our best thinkers working on political and social theory actual advance seems relatively minimal -- Plato's Republic is still relevant today. The organizational structures we have now have existed in one form or another for almost as long. Even things we associate with modernity such as Marxist Communism have existed as organizational structures for centuries -- for example, early Christian communities were probably organized on communistic lines.

The irony here is that I *do* think that the digital technological revolution *does* make possible a new political/economic system built around [openness][open]. However: a) the possibility comes from the fundamental change to an economy built on a nonrival commodity: information b) realising that possibility needs traditional political action not more tech. 

[open]: /open/ 

> The decentralisation trends of the Internet, blockchains, the internet of things and artificial intelligence will result in new social, political and economic structures. At the moment, we lack a framework through which to see all of these trends. I think The DAO is the first experiment in testing a new organising principle.

How is the DAO that different (or better) from the organizational experiements we could do in virtual worlds?

## Gold-rush or Internet-rush?

A  basic question about the blockchain frenzy is to what extent this is a "gold-rush" versus an "internet-rush".

Both these "rushes" involved speculative manias but they differed fundamentally in their substance and impact. A gold-rush ultimately just means diverting productive effort into mining more of an inert metallic substance that convention has blessed as a store of value for millenia but which has little or no actual use-value. In this sense it is basically "unproductive".

By contrast, an internet-rush is productive. Though it also involves a speculative mania that may misallocate capital and energy it does provide investment capital that creates new and valuable innovations and infrastructure.

Whilst it seems clear that at least some of the BlockChain technology is valuable it is still not entirely clear how much and in what area. For example, it seems quite possible that we may get better trade-settlement mechanisms for banks but at the same time be very sceptical about the claims for revolutions in governance and organizational design or the "return" of a truly decentralized Internet.

(We could also cite the tulip mania here and add to our recommended reading list for avid blockchainers Kindelberger's classic "Manias, Panics, and Crashes - A History of Financial Crises").

### The Virtual World Gold-Rush: Another Analogy

There are also other similarities with virtual worlds: remember the incredible [$100k someone paid for a virtual space station][entropia] back in 2005 in SecondLife? Eerie similarities with incredible sums people are currently willing to pump into the bewildering variety of blockchain crowdsales each of them predicated on the assumption that one day their particular cryptocurrency / marketplace will make it.

[entropia]: http://www.cnet.com/news/man-pays-100000-for-virtual-resort/

To be clear virtual worlds exist and are going strong and that $100k space station sold out for a profit years later. BUT: virtual worlds though interesting haven't revolutionized our economies or our societies or created a breakthrough in how we cooperate and govern ourselves. This should temper our enthusiasm for some of the bolder claims of the blockchain believers.

*Aside: if one were being "Devil's Dictionary-ish" I'd define a BlockChain crowdsale as an equity offering to uninformed investors in wildly speculative ventures using a currency of unprecedented volatility. (Examples:[maidsafe raises][1][^maidsafe] and [issues][2], [mastercoin price chart][4], [mastercoin seeks new start as omni][3], [dubious participants and financial woes][5] etc)*

[1]: https://blog.maidsafe.net/2016/05/31/maidsafecoin-announcement/
[2]: https://forum.safenetwork.io/t/current-finance-condition-and-statement-of-maidsafe/1017/6
[3]: http://www.coindesk.com/mastercoin-new-beginning-omni/
[4]: http://coinmarketcap.com/currencies/omni/
[5]: http://www.bloomberg.com/news/articles/2015-12-30/the-final-days-of-the-bitcoin-foundation-

[^maidsafe]: "Those that have been involved with the SAFE Network since the days of the crowdsale will know that while the sale was very successful from a community-participation perspective, it was less so from a funding standpoint and didn’t give MaidSafe the necessary resources to fully accelerate development. The anticipated $8 million (£5.5m) and 3 years of running costs actually equated to $2 million (£1.4m) with the crash in the mastercoin price and fall in bitcoin price taken into account since that time." https://blog.maidsafe.net/2016/05/31/maidsafecoin-announcement/

## Governance Matters in Bitcoin

From [Mike Hearn's Why Bitcoin is Forking][forking]:

> The problem is that any change, no matter how obvious, can be nixed entirely if it becomes “controversial”, meaning another person with commit access objects. As there are five committers and many other non-committers who can also make changes “controversial” this is a recipe for deadlock. The fact that the block size was never meant to be permanent has ceased to matter: the fact that removing it is debated, is, by itself, enough to ensure it will not happen. Like a committee with no chairman, the meeting never ends. To quote the committer who has pushed hardest for stasis, “Bitcoin needs a leader like a fish needs a bicycle”.

[Ed: see again the [Dictator and the Anarchist][dictator] ...]

And it [all goes wrong socially ...][hearn-leaving]:

> In the span of only about eight months, Bitcoin has gone from being a transparent and open community to one that is dominated by rampant censorship and attacks on bitcoiners by other bitcoiners. This transformation is by far the most appalling thing I have ever seen, and the result is that I no longer feel comfortable being associated with the Bitcoin community.
>
> ...
>
> In August 2015 it became clear that due to severe mismanagement, the “Bitcoin Core” project that maintains the program that runs the peer-to-peer network wasn’t going to release a version that raised the block size limit [called Bitcoin XT]. ...
>
> The release of Bitcoin XT somehow pushed powerful emotional buttons in a small number of people. One of them was a guy who is the admin of the bitcoin.org website and top discussion forums. He had frequently allowed discussion of outright criminal activity on the forums he controlled, on the grounds of freedom of speech. But when XT launched, he made a surprising decision. XT, he claimed, did not represent the “developer consensus” and was therefore not really Bitcoin. Voting was an abomination, he said, because:
>
> >    “One of the great things about Bitcoin is its lack of democracy”
>
> So he decided to do whatever it took to kill XT completely, starting with censorship of Bitcoin’s primary communication channels: any post that mentioned the words “Bitcoin XT” was erased from the discussion forums he controlled, XT could not be mentioned or linked to from anywhere on the official bitcoin.org website and, of course, anyone attempting to point users to other uncensored forums was also banned. Massive numbers of users were expelled from the forums and prevented from expressing their views.
>
> As you can imagine, this enraged people. Read the comments on the announcement to get a feel for it.

Ed: Oh, the deep and tragic irony of it: the revolutionary decentralized, P2P currency that no-one controls and has at its heart an automated machine-driven consensus (no humans to  mess things up) is finally brought low by the most traditional kind of politicking and in-fighting. Yet again, technology is no match for basic social problems of collaboration and (human) consensus. The fault dear Brutus lies not in our technology but in ourselves! This is for me one of the great lessons here and of so much techno-solutionism: the misplaced belief that we can take a technological shortcut to solve some hard social problem (currencies at heart are a social problem based as they fundamentally are on trust and belief).

*Note: I am not endorsing Mike Hearn or anyone else in this controversy since I am not expert enough to make judgments. However, the quotes cited do definitely point to significant disagreements and social challenges in the community -- irrespective of who you think was "right or wrong".*

## The Myth of a Costless, Ownerless Network

From [Mike Hearn's departure piece][hearn-leaving]:

> Bitcoin is supposed to respond to this situation with automatic fee rises to try and get rid of some users, and although the mechanisms behind it are barely functional that’s still sort of happening: it is rapidly becoming more and more expensive to use the Bitcoin network. Once upon a time, Bitcoin had the killer advantage of low and even zero fees, but it’s now common to be asked to pay more to miners than a credit card would charge.

[forking]: https://medium.com/faith-and-future/why-is-bitcoin-forking-d647312d22c1#.kbf30gw0v
[dictator]: http://rufuspollock.org/nonfiction/dictator-and-the-anarchist/
[hearn-leaving]: https://medium.com/@octskyward/the-resolution-of-the-bitcoin-experiment-dabb30201f7#.z9gh72vlm

## Lessons from History

The "DAO Fiasco" is leading many to speculate on the "governance" lessons for decentralized systems -- and the dangers of thinking that code can so easily substitute for law. (See e.g. [this][this], [this][dao-social-problems], and [this urbit post][urbit-dao]).

In such circumstances it would be worth taking a look at some of the old, now almost pre-historic, discussions about governance in virtual worlds as they have an eerie similarity. For example, there was the famous governance debate that arose in LambaMOO in the 90s as a result of a virtual rape. Memorarbly reported by Julian Dibbell in his piece on the [The Toading of Mr Bungle for Virtual Rape][dibbell] it illustrates both that classic human governance questions will inevitably rear their head even in "code-based" worlds and that the law/code excitement is not as neew as we might think.

[this]: https://medium.com/@Alex_Amsel/faildao-why-the-ethereum-foundation-had-to-step-in-ad30a95b8d3a#.37sojet5e
[dao-social-problems]: http://www.coindesk.com/system-problems-social-issues-daos-structure/
[urbit-dao]: https://urbit.org/blog/dao/
[dibbell]: http://www.juliandibbell.com/articles/a-rape-in-cyberspace/

### Appendix: The Toading of Mr Bungle and Governance in Virtual Worlds

*Here are some relevant excerpts from Dibbell's excellent but lengthy article.*

What is the lesson? Put simply: virtual worlds tend to encounter just the kind of hard governance problems of "real-life" and have just as hard a time resolving them. The "magic" of digital technology, the limitless space of virtual realms, sadly is of little help in solving classic collective action / principal agent problems that bedevil the invention of better forms of governance and collective action. (See also [The Dictator and the Anarchist][dictator]).

Excerpts from <http://www.juliandibbell.com/articles/a-rape-in-cyberspace/>

> ... [The benevolent Dictators get tired] But the wizards of LambdaMOO, after years of adjudicating all manner of interplayer disputes with little to show for it but their own weariness and the smoldering resentment of the general populace, had decided they’d had enough of the social sphere. And so, four months before the Bungle incident, the archwizard Haakon (known in RL as Pavel Curtis, Xerox researcher and LambdaMOO’s principal architect) formalized this decision in a document called “LambdaMOO Takes a New Direction,” which he placed in the living room for all to see. In it, Haakon announced that the wizards from that day forth were pure technicians. From then on, they would make no decisions affecting the social life of the MOO, but only implement whatever decisions the community as a whole directed them to. From then on, it was decreed, LambdaMOO would just have to grow up and solve its problems on its own.
>
> Faced with the task of inventing its own self-governance from scratch, the LambdaMOO population had so far done what any other loose, amorphous agglomeration of individuals would have done: they’d let it slide. But now the task took on new urgency. Since getting the wizards to toad Mr. Bungle (or to toad the likes of him in the future) required a convincing case that the cry for his head came from the community at large, then the community itself would have to be defined; and if the community was to be convincingly defined, then some form of social organization, no matter how rudimentary, would have to be settled on. And thus, as if against its will, the question of what to do about Mr. Bungle began to shape itself into a sort of referendum on the political future of the MOO. Arguments broke out on *social and elsewhere that had only superficially to do with Bungle (since everyone seemed to agree he was a cad) and everything to do with where the participants stood on LambdaMOO’s crazy-quilty political map. Parliamentarian legalist types argued that unfortunately Bungle could not legitimately be toaded at all, since there were no explicit MOO rules against rape, or against just about anything else — and the sooner such rules were established, they added, and maybe even a full-blown judiciary system complete with elected officials and prisons to enforce those rules, the better. Others, with a royalist streak in them, seemed to feel that Bungle’s as-yet-unpunished outrage only proved this New Direction silliness had gone on long enough, and that it was high time the wizardocracy returned to the position of swift and decisive leadership their player class was born to.
>
> And then there were what I’ll call the technolibertarians. For them, MUD rapists were of course assholes, but the presence of assholes on the system was a technical inevitability, like noise on a phone line, and best dealt with not through repressive social disciplinary mechanisms but through the timely deployment of defensive software tools. Some asshole blasting violent, graphic language at you? Don’t whine to the authorities about it — hit the @gag command and said asshole’s statements will be blocked from your screen (and only yours). It’s simple, it’s effective, and it censors no one.

