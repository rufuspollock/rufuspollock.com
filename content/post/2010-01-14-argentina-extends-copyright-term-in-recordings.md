---
title: >-
  Argentina Extends Copyright Term in Recordings
slug: argentina-extends-copyright-term-in-recordings
date: 2010-01-14T17:54:00
themes: ['Information Economy']
tags: ['Government']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 475
---

Apparently, on the 11th of December 2009, Argentina extended copyright term in recordings from 50 to 70 years (see e.g. [here](http://www.ip-watch.org/weblog/2009/12/23/argentina-toughens-music-performers-and-producers-protection/), [here][billboard] and [here][zeropaid]).

[zeropaid]: http://www.zeropaid.com/news/87460/argentina-extends-copyright-protection-term-by-20yrs-2/
[billboard]: http://www.billboard.biz/bbbiz/content_display/industry/e3i35216ec6c2433321c54b63d4cc30bb31

Instead of the real reasons for extension -- propping up the profits of a handful of multinational record labels and their shareholders (at the expense of everyone else) -- the usual disingenuous justifications were once again being trotted out by music industry representatives.

First up was (all quotes from the [billboard article](billboard)):

## The investment argument

> "I would like to thank all those who supported this new law which will benefit the music community in Argentina," tango master Leopoldo Federico, president of AADI, said in a statement. "**It will improve incentives to invest in future recordings** and also helps older performers who had faced losing their rights just when they need them the most."
>
> ...
>
> John Kennedy, chairman and chief executive of IFPI, also welcomed the legislation. "I am delighted that Argentina has strengthened the rights of performers and producers by extending the term of protection," he said in a statement. "Argentina has a strong musical heritage and this reform means that **producers will have a greater incentive to invest in the next generation of local talent.**"

But wait a moment: "producers" are already getting 50 years of monopoly protection. How much extra incentive are those 20 extra years going to provide?

Let's do some simple calculations.

First off remember this is about incentives, which means it is about expected payoffs at the point of investment, i.e. when the recording is created. As such we should be dealing with ["present value"](http://en.wikipedia.org/wiki/Present_value) figures, i.e. total revenue in "today's terms".

To work out the the effect of an extension then we need an idea for a) what future sales look like relative today (the cultural decay rate) and b) a way of putting future revenue in today's term (the discount rate). The industry's [own analysis](http://www.ipo.gov.uk/report-termextension.pdf) (commissioned for the Gowers review in the UK) used a nominal discount rate of 12.3% (pre-tax) and cultural decay rates of 3-20% (in nominal terms it appears). Let's be generous and take the lowest possible cultural decay rate of 3%. Combined with the 12.3% discount rate this means that, ***on average,*** **revenue is dropping at a substantial 14.3%**!

Running this through a bit of basic maths (and I mean really basic -- code inline below) we find that the 20 year extension will deliver a **tiny 0.08% increase in revenues**. Even halving the nominal discount rate to a very low figure like 6% only pushes up the revenue gain to just over 1% (1.1%). For those who like things visually here's a picture:

<img src="http://www.rufuspollock.org/wp-content/uploads/2010/01/revenue_impact.png" alt="revenue_impact" title="revenue_impact" class="display" />

**Aside:** Of course there will be a lot of variation from the average -- note that the relevant variation is *not* between hits and duds (as these may experience exactly the same decay!) but between records which go on selling at a reasonably steady rate and those which fade away fairly quickly. However, an "investor", such as a record label, tends to "invest" in a whole "portfolio" of records precisely in order to reduce this "risky" variability (and in any case greater risk implies a higher discount rate assuming the investor is risk averse). As such the average revenue increase is precisely what an "investor" will use when making decisions such as how many recordings to fund.

Next up was:

## The pension for performers argument

> "I would like to thank all those who supported this new law which will benefit the music community in Argentina," tango master Leopoldo Federico, president of AADI, said in a statement. "It will improve incentives to invest in future recordings and also helps **older performers who had faced losing their rights just when they need them the most.**"

But life expectancy in Argentina is [75 years](http://www.google.co.uk/search?q=life+expectancy+argentina) -- and is probably shorter for most performers who are old today. So, unless a performer is especially prolific in their teens, 50 years of copyright monopoly is already enough to cover them in their old(er) age.

And anyway haven't performers heard about pensions or saving for the future -- everyone else has. I don't expect the plumber I pay today to fix by sink to come back in 50 years asking for additional payment for a pension plan! Instead I expect the plumber to save some of the income received today to use in retirement.

Moreover, as the calculations above should make clear, copyright income 50+ years in the future from recordings today is likely (on average) to be tiny (0.08% of the revenue received during the first 50 years!). As such there is no way the average performer could rely on income from a 20 year term extension 50 years in the future to support them in their old age. Just like everyone else they will need to **save** some of the income during that first 50 years.

**Aside:** in fact it is is more like 10 years or even 5 years, as for most recordings, the vast majority of the revenue they will ever generate will come in the first 5 or 10 years after release.

Last up we had:

## The cultural argument

> Javier DelupÃ­, CAPIF's executive director, added: "This new law is good news for Argentine culture. It promotes the creation of new music and safeguards the rights of performers and producers both here and abroad."

But:

  * The investment argument is completely invalid (see above) and hence there won't be any "promoting the creation of new music".
  * In fact, to the contrary, the extension will impede the creation of new works by reducing the public domain on which all creators can and do build.
  * Moreover, an extension transfers money to (older and already successful) performers away from younger and less well-known ones.
  * Depending on how comparison of terms is implemented an extension actually harms the balance of payments of the enacting country (e.g. the UK looses out from a term extension in recordings)

So, no, **term extensions aren't good for (Argentine) culture** -- though they may be good for CAPIF (Representando a la Industria Argentina de la MÃºsica).

## Conclusion

**It's time we start calling a spade a spade: this term extension is a simple, and highly inefficient, subsidy to the major record labels plus, perhaps, a few, already highly successful, performers, which is paid for by the general populace.**

If it can command widespread assent in that form, then, fine, let it pass! But I sincerely doubt the likelihood of this occurrence. If this is so, then **the passage of such bills, is nothing more or less than a straightforward ["robbery upon the public"](http://www.rufuspollock.org/2009/09/22/talk-at-atrip-conference-how-long-should-copyright-last/)** -- in the 150 year-old words of Henry Warburton, radical opponent of the UK's term extension of the 1840s.

## Colophon

Here's the python script used for the revenue calculations above, together with the code to generate the figure.

    #!/usr/bin/env python
    def extra_revenue(term, extension, decay, irate):
        dfactor = 1/(1+decay+irate)
        def geometric(df, NN):
            return (1-df**(NN+1))/(1-df)
        total = geometric(dfactor, term)
        textension = dfactor**term * geometric(dfactor, extension)
        increase = textension/total
        print('Term, Extension, decay, irate: %s %s %s %s' % (term, extension,
            decay, irate))
        print('Percentage increase: %s' % (100*increase))

    extra_revenue(50, 20, 0.03, 0.123)
    extra_revenue(50, 20, 0.05, 0.123)
    extra_revenue(50, 20, 0.03, 0.06)
    extra_revenue(50, 20, 0.04, 0.06)

    import math
    def visualize():
        import matplotlib.pyplot as pyplot
        # normalize main square to 10x10 = 100
        pyplot.bar(0, 10, width=10, fc='red', alpha=0.6)
        edge = math.sqrt(0.08)
        pyplot.bar(14, edge, width=edge, bottom=5, align='center', fc='blue', alpha=0.6)

        pyplot.bar(14, 1, width=1, bottom=1, align='center', fc='blue', alpha=0.6)

        pyplot.figtext(0.15, 0.7, 'Present Value of Revenue\nUnder Existing\n50y Term', multialignment='center', va='top')
        pyplot.figtext(0.65, 0.7, 'PV of Extra Revenue\nfrom 20y Extension',
                multialignment='center', va='top')
        pyplot.figtext(0.7, 0.4, '1% of Existing\n Revenue',
                multialignment='center', va='top')

        # hack to get rid of axes ...
        ax = pyplot.gca()
        ax.set_frame_on(False)
        pyplot.yticks([],[])
        pyplot.xticks([],[])

        fig = pyplot.figure(1)
        fig.set_size_inches(5, 3)
        pyplot.savefig('revenue_impact.png')

    visualize()
    print('Saved image to disk')


