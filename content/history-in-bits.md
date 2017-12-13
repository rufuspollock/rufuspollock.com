---
title: This Information Age
subtitle: A History in Bits of Bits in History
author: Rufus Pollock
date: 2009-02-26
version: v0.1
---

<h1 style="font-size: 130%; font-style: italic;">A History in Bits of Bits in History</h1>

<p style="font-size: 100%; font-style: italic;">The following represents the starting draft of a planned book on the coming of the information age. It was produced over a period of a month and a half in January and February 2009 and then set aside. I hope to return to it. In the mean time I am posting it online in the hope it will prove of value to others.</p>

{{< toc >}}

# Chapter Outline

1. The Information Bit
  * 0 or 1: the binary basics
  * Shannon (post WWII)
  * Morse code
  * Compression and Complexity

2. Content, Code, Databases / Knowledge, Information, Data: It's All the Same to Me
  * What's the distinction?
  * Does it matter: no

3. Information Production Before Digital
  * Oral transmission
  * The Codex
  * Recordings and Films

3. Nonrivaly: What Makes (Digital) Information Special
  * Shoes versus software
  * Distinguish production reproduction and storage (?)

4. Hardware: Software's Shell
  * Software lives definitively in the world of hardware, which, as its name suggests, resides firmly in the physical.
  * It is the technological advances in hardware that make a world of information possible 

5. Bandwidth and MIPS
  * Information has been accumulated, processed and transmitted since the beginning of time. So what's special about the recent past? The answer is scale. For most recorded history the amount of information a person, or a society, could reasonably deal with was extremely limited. In medieval monasteries scholastics might take a lifetime simply to reproduce a few codexes -- albeit in very beautiful form.

6. The Attention Economy
  * Data without attention has little value
  * The increasingly sharp battle for attention
  * Equal or more unequal world

7. The Attention Society
  * Too much
  * Inequality in an online world
  * Virtual worlds
  * Want and Need

8. Complexity and AI
  * Complexity is everywhere (synergy between hardware and software)
  * Too much
  * AI: Beyond man and machine

9. Rules and Regulations, Openness and Intellectual Property: Who Will Own and Control the Digital World

10. Robber Barons or Princes of Light
  * 100 years on from Carnegie Rockefeller
  * Bill Gates, Oracle, ...
  * High fixed, low marginal costs
  * Tipping effects (compatability and standardization)

11. Conclusion: This Information Age

# Introduction

## Beginnings

We live in an information age and we live in a digital age – and these twin aspects of our present existence are mutually intertwined. As the volume and role of information have grown so too have the challenges of managing and handling it. By making information digital – converting it into electronic "bits" – we have made it vastly easier to store, manage, analyze and transfer. The triumph of information therefore depends fundamentally on the triumph of the digital – without the powers of digital technology the current cornocopia of information would be impossible, indeed unthinkable. At the same time digital technology *is* fundamentally information technology. Information processing, storage and transmission are what digital technology does and why it exists. Without the driver of our informational needs the digital age would likely never have been born let alone reach maturity.

Thus, information and the digital are symbiotic: the advance of information necessitates the development of digital technology while that technology makes possible, and encourages, the advance of information. Put simply, information drives digitization and digitization drives information.

This book explores these twin proliferations, examining their interaction and the way in which our present, and future, has been, and is being, shaped by these processes. The revolution in communications that started with Morse and Marconi, and the revolution in processing that started with ENIAC and the transistor of Shockley, is still continuing. Almost exactly 50 years on from the first electronic computers of the Second World War period, the last decades of the twentieth century have witnessed another major development in the simultaneous mass adoption of two distinct but related communication technologies: the Internet/World-Wide-Web and mobile telephony. Suddenly cheap digital communication, and the activities it makes possible, are available on a mass, global, scale.

These changes are not to be seen purely at the social or technological level. Already much of the economy is derived directly, or indirectly from transactions in information. The implications are to be seen from the smallest to the largest levels. Today, at the dawn of the 21st century, many of the most well-known, and most powerful companies in the world base their business on information. Perhaps pre-eminent among them is Google, an entity whose business is built upon the acquisition and analysis of the vast information space that is the web – though interestingly their revenue primarily derives not from selling that information directly but from selling the attention it generates.

We should also not forget software that most fundamental and crucial substance of the information age – being both itself the purest kind of information and, as algorithms made "flesh", the information "machinery" that which manages and processes all other data. What is more, software is now not only one of the largest industries on the planet, but is also ubiquitous in practically every kind of business large or small. In a period of a little over 30 years this industry has given us both Microsoft, the most successful monopolist the world has ever seen, and the peer-produced work of the Free/Open-Source movement.

Here then we have information built upon information, data upon data. It is no wonder that some ask whether these spiralling skyscrapers of the digital age ever touch earth, and, if so, where. Are we fashioning ourselves a heaven or a hell? More prosaically, what do we gain, and what do we lose, as everything that glitters becomes bits? Will knowledge be available to all for the cost of an internet connection or ever more proprietarized and controlled? Will democracy be made good by a world of informed and active citizens, or disintegrate into a million insular and self-reinforcing Babels?

This is a technological, economic and social story. It sprawls out over our history, small at first but growing with such rapidity in the last few decades that, information, and its associated "revolution", are now one of the central elements of our world. So recent, rapid and widespread are these changes, ramifying and filtering into so many diverse aspects of our existence, that it is hard for us to here now to comprehend their scope or predict their future and to do full justice to this subject is a clear impossibility.

Instead, in this work we must take a different route, proceeding by way of survey, allusion and illustration. In short we offer a history in bits of "bits" in history.

## The Nature of Analysis

It is often difficult for us, situated as we are in the midst of events, to accurately discern the general pattern of which they are part.

# "Bits" of Information

## Etymologies

It is perhaps symbolic of the changes of the last century that in 1900 the most common usage of the term "bit" (after it everyday meaning of "small part") was to denote that portion of a bridle that sat in a horse"s mouth. Today it has a quite different meaning: the smallest unit of information, especially in relation to the storage capacity of a computing device. Perhaps nothing then conveys better our passage from that age to this one than this simple change in meaning.

Where then did this modern meaning arise? For in tracing etymology here we may also be able, albeit indirectly, to trace the development not just of a word but of a concept and with it an entire system.

The first occurrence of the term "bit" in published form with its modern meaning appears, rather conveniently, to have occurred in Claude Shannon"s seminal 1948 paper *A Mathematical Theory of Communication*. This was published in the Bell System Technical Journal and is widely considered to be one of *the* seminal papers in the information sciences.

Before coming to Shannon"s paper in more detail a little background is in order. The development of the telegraph and telephony in the 19th century, and particularly the mass adoption of the telephone in the early twentieth, had created the need to find efficient and reliable ways to transmit information, especially human voices, from place to place.[^1]

Animated by this requirement, "communication theorists" had been searching for a way to formally define information. Formalism was important because it would allow precise answers to such questions as: "How much information does this message contain?", or, more relevantly, "How much information has been lost during its transmission?”.

The solution came from statistics and was, crudely, to relate information to unlikelihood (or likelihood) on the basis that the more unlikely something was to occur the more information its actual happening conveyed. For example, if I already know for certain that the sky is blue, then being informed that the sky is blue tells me nothing: no information has been gained. If, however, the sky could be blue or orange then telling me it is blue has genuinely conveyed information – rather little if I was already almost certain it was was blue but a lot if I thought it almost certain to be orange.

Proceeding along these lines, by the time of Shannon"s paper, it had already been established that a measure of information of a message must correspond to the size (or some monotonic function of the size) of the pool of possible messages from which the observed message was drawn – each message being, a priori, equally likely. That is, being told the winner of a ten-horse race in which, a priori, each horse was equally likely to win conveys twice as much "information" as being told the winner of a similar five-horse race.

Furthermore, for a variety of compelling and natural reasons, it was preferable to use the logarithm of the size of the pool rather than the size itself – most obviously a communication system with only one message or symbol is useless since any transmission is known in advance with certainty.[^2] In the simple case where there were only two possible symbols (or outcomes), for example, no/yes, 0/1, or blue/orange, it was natural to use the logarithm to base 2 so that a single observed symbol is 1 unit of information (and N symbols, which corresponds to $2^{N}$ possibilities, contains N units of information). Requiring a term for this unit, Shannon coined the term "bit" or binary digit based on a suggestion of J.W. Tukey.[^3]

Thus, a bit, a binary digit, represents the smallest possible fragment of information. Given that any more complex set of symbols can be represented in terms of (strings of) binary symbols a binary system represents, not only the simplest possible symbol set, but also a comprehensive one, that is, any (discrete) message using any symbolic system can also be expressed as a string of 0s and 1s (or ons and offs etc). Moreover, its basic on/off structure makes it perfectly suited for utilization in a variety of electrical and electronic apparatus, most notably digital storage and computation.

## Being Binary

It is worth digressing here a little further both into the realm of history and theory of symbol systems. First, as it will be important, let us be clear about some minor terminology. "Symbol" here means an *elementary*, i.e. irreducible, symbol – this would correspond to a single character in a standard language.[^4] The set of these elementary symbols form an *alphabet*, which, for a discrete system, will be finite.[^5] Finally, symbols are concatenated together into *strings or messages*.

Now, reflect for a moment on the text that you are reading. It written in a your language, probably *the* – and perhaps the only – symbol system with which most people are familiar.[^6] But, unless you are extremely unusual, this will not be binary system – for example, in English, which is my native language, there are 27 basic characters (26 letters of the alphabet plus space) with another 10 to represent the numbers making a basic total of 37 (and that"s excluding any form of punctuation). Thus, although the binary system may be the most natural from a theoretical point of view, it is noteworthy that almost all human communication systems have alphabets consisting of more than 2 symbols.

Furthermore, this is true not only for human communication systems but of the first electronic communication system: the electric telegraph, developed into functional form in the 1830s and 1840s (the optical telegrpah, based on semaphore had been invented, by Claude Chappe in the 1790s). The electric telegraph used Morse Code, named after Samuel Morse, one the main contributors to the development and commercialization of the invention.[^7] Morse Code, once ubiquitous but today becoming little known, was designed for encoding English. It consisted of four-symbols consisting of dot, dash and the two types of space: a two-dot space between letters, and a three-dot space between words.

What determines these choices? Why does Morse Code have an alphabet with four items rather than two or twenty? Why are no human languages binary based and why do they vary so widely in the size of their alphabets with some consisting of a few tens of symbols but others containing thousands? Fully exploring, let alone answering, such a questions, especially in relation to human languages, would take us rather too far afield. However, we can make some general points.

The starting point of any analysis must be an understanding of three distinct facts. First, that any system of communication (and hence it associated symbolic apparatus) will tend to *efficiency*, whether through design or evolutionary pressures. Second, there is *no single criteria* by which we can measure efficiency but instead a multiplicity factors which will be important – speed, reliability, suitability to the natural or technological medium, etc – and their relative importance may change. Third, that such systems are designed, or evolve, over time, and hence, later modifications are necessarily constrained by earlier ones, either because they build upon those previous changes or out of a requirement for compatability, and hence the ability of a system to be efficient today may be constrained by the adaptations of yesterday.

Returning to the case of Morse Code we note that it was designed for encoding (basic) English over an electrical medium (the telegraph line) where temporal variation was possible and attractive. Thus, in Morse Code, the basic on/off provided by an electrical system was combined with a duration with a dot being a simple "on", a dash being "on" for the duration of 3 dots, a "space" between letters being "off" for the duration of 1 dot, a "space" between words being "off" for the duration of 3 dots, and dots and dashes being separated by an off for the duration of one dot (one can therefore interpret the 2 and 3 dot "spaces" as 1 and 2 dot "spaces" with the basic separator incorporated).

One might wonder why, when already utilizing the basic on/off nature of electrical system,[^8] and so close to the two symbols of basic binary Morse Code stuck with four. The answer likely lies in the fact that the two operators at the end of telegraph line had no way to standardize on a unit of time. Reduced to only two symbols, dot and space (i.e. on and off), and no temporal standardization, it would be very easy to confuse 11 and 101 as these would encode as "dot short-space dot" and "dot short-space space short-space dot". Incorporating a "dash" solves this problem by defining a unit of time (the length of a "dot").

Of course, this is only takes us so far, since with a simple dot and dash Morse Code would again be binary. The addition of the "spaces" to the code corresponding to the space between letters and between words therefore cannot be attributed to necessity but rather to convenience or coincidence. In particular, since oriented to encoding English, dedicated symbols equivalent, at least approximately to the absence on the page or in speech, might assist the original human operators in their task (it is generally found that humans find morse easier to learn and recognize aurally rather than as marks on paper).[^9] This benefit of having explicit spaces was all the greater because Morse code did not use fixed length "strings" of dots and dashes for each English character but instead varied the length of the encoding with the approximate frequency of that character in English, that is shorter sequences for the more common letters and longer sequences for the less common: ...

What motivated this decision to use differential length encoding? The answer lies in another, and for our story, very important form of efficiency: *efficiency of encoding*, encoding being the process of converting a message from one symbol system to another, for example from English to Morse code (the reverse process is termed *decoding*). An efficient encoding is one which, averaged over the possible input strings, results in the shortest possible output, and hence in the efficient, i.e. minimal, utilization of bandwidth, i.e. the transmission channel"s capacity.

Note that this correspondence between minimal strings and minimal bandwidth depends on the assumption that each symbol is of equal in "size" (i.e. uses an equal amount of channel capacity). Usually this is true by definition: each elementary symbol in a symbol system is equivalent of any other. However, matters may be a little confusing when the technology itself performs another encoding. For example, with Morse Code encoding efficiency is formally evaluated with respect to the number of symbols used (i.e. each distinct symbol counting as one unit), but we may be as, or even more, interested in the amount of actual time taken to transmit the message (which would take account of the fact that each Morse symbol is itself encoded down to electrical on/offs of different lengths). Thus, in may the case that "formal" efficiency of a symbol system differs substantially from its "actual" efficiency. Again this points to the fact that features of the technological, natural or human environment in which the symbol system is utilized are central to any understanding the system"s development and characteristics.

This concept of (formal) encoding efficiency is not only important in itself but also conveniently brings us back to the work of Shannon. It was Shannon again who formalized the concept of encoding, proved precise bounds on its efficiency and showed that efficiency is attainable.[^10] The key to the encoding theorem, and associated results, was the generalization of the previously discussed concept of information to what is known as entropy.[^11]

With information/entropy suitably defined the encoding theorem is almost self-evident, stating, in essence, that the output and the input contain the same amount of *information*. Slightly more formally, if my input source has, on average, H units of information/entropy per symbol (of its symbol system), and the output has G units of information per symbol (in its symbol system) then the best possible encoding results in using H/G symbols of the output: the input had N symbols, hence the message contained N times H bits of information in total, and so the output must contain N times H bits of information and therefore requires at least N times H divided by G output symbols.

Putting this another way suppose, on average, a 100 symbol source message becomes 10 symbols of output after encoding. Then, it would be natural to say that a compression ratio of 0.1 had been achieved (or a compression *rate* of 10). Put this way, the ratio H/G also gives us the maximum possible compression ratio – and conversely, if we didn"t know what H/G was, then achieved compression ratios put upper bounds on H/G. It is worth unpacking this a little further. Recall that the informational bit was defined so that if we had N equally likely outcomes then the associated amount of information was \(log_{2}(N)\) bits – and hence a single binary digit (0or a 1) has one bit of information.

Thus, a symbol system with a binary alphabet, and no restriction on the forms of its messages (so each message is equally likely), has 1 bit of information per symbol.[^12] Consider another symbol system, for example English, which uses the Roman alphabet of 27 symbols. Assuming these were equally likely, per our definition of information, we know this has around four and a half bits per symbol (\(log_{2}(27)\)) – equivalently we would require an average of four and a half 0s and 1s to represent all of the symbols in this alphabet. Thus, one factor affecting the encoding of a message in one symbol system to another is the relative sizes of their respective alphabets. Specifically, pure alphabet effects should account for a compression affect equal to \(log_{2}\) of the relative alphabet sizes.

This factor, being so obvious, is not very interesting. So much so that it would be best to ignore it entirely by focusing on the case where the alphabets remain of the same size – or, when the alphabets are of different sizes, by normalizing the compression ratio to take this fact into account.[^13] Assuming this is so is any compression possible? After all we are encoding between two systems with the same size alphabets. Consider, the following example of an encoding of a sentence in English:

> th qck brwn fx jmpd ovr th lzy dg

Most English speakers should, almost without effort, be able to *decode* this back into its original form: "the quick brown fox jumped over the lazy dog”. Observe that although the encoded sentence used the Roman alphabet and although it was no longer "English" it was perfectly comprehensible (the encoding method should also be obvious: omission of every vowel from the original). Assume for a moment that this encoding was always uniquely decipherable, that is any encoded message can be unambiguously decoded back to its source.[^14] What compression rate would this achieve? Averaged across a wide set of texts, vowels account for approximately 32% of the 27 basic characters (letters plus space). Hence, *on average*, the encoded version would be 68% of the size of the input (our example, being a pangram or holaphabetic sentence, that is a sentence including every letter at least once, fares rather worse only achieving compression to 77% of the original size).

In fact, estimates by Shannon and other authors suggest that English text, at least in bulk, can be compressed substantially further, to somewhere between 30% and 60% of its original size (a compression ratio of between 1.7 and 3.3). Put another way, the *redundancy* of English, is between 40 and 70%, that is there is an encoding such that the output has 40-70% fewer symbols than the input. Redundancy is a measure of how much space is being "wasted" in the average message, that is, how many symbols are being used above the minimum necessary to convey the information present.[^15] That is, to return to the starting point of this discussion, redundancy is a measure of *(in)efficiency*: a redundancy of 0 means that no "space" (symbols) are being wasted, a redundancy of 0.5 means 50% of space is being wasted, and a redundancy of 1 means all space is being wasted. Wasted "space" equates to unnecessary symbols and therefore use of transmission or storage capacity above that actually necessary.

Observe that the inefficiency of redundancy results from structure, i.e. patterns, in the symbol system. By exploiting and eliminating these patterns redundancy can be reduced. To take a very simple example: suppose we have a binary system in which 0s and 1s always occurs in pairs, so messages look like 110011... or 111100..., then one can exploit this fact by replacing every pair of 0s and 1s by a single 0 or 1 thereby halving the size of the message. Or consider Morse Code, which exploited the pattern English letter frequencies in order to achieve compression by using shorter sequences for more common letters.[^16] Conversely, the "structure" in Morse Code, in that a letter or word space must be followed by a dot or dash, increases its redundancy and reduces its efficient utilization of bandwidth – though, as noted earlier, to the benefit of increased comprehensibility to its human users.[^17]

It might seem odd that systems with more *structure* are more redundant and hence convey *less* information. After all, we normally think of highly structured objects as conveying a lot of information – compare a picture made of randomly drawn dots with a face, or a house with the "building" constructed by laying bricks on top of each other at random! This intuition is entirely correct and agrees with, rather than contradicts, what we have just been saying. The point is that, within the space of all drawings or all buildings, those with structure are very unusual. Now, as explained earlier, the more unlikely something is to occur (ex ante) the more information actually observing it conveys (ex post). Thus highly structured or patterned objects do indeed convey a lot of information. However, if it was known a priori that this structure was always present this would no longer be true, and the redundancy that the structure introduced would equate to wasted space.

This has some interesting implications. For example, suppose we have some encoding that achieves perfect compression for our symbol system, which for concreteness we can think of as English text (with a length limit of, say a million words). Perfect compression means no redundancy and so must imply that encoded messages are distributed perfectly uniformly at all levels (first-order, second-order etc). So, there must be just as many \`e"s as \`z"s, just as many \`ui"s as \`qv"s etc. Hence encoded output would be indistinguishable from randomness. Furthermore, every string of letters in the output system must correspond to an input message – otherwise there would be wasted space. Consider then the effect of an error in recording one letter of the output, for example the replacement of "a" with "b". Since every encoded string corresponded to one original input string this error wouldn"t be detectable: the encoded message would be valid and would still decode to some valid input message. Thus, a single letter transposition of the encoded message may mean that what was originally *War and Peace* is decoded as *Gone with the Wind*, or "Do not launch nuclear strike" becomes "Mary had a little lamb, Its fleece was white as snow".[^18]

In practical terms this is something of a problem. Very few storage or transmission media are entirely error free: wind, weather and the general vicissitudes of history have worn away parts of the black stele on which Hammurabi"s code is inscribed, while the magnetic hard disks of today are subject to their own "thermal instabilities" which lead to the random flipping of bits.

Perfect efficiency then, in the sense of zero redundancy, is unlikely to be an attractive quality in a symbol system as it makes it extremely vulnerable to error. Once again, we therefore find ourselves with a trade-off, this time of efficiency with robustness to error in transmission or processing. Since error, or "noise", is such a familiar part of any real-world system it is not surprising that robustness ranks high among the attributes such systems should possess – often higher than efficiency. It is also not surprising that this matter was also treated by Shannon in his seminal paper where he provided an elegant and powerful result linking the form of noise to the maximal "error-free" encoding rate for a source.

However, this is not the place to delve further into these matters. We have now travelled far enough into the territory of pure information and its associated theory and we have visited some of our key themes, in particular the way in which the information systems of the past and present are formed by the interplay of a variety of competing forces and constraints – technological, social, economic and physical – while simultaneously helping to shape those same forces and constraints. These are themes will remain with us throughout this work, weaving through the tapestry of event and explanation, sometimes obvious, sometimes hidden, but always important in holding it together.

## Appendix: Information, Entropy and Shannon"s Coding Theorem

First, recall the definition of information was related to outcomes that were equiprobable. For example, if we had N possible messages, all equally likely, then the amount of information was the logarithm to the base 2 of N bits. Now, it would be useful to consider cases where symbols, or strings of symbols, were not all equally probable.

# Going Digital

## Introduction: This Information Age

It was no coincidence that Shannon"s work emerged around the mid-point of the twentieth century and almost simultaneously with the development of the first computers, for the demand for both developments arose from the same source: the increasing technological and social complexity of modern societies. This was a moment when there was a need for informational capacity and processing of a new order – be it for designing atomic bombs or calculating the national income accounts required for Keynesian demand management.[^19]

It is therefore not unreasonable for us to select this instant as the beginning of our information age – even if, as with all such designations we know that such an attribution is made in retrospect with the knowledge of what came after. Of course, it is hard, if not impossible, to ever definitively to establish the precise beginning of any era. Informational growth was not new and even considering the rate of growth it is difficult to establish any clear break. Technological advances related to information recording, transmission and processing are almost as old as humanity itself, and the pace of developments in this area – like most others – had undoubtedly been quickening since the industrial revolution with major information-related inventions such as the telegraph (1840s), the typewriter (1870s), punched-card tabulators (1880s), wireless telegraphy (1890s) etc. But this is no great surprise, very little in the stream of history arises suddenly ex nihilo, and this especially true when, as here, we concern ourselves with structures and tendencies.

There is, moreover, one other important and compelling reason, to choose this moment rather than any other: it is also the beginning of (electronic) computers, and therefore, the beginning of the digital revolution which forms the other half of our narrative. For it is digitization that has made possible the informational developments or the last half-century – though as we have just noted, such flows are always two ways: informational demands drive technological developments including those in digital computing and communications.

As already noted, computing and communications in themselves are not modern inventions. However, what is modern is the development and production of *machines* capable of performing these tasks, especially machines that were "digital". "Digital" devices are those which deal only with a finite, discrete, set of symbols or values while "analogue" devices are those that deal with infinite, continuous ones. For example, a digital computer will store and manipulate only symbols from some discrete finite alphabet – usually binary – while an analogue computer will store and manipulate continuous quantities such as voltage.[^20] [^21] Or an analogue phone system will transmit the original (analogue) voice into a analogue signal – for example, a voltage – while a digital system will "discretize" the signal into a finite set of values represented in some finite, discrete alphabet. Similarly an analogue sound storage device, such as a LP record will encode the original analogue signal into an analogue "groove" on a piece of vinyl while a digital system, such as a Compact Disc, will discretize the sound and then store it in that discretized form – in the case of a CD in binary form represented by the presence or absence of a very small "hole" in the surface of the disc.

Strictly speaking digital devices need not be *electronic* ones, and there are many examples of mechanical or electro-mechanical devices stretching back into the nineteenth century to Babbage and beyond. However, when we speak of "digitization" we mean a move to devices that were both digital and electronic. This is not just a semantic point but a practical one. As we shall see below, while *digital* computation occurred prior to the move to electronics, it was electronics which made possible the vast developments in speed, power and flexibility in information handling that have been hallmarks of the information era. Thus, when we speak of "Going Digital" we are intending a less precise and more common-place meaning that encompasses the twin processes of digitalization and electronization.

## Before the Electronic Computer

Computers, in the most general sense of devices that carry out "computations", i.e. the automated the processing of information, are almost as old as humanity itself. For example, early astronomical clocks or even the simple abacus could, with this definition, be argued to be computing devices. It is therefore useful to extend this definition somewhat to include not only the requirement of automated processing but that of "programmability", that is the ability for the device to change the computations it carries out in response to input. Almost all the early devices lack this programmability – they would carry one kind of computation and one kind of computation only. For example, the calculating machine designed by Wilhelm Schickard in 1623 though supporting addition and multiplication of numbers up to six digits – and therefore arguably the first "calculator" ever conceived – could not be reprogrammed to do anything else.[^22]

To find the first device whose combination of the two key "features" of computation and programmability was sufficient to merit the term "computer" we must move forward three centuries to Charles Babbage"s "Analytical Engine" (dated to 1837). Despite never being completed, it is generally agreed that Babbage"s design was the first example of a fully programmable calculator: a computer.[^23] Of course, like the machines of his predecessors, the "Analytical Engine" was entirely mechanical but its marriage of programmability and automated computation are sufficient to have merited Babbage"s designation as the forefather of modern computing.

Given this, it is somewhat ironic that Babbage"s design had almost no influence on subsequent efforts, and most importantly, on the development of the modern electronic computers whose descendants we use today – not least because Babbage"s technical designs were never published.[^24] In fact it can even be argued that Babbage"s work, because of their ultimate failure, were a significant obstacle to progress because their effect on the efforts of others. For example, in the 1840s a self-taught Devonshire bookseller and printer Thomas Fowler developed a digital calculating device based on ternary arithmetic which appears, at least in retrospect, to have held out great promise, perhaps even exceeding the "analytical engine". However it failed to receive any funding from the British Government because of their early misadventures with Babbage"s machines.[^25] That said, Babbage"s example, and the implications from his work that a "computer" was possible, were an important inspirational influence on many, though by no means all, of the later pioneers.[^26]

In recording these advances it is interesting once again to place them in context by considering the motivations and technologies that underlay their development. In most of the early cases the increasing computational demands of "scientific research", especially in astronomy, played a central role. For example, Al-Jazari"s "castle clock" of 1206 (the first recorded analogue calculator) was designed for providing astronomical information (the zodiac, solar and lunar orbits) while Schickhard"s efforts were directly intended to assist Kepler"s astronomical calculations. While this is scientific research it is very much "applied science". This is not surprising since the need for explicit numerical calculations is a hallmark of such work.

Kepler and Schickard, alive in the early 17th century, are part of the dawn of modern science. As science and engineering developed the calculational needs only barely felt by them would grow substantially. Again it seems no coincidence that the slide-rule, based on John Napier"s discovery of logarithms, was invented by William Oughtred, Edmund Wingate and others, almost exactly contebased with Schickard"s work on his calculator.

By the time of Babbage, the industrial revolution was in full swing and the demands of both of practice and of research had dramatically increased the demand for numerical computations. It is therefore no surprise that Babbage"s "Difference Engine" was expressly intended to assist in the automated calculation of mathematical tables (especially logarithms) which were of ever increasing importance both in "pure research" (Babbage after all was Lucasian Professor of Mathematics at Cambridge) and in practice. Furthermore, the mechanical sophistication of Babbage"s machine was such that it could only have been considered implmentable with the advent of industrialization and the associated dramatic improvements in mechanical technology (and reductions in cost).

Of course neither of Babbage"s proposed machines were ever built in part because of continual cost overruns! Georg Scheutz, a Swedish printer and inventor, together with his son Edvard did succeed in building a mechanical calculator in the 1840s and 1850s based on Babbage"s designs for the Difference Engine. Unfortunately, like many inventor-entrepreneurs both Georg and Edvard died bankdrupt, after managing to sell only two machines, one to Dudley observatory in Albany New York (where it went unused) and one to the General Register Office in London for the production of the 1864 Life Table (where though used it proved unsatisfactory due to its unreliability).[^27]

The fact that the one working usage of a Babbage designed machine was for the production of a statistical tables is not a coincidental one for our story. It it points the direction that developments would now take, away from the realm of science, whether pure and applied, and into the realm of information processing, a move from the production of mathematical tables to the calculation of statistical tables based on data provided by the user.

## Statistics and the Modern State

Again passing silently over intervening developments we move forward to the 1880s and change continents to the United States. The United States had introduced a census in 18XX, following the practice of other countries such as England (Census introduced in 1801) and Sweden (introduced in XXX). Analyzing the mass of data in the Census was done by hand. With the rapidly increasing population of the United States the Census bureau found itself stretched. The 1860 Census had taken XX years to tabulate the census and the 1870 Census had taken YY years. On this basis there were serious concerns that the 1880 census would not be fully tabulated before the 1890 census began a decade later. This was clearly an issue. Automation of the process was considered and YY was done. Herman Hollerith YY

# Conclusion

Could societies as complex as ours survive without the capacities for information storage and processing that digital technologies permit? The answer is surely no.

Moreover, the very availability of these technologies encourage the collection and storage of ever more data, a process that threatens, if not already achieving, information overload for ourselves and our societies. The increasingly complex technological, social and economic systems built with the assistance of these information technologies while delivering unimagined benefits have also created great fragility.

Just as ecosystems in adapting ever more perfectly to current conditions make themselves more vulnerable to shocks we must wonder at the robustness of our current informational adaptations which are now so fundamental to the functioning of so many key systems that support large parts of our existence, not only in the developed world but increasingly in the developing as well. It is noteworthy that the period since the dawn of the information age has seen no major conflict between world powers. How well will our complex machines cope if such a conflict were to occur with all its attendant disruption and destruction?

[^1]: Almost all of the early contributions to the field appeared in *Bell* System Technical Journal, Bell Telephone Laboratories being the research division of AT&T (the regulated monopoly which operated US telephone services for most of the twentieth century).

[^2]: TODO: (?) additional reasons. Discuss yes, no etc. To be clear explain why repetitions increase the message space above one.

[^3]: p.1: "The choice of a logarithmic base corresponds to the choice of a unit for measuring information. If the base 2 is used the resulting units may be called binary digits, or more briefly bits, a word suggested by J. W. Tukey.”

[^4]: This helps us distinguish from the other potential meanings of symbol including the representation, metaphorical or physical, of a concept.

[^5]: Classic examples of continuous, non-discrete systems, would include an alphabet based on continous variables such as the pitch of sounds or the voltage in a wire, and having every distinct value count as a distinct symbol.

[^6]: There is, of course, a distinction between a language as spoken and as written. Spoken language, via a variety of methods: intonation, phrasing, pauses, etc, frequently conveys much more than its written equivalent (though it is also marked by much greater redundancy in the form of repetitions, temporizing ums etc). One might even go so far as to claim that much of the function of spoken language, that of emotional interaction and "grooming", is performed by these additional aspects rather than by the words themselves – written text conveys itself, but with speech the text may be but a small part of the message. However, in order to keep matters simple, when discussing human languages we shall imagine these as represented by their written forms.

[^7]: Traditionally it was Morse who was credited with the invention of Morse Code though today his partner Alfred Vail also receives credit. It is also true that Morse"s original code was refined somewhat over time. TODO: more here on this.

[^8]: Though it is worth noting that the independently invented eletrical telegrahg of William Cooke and Charles Wheatstone in England, which like Morse and Valil"s also used electrical transmission and electromagnetic receivers, used a needle pointer to indicate the alphabetic character being sent.

[^9]: Initially, transmissions were recorded as dots and dashes on tape with these tapes then decoded by operators. However, it was rapidly discovered that operators could utilize the tapping sound of the stylus to decode directly rather than by reading the tape.

[^10]: Or almost attainable, that is within an arbitrarily small deficiency.

[^11]: For discussion of this generalization see the Appendix to this chapter.

[^12]: As we shall discuss a few paragraphs on, if all message strings are not equally likely then the information content will be lower. Thus 1 bit per symbol is an upper bound, and this is true generally: a symbol system with an alphabet of size N has at most $log_{2}(N)$ bits of information per symbol.

[^13]: This would be done by dividing the compression ratio by the $\(log_{2}\frac{\textrm{Dest Alphabet Size}}{\textrm{Source Alphabet Size}}$.

[^14]: It should be obvious that this is, in fact, not so. For example, "quack" and "quick" both encode to "qck".

[^15]: Formally, redundancy is defined as $1 - \frac{\textrm{average information per symbol}}{\log(\textrm{size of alphabet})}$. Recall that for any symbol system the maximum achievable information per symbol is $\log(\textrm{Size of the alphabet})$. Thus the fraction is the compression ratio for the best possible encoding of that symbol system using symbols from the same alphabet.

[^16]: Interestingly, Morse, with no immediate access to tabulations of English word frequencies, based his estimates by examing the size of the type boxes kept by printers for each letter.

[^17]: TODO: give info on channel capacity and encoding efficiency of Morse Code. Peirce 1961.

[^18]: It may seem improbable that a single letter of transposition could result in such vast changes upon decoding. After all surely things "close" in their original form, the first edition versus the second edition of War and Peace, would remain "close" when encoded and vice-versa. Unfortunately, our encoding is perfect and hence no exploitable pattern can remain in the set of encoded messages taken as a whole – in fact, as already mentioned, the distribution of encoded messages must be random in a very uniform way. This would not be possible if we were to require that encoding preserve "closeness" and so there cannot be anything but a random relation between "closeness" in the original version and the encoded version.

[^19]: Talk about Kuznets work in the US and Stone et al in the UK. There were no modern GDP indicators until the 1930s ...

[^20]: Of course all electrical computers, digital or analogue, require electricity at some voltage in order to function. However, digital computers do not compute using the voltage or the electricity but simply use the electricity for power.

[^21]: Thanks to quantum theory it might be possible to answer that all natural quantities, including e.g. voltage, are necessarily "quantized" and therefore actually discrete. While perhaps technically true the number of possible values for such quantities is still vastly larger (even if finite) then for any digital one and so the basic distinction remains.

[^22]: Unfortunately the design was never constructed as a half-built implementation intended for delivery to Kepler was destroyed by fire on February 21 1624 and a replacement was never built (see Schickard"s letter to Kepler dated Feb 24 1624, a transcription of which may be found on http://www.thocp.net/biographies/schickard_wilhelm.html). The first working calculators that we know of were the "Pascaline" (1645) of Blaise Pascal and the "Stepped Reckoner" (1694) of Leibniz both of which, unlike Schikard"s device, were actually manufactured and used. TODO: insert ref

[^23]: Babbage also designed a "difference engine" which was intended for the computation of logarithms and other astronomical and mathematical tables. The difference engine lacked programmability and therefore was not a "computer" in our sense of the word. As with the analytical engine Babbage never succeeded in constructing the difference engine (he was notoriously difficult to work with), though machines based on his designs were constructed by others.

[^24]: See <http://www.computerhistory.org/core/charlesbabbage/> (retrieved 2009-05-07) and citations therein.

[^25]: See also the quotation in (p. 180) from L.J. Comrie that "this dark age in computing machinery, that lasted 100 years, was due to the colossal failure of Charles Babbage.”

[^26]: Most notably, Howard Aiken, one of the main figures behind the Harvard Mark I.

[^27]: <http://www.computerhistory.org/babbage/georgedvardscheutz/>

