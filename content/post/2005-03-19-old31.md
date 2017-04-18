---
title: >-
  Limitations of the Human Mind: Insights from Lucasfilm's Habitat
slug: old31
date: 2005-03-19T22:26:52
themes: ['virtual-worlds']
tags: ['Government', 'Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 31
---

<p>
Extracts from <a href="http://www.scara.com/~ole/literatur/LessonsOfHabitat.html">
<em>The Lessons from Lucasfilm's Habitat</em></a>, Chip Morningstar and F. Randall Farmer. A fascinating work which, unusually for computer scientists, is full of lapidary phrases and well-written prose.
</p>

<h3>The Problems of Central Planning (or, the dangers of being a pointy-headed engineer with his control variables)</h3>

<blockquote>
<p>There were two sorts of implementation challenges that Habitat posed. The first was the problem of creating a working piece of technology -- developing the animation engine, the object-oriented virtual memory, the message-passing pseudo operating system, and squeezing them all into the ludicrous Commodore 64 (the backend system also posed interesting technical problems, but its constraints were not as vicious). The second challenge was the creation and management of the Habitat world itself. It is the experiences from the latter exercise that we think will be most relevant to future cyberspace designers.
</p>
<p>
We were initially our own worst enemies in this undertaking, victims of a way of thinking to which we engineers are dangerously susceptible. This way of thinking is characterized by the conceit that all things may be planned in advance and then directly implemented according to the plan's detailed specification. For persons schooled in the design and construction of systems based on simple, well-defined and well-understood foundation principles, this is a natural attitude to have. Moreover, it is entirely appropriate when undertaking most engineering projects. It is a frame of mind that is an essential part of a good engineer's conceptual tool kit. Alas, in keeping with Maslow's assertion that, "to the person who has only a hammer, all the world looks like a nail", it is a tool that is easy to carry beyond its range of applicability. This happens when a system exceeds the threshold of complexity above which the human mind loses its ability to maintain a complete and coherent model.
</p>
</blockquote>

<h3>Engineering Rule #1: Don't trust anyone (because you can't)</h3>

<blockquote>
<p>
If, however, a computer game involves multiple players, delving into the program's internals can enable one to truly cheat, in the sense that one gains an unfair advantage over the other players of which they may be unaware. Habitat is such a multi-player game. When we were designing the software, our "prime directive" was, "The backend shall not assume the validity of anything a player computer tells it." This is because we needed to protect ourselves against the possibility that a clever user had hacked around with his copy of the frontend program to add "custom features". For example, we could not implement any of the sort of "skill and action" elements found in traditional video games wherein dexterity with the joystick determines the outcome of, say, armed combat, because you couldn't guard against someone modifying their copy of the program to tell the backend that they had "hit", whether they actually had or not. Indeed, our partners at QuantumLink warned us of this very eventuality before we even started -- they already had users who did this sort of thing with their regular system. Would anyone actually go to the trouble of disassembling and studying 100K or so of incredibly tight and bizarrely threaded 6502 machine code just to tinker? As it turns out, the answer is yes. People have. We were not 100% rigorous in following our own rule. It turned out that there were a few features whose implementation was greatly eased by breaking the rule in situations where, in our judgment, the consequences would not be material if people "cheated" by hacking their own systems. Darned if people didn't hack their systems to cheat in exactly these ways.
</p>
</blockquote>

<h4>Or they might just exploit your own bugs / features</h4>

<blockquote>
<p>
In order to make this automated economy a little more interesting, each Vendroid had its own prices for the items in it. This was so that we could have local price variation (i.e., a widget would cost a little less if you bought it at Jack's Place instead of The Emporium). It turned out that in two Vendroids across town from each other were two items for sale whose prices we had inadvertently set lower than what a Pawn Machine would buy them back for: Dolls (for sale at 75T, hock for 100T) and Crystal Balls (for sale at 18,000T, hock at 30,000T!). Naturally, a couple of people discovered this. One night they took all their money, walked to the Doll Vendroid, bought as many Dolls as they could, then took them across town and pawned them. By shuttling back and forth between the Doll Vendroid and the Pawn Shop for hours, they amassed sufficient funds to buy a Crystal Ball , whereupon they continued the process with Crystal Balls and a couple orders of magnitude higher cash flow. The final result was at least three Avatars with hundreds of thousands of Tokens each. We only discovered this the next morning when our daily database status report said that the money supply had quintupled overnight.
</p>
</blockquote>

<h3>"Engineering" Rule #2: Keep Reality Consistent by Working Within the System Wherever Possible</h3>

<blockquote>
<p>
One of the more popular events in Habitat took place late in the test, the brainchild of one of the more active players who had recently become a QuantumLink employee. It was called the "Dungeon of Death". For weeks, ads appeared in Habitat's newspaper, The Rant, announcing that that Duo of Dread, DEATH and THE SHADOW, were challenging all comers to enter their lair. Soon, on the outskirts of town, the entrance to a dungeon appeared. Out front was a sign reading, "Danger! Enter at your own risk!" Two system operators were logged in as DEATH and THE SHADOW, armed with specially concocted guns that could kill in one shot, rather than the usual twelve. ...
</p>
<p>
One evening, one of us was given the chance to play the role of DEATH. When we logged in, we found him in one of the dead ends with four other Avatars who were trapped there. We started shooting, as did they. However, the last operator to run DEATH had not bothered to use his special wand to heal any accumulated damage, so the character of DEATH was suddenly and unexpectedly "killed" in the encounter. As we mentioned earlier, when an Avatar is killed, any object in his hands is dropped on the ground. In this case, said object was the special kill-in-one- shot gun, which was immediately picked up by one of the regular players who then made off with it. This gun was not something that regular players were supposed to have. What should we do?
</p>
<p>
It turned out that this was not the first time this had happened. During the previous night's mayhem the special gun was similarly absconded with. In this case, the person playing DEATH was one of the regular system operators, who, accustomed to operating the regular Q-Link service, had simply ordered the player to give the gun back. The player considered that he had obtained the weapon as part of the normal course of the game and balked at this, whereupon the operator threatened to cancel the player's account and kick him off the system if he did not comply. The player gave the gun back, but was quite upset about the whole affair, as were many of his friends and associates on the system. Their world model had been painfully violated.
</p>
<p>
When it happened to us, we played the whole incident within the role of DEATH. We sent a message to the Avatar who had the gun, threatening to come and kill her if she didn't give it back. She replied that all she had to do was stay in town and DEATH couldn't touch her (which was true, if we stayed within the system). OK, we figured, she's smart. We negotiated a deal whereby DEATH would ransom the gun for 10,000 Tokens. An elaborate arrangement was made to meet in the center of town to make the exchange, with a neutral third Avatar acting as an intermediary to ensure that neither party cheated. ...
</p>
<p>
These two very different responses to an ordinary operational problem illustrate our point. Operating within the participants' world model produced a very satisfactory result. On the other hand, taking what seemed like the expedient course, which involved violating the world-model, provoked upset and dismay. Working within the system was clearly the preferred course in this case. 
</p>
</blockquote>

<h3>Conclusion: Decentralize Control to Allow for Evolution (or: don't be a pointy-headed engineer who wants to control everything)

<blockquote>
<p>
In a discussion of cyberspace on Usenet, one worker in the field dismissed ClubCaribe (Habitat's current incarnation) as uninteresting, with a comment to the effect that most of the activity consisted of inane and trivial conversation.Indeed, the observation was largely correct. However, we hope some of the anecdotes recounted above will give some indication that more is going on than those inane and trivial conversations might indicate. Further, to dismiss the system on this basis is to dismiss the users themselves. They are paying money for this service. They don't view what they do as inane and trivial, or they wouldn't do it. To insist this presumes that one knows better than they what they should be doing. Such presumption is another manifestation of the omniscient central planner who dictates all that happens, a role that this entire article is trying to deflect you from seeking. In a real system that is going to be used by real people, it is a mistake to assume that the users will all undertake the sorts of noble and sublime activities which you created the system to enable. Most of them will not. Cyberspace may indeed change humanity, but only if it begins with humanity as it really is.
</p>
</blockquote>

