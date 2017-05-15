---
title: >-
  Open Knowledge
slug: open-knowledge
date: 2005-12-24T17:47:08
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - page_id: 61
---

## Random Thoughts and Random Links

### Macauley on Patent Extensions

Here is Lord Macauley (successfully) opposing an extension of copyright term from 28 to 60 years in the 1840s:

> 'It is good that authors should be remunerated, and at least exceptionable way of remunerating them is by a monopoly. Yet monopoly is evil. For the sake of the good we must submit to the evil: but the evil ought not to last a day longer than is necessary for the purpose of securing the good'
>
> ....
>
> 'Dr Johnson died 56 years ago. If the law were what my honourable and learned friend wishes to make it, somebody would now have the monopoly of Dr Johnson's works. Who that somebody would be, it is impossible to say: but we may venture to guess. I guess, then, that it would have been some bookseller, who was the assignee of antoher bookseller, who was the grandson son a third bookseller, who had bought the copyright from Black Frank, the Doctor's servant and residuary legatee in 1785 and 1786. Now, would the knowledge that this copyright would exist in 1841 have been a source of grtification to Johnson? Would it have stimulated his exertions? Woudl it have once drawn him out of his bed before noon? Would it have cheered him in a fit of spleen? Would it have induced hime to give us one more allegory, one more life of a poet, one more imitation of Juvenal? I firmly believe not.'

### Watt on Not Inventing

Taken from Merges and Nelson 1990: Complex Econ of Patent Scope n.141:

> The transition from entrepreneur to established, cautious firm can be breathtakingly fast. An historian who studied the beginning of the electrical lighting industry in the U.S. pointed out that in ten years, Thomas Edison moved from a maverick trying to get incandescent lighting accepted as feasible to a staunch opponent of the "dangerous" innovation of alternating current. H. Passer, The Electrical Manufacturers 1875-1900, at 174 (1953). The same phenomenon has been noted repeatedly. See, e.g., Scherer, Invention and Innovation in the Watt-Boulton Steam-Engine Venture, 6 Tech. & Culture 165, 174 (1965), quoting a letter from James Watt, inventor of the steam engine, to his partner James Boulton:
>
> **On the whole I find it is now full time to cease attempting to invent new things, or to attempt anything which is attended with any risk of not succeeding . . . . Let us go on executing the things we understand, and leave the rest to younger men, who have neither money nor character to lose.** (emphasis added)

## Open Source Software Economics

### Why Open Source Works

A brief summary of economic reasons why open source works, i.e. why it manages to, at least partially, overcome the provision of public good problem (why doesn't everyone free ride and none of the good gets provided)

  * humans do not engage in many activities solely because of financial reward. Much of open source software is produced by people in their spare time because they enjoy 'hacking' and creating things. There is also the important status system that rewards good work. (Note that these points hold a fortiori for many intellectual and academic endeavours.)

  * institutions exist that can provide funding for 'public' good projects. In particular most governments are very significant purchasers of software and can support open source in its role as a public good

  * Complementarity between software and services. In software product and services (installation, maintenance, upgrades, customization etc) often go together. Frequently the services are more valuable, and costly, than the actual product. Thus it often makes senses to open source the product and make money on the consulting.

  * Improved quality of open source software (see below)

  * less lock-in for customers, fewer overheads and more flexibility (you can always fork)

  * ability to solve the 'commons problem' with respect to a public good. In case of software (also holds for knowledge) often have the very useful property that system can be improved very incrementally (bugfixes, plugins). This means, /purely on a selfish basis/ the cost of an improvement may be less than benefit for an /individual/ user and hence they will make that improvement. But then of course the rest of the community gets that fix for free exploiting the non-rival nature of information goods.

## Biblio

1. 'Open and Closed Systems are Equivalent (that is, in an ideal world)'
  * http://www.cl.cam.ac.uk/ftp/users/rja14/toulousebook.pdf
  * develops the analysis of open versus closed systems and shows that while the two are equivalent in an ideal world, there are many factors that can break symmetry and cause one or the other to be better in practice.
2. 'Simple Economics of Open Source'
 * http://papers.ssrn.com/sol3/papers.cfm?abstract_id=224008
 * Lerner and Tirole 2002
3. Discussion of Software Patents that provides a simple overview of the theory of patent IP:
  * http://www.okfn.org/wiki/IntellectualPropertyIssues

## Copyright

### Biblio

 * http://www.copyrighthistory.com/

## Statistics on Information Production

### Books

  * Google for: book publishing statistics
  * http://parapub.com/statistics/
  * Author's Guild Report (supported by OSI) (2000): http://www.authorsguild.org/miscfiles/midlist.pdf
    * Very good with a lot of stats (though spread throughout text) however '''no sources''' explicitly referenced
    * p. 41: stats on distribution of sales across books
      * sales break down into front-list (in stock less than a year) and back-list (the rest).
      * 30% sales from front-list. 20% of that revenue comes from only 100 books. Next 20% from 6,0000 titles.
      * 70% from back-list. 20% revenue from top 500 titles. next 20% from 25,000 titles.
      * 'At B&N and Borders the vast majority of the titles in stock sell fewer than two copies a year.'
  * You can get sales rank data (and maybe price) from amazon's web api:
   * http://www.amazon.com/gp/aws/sdk/main.html?s=AWSEcommerceService&v=4-0&p=PgDatamodelOverview
   * zuckerman's html crude html interface: http://h2odev.law.harvard.edu/ezuckerman/amform.html
  * nielsen bookscan:
   * can get very basic data from the Bookseller yearbook
   * their own data they don't give out even for academic use (and apparently the whole database would cost a 'seven figure sum' for 'technical reasons' (it is so complex to run the sql queries apparently)
