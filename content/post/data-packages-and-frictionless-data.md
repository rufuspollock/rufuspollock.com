---  
title: Data Packages and Frictionless Data - Submission to Knight Foundation Call on 'Making Data Work For Individuals and Communities'
slug: data-packages-and-frictionless-data-submission-to-knight-foundation
date: 2015-09-27
---  

Datopian's submission to the Knight Foundation open call for ideas on how to make data work for individuals and communities. The submission describes Datopian's work on Data Packages and Frictionless Data.

## Knight Foundation Mission

Knight Foundation supports transformational ideas that promote quality journalism, advance media innovation, engage communities and foster the arts. We believe that democracy thrives when people and communities are informed and engaged.

## Brief

This is an open call for ideas.

Data is the basic building block of information. In an increasingly data-rich world we see new opportunities for people to interact with data and technology in ways that improve society.

For this challenge, we want to discover ideas that use data for good--that inform and empower people to make decisions about their lives, their communities, and democracy. We believe that data can unlock useful information and that information is key to stronger, more knowledgeable communities.

New technologies and the open data movement have put data in the hands of more people, giving rise to both challenges and opportunities. We want projects that use data to fuel innovation and new ideas, while protecting the rights of individuals and communities. We’re not prescriptive in our approach; we welcome all kinds of ideas, from new ways to collect, analyze, present, interpret and share data, to better journalism and data-enhanced storytelling techniques, to ways to promote transparency, security and privacy.

This challenge is open to anyone, from journalists, startups, civic hackers and academics, to media organizations, businesses, nonprofits, governments and individuals.

So how might we make data work for individuals and communities? From Sept. 8 to Sept. 30, we invite you to submit your idea to win a share of $3 million, which we’ll award in January 2016. After the challenge closes, participants will have the opportunity to refine their submissions and we will review every entry we receive, with the help of a team of outside advisers. We also encourage you to share your reactions to the ideas you see here on http://newschallenge.org.

## Datopian Submission

### Title

Data Packages and Frictionless Data

### Describe your contribution in one sentence.

We’re creating a set of standards, tooling, and software integrations to remove the friction of getting, sharing, and processing data.

In other words, a lightweight specification and tooling for “packaging” data and automating “transport” between users.

### Describe your idea in more detail.

Defining standards for generically packaging data (e.g. Tabular Data Package, JSON Table Schema) will make it easier for individuals (who may necessarily be data scientists) to effectively use data.

Data Packages are a lightweight "packaging" format for data that provide a basis for convenient delivery, installation and management of datasets--they offer functionality similar to "packaging" in software and "containerization" in shipping: a simple wrapper and basic structure for transportation of data that significantly reduces the friction in data sharing and integration, supports automation and does this without imposing major changes on the underlying data being packaged.

### Full description

The core of the proposal is developing “Data Package”, its suite of tools and integrations, and, perhaps most importantly, building awareness and buy-in around the approach in research.

We have developed--and will continue to refine--a simple, lightweight specification for packaging data and especially tabular data. A key aspect of this specification is that it aligns with tools people use in ordinary work (e.g. Excel) and will require few or no changes to existing data and data structures.

The specification also provides a simple, easy way to create schemas for tabular data, again, in a way that requires no changes to existing data. (We emphasize that the proposal is not about actually creating those schemas--which is up to specific user communities to define to fit their needs).

The specification is quite mature having been under development for several years. We take a IETF RFC style approach of “rough consensus and running code” placing a huge emphasis on tooling that implements or utilises the specification--rather than just having a “standard” done.

Tooling and Integration is a major focus of the proposal. It is key that there is both tooling for standard operations but also that there is excellent integration into existing tools and platforms--we usually cannot expect users to adopt new tools or platforms when they already have perfectly good ones.

Our focus then is to develop tooling, libraries and integrations that support the key operations around data packages, such as:

* Creation: creating data packages quickly and easily--and doing so from inside existing tools (from Excel and Google Spreadsheets to R and Relational Databases)

* Validation: easily check that data conforms to a given schema

* Import: automated/one-click

### Publication and Discovery

Publication: putting data packages online using tools that everyday researchers are familiar with from Dropbox to Google Drive to Wordpress to S3.

Discovery: a simple central registry and a toolkit for creating your own registry (in hours).

Use and adoption are ultimately the only measure of success for this kind of work. As such, work to do outreach, develop communities and run pilots will be absolutely central. Work will include:

* Documentation: providing excellent documentation including guides and training materials

* Running and participating in events for key user groups

* General outreach through blogging, social media, training and evangelism

* Running targeted pilots with selected partner organisations and groups to trial and use the tools and specifications. These will be key as they can act as demonstrators to build wider adoption in target user communities

### Briefly describe the need you're trying to address

There is very significant friction around the acquisition, sharing and reuse of data. Data may be hard to find, “closed” or otherwise restricted in use. Often structure is poor and may not use a standardized schema, necessitating significant manipulation to be usable. With poor data quality, extensive time must be spent manually transferring data from one tool to another. 

The focus of this proposal is technical. Based on working both with researchers and government for more than a decade on the issues surrounding data sharing and use, we have identified a specific subproblem which is both significant and tractable. Our laser focus is on alleviating friction in one major area: the technical process of preparing and sharing data--that is, having data go from one person’s tool (Excel, Stata, a database) to another person’s tool as quickly and as easily as possible. The data can be open or closed: what we propose will assist whether you are sharing within a small group of collaborators or publishing your data to the whole world.

Specifically, in this proposal we focus on the development and adoption of a lightweight specification and associated tooling for “packaging” (tabular) data and transporting it easily and efficiently from one tool, or one user, to another. The approach is titled “Data Package” because our work has close analogy with “containerization” in shipping and “packaging” in software.

Within logistics, containerization only addressed one specific problem: loading and unloading cargo from ships. It did not deal with exactly how cargo got from a given port to its ultimate destination or even from its source factory onto the ship--and it certainly did not deal with the actual production or consumption of the goods it helped transport. Similarly, the Data Package proposal focuses on key “onload” and “offload” steps--getting data out of one tool and into another, and from one researcher to another. Similar to the “packaging” that happens both in shipping and software, it seeks to standardize, simplify and automate these processes.

It is worth pursuing the analogy a little further. We have pointed out that containerization does not have an impact directly on production--it transports cars or iPhones but it does not help make them. And the same is true for “data packages”--they will not help do the household survey or collect the air samples. However, containerization does have an impact indirectly: since complex production often involves combining multiple components--an iPhone’s final assembly will put together components made elsewhere (screen, memory, case etc)--by making it easier to source those components together in one place, containerization can make production more efficient, or even possible.

We also see an analogy with software. Software packaging makes it easier to reliably pull together different libraries and combine together to make new libraries and applications. This analogy holds for data: right now, the bulk of all data-driven research involves combining together multiple datasets. This process is still frequently manual and error-prone. “Data packages” could allow for the automation of much of this: we imagine a future similar to software, where standard “data packages” are automatically downloaded and “installed” into your statistics program (for example, your analysis may require country codes, GDP, inflation etc). Rather than hand downloading them, copying them into a central spreadsheet, tweaking etc (as we once did with software libraries too!), these should be “data packages” and be automatically installable from their authoritative source directly in your tool of your choice.

### What progress have you made so far?

Substantial initial work has already been done on the core specifications and tooling. We have also seen adoption, primarily in government and civic tech. The best summary of progress on “core” work can be found in the online roadmap: http://data.okfn.org/roadmap. There are now first pass on core libraries in several major languages including R, Python, Ruby and Node and growing awareness and use of the specifications and tooling.

### Key points

The basic specifications have now been in development for several years and are mature and well tested. There is some remaining work, for example to submit to the IETF RFC process, but this is relatively minimal.

Data Package: http://dataprotocols.org/data-packages/

Tabular Data Package: http://dataprotocols.org/tabular-data-package/

JSON Table Schema: http://dataprotocols.org/json-table-schema/

Tooling both produced both by Open Knowledge and others has been growing rapidly. There are now core libraries in several major languages including R, Python, Ruby and Node (though there is some variation in their completeness). There are several online validation and creation services, etc. See http://data.okfn.org/tools/ for details.

There is growing awareness and use of the specifications and tooling. For example, there has been production use in government, discussion with national statistics offices, and support from funders. 

Some examples:

The UK government have been using JSON Table Schema and Tabular Data Package tools as part of their publication process for spend data. (See Appendix for one specific example)

The US government (data.gov) have been examining JSON Table Schema for use in data validation.

Several local government entities have used JSON Table Schema and Tabular Data Package for managing and validating data.

A significant number of people have created Data Packages themselves as well as tools that manage Data Packages--these have included governments, researchers and individual data wranglers. The exact number is difficult to know as people are not obliged to register their data packages or tools but so far we have seen at least a dozen tools and hundreds of data packages created by third parties.

### What would be a successful outcome for your project?

A working suite of efficient tools that make it easy to import and export data packages from one individual to the next, one community to the next.

### Please list your team members and their relevant experience/skills.

#### The team

Dr. Rufus Pollock, Founder and President of Open Knowledge. A leading global figure in open data and data sharing and has worked with governments and research institutions on these issues for more than a decade.

Paul Walsh is an experienced Technical Project Manager and Senior Developer with experience working on a range of projects such as Open Data Index, Open Data Handbook, Spend Publishing Dashboard, OpenSpending, and Frictionless Data. As the Technical Lead of OpenSpending, Paul manages the architecture and specification work for the all upcoming versions. Paul holds a BA with Honours in Anthropology from the University of Western Australia, and has 9 years commercial experience working in startups in the highly competitive Israeli Hi-Tech industry. He also has several years experience as a volunteer and contractor working with open data and open source communities at the Israeli NGO The Public Knowledge Workshop, where he lead development of a platform for the open publication of municipal budgets in Israel.

Sander van der Waal, Projects Director at Open Knowledge. Sander oversees projects in the various areas of open knowledge, including Open Government Data, Open Access to research and Open Data for Development. Sander has extensive experience developing and sustaining connections across the diverse set of communities that constitute the global Open Knowledge network and works ensure that open data projects have a positive impact on the world. Sander is a computer scientist and philosopher with a many years experience in the open source world, having advised academic projects on open source software development at OSS Watch at Oxford University and contributed to projects at the Apache Software Foundation.

Daniel Fowler contributes to various projects at Open Knowledge and currently serves as an Open Knowledge Labs lead helping build a community of makers and doers around open data. He has a Master’s degree in Information and Communication Technologies for Development from Royal Holloway, University of London and a Bachelor’s degree in Psychology from Princeton University. Between degrees, he worked for several years as a system administrator for an investment bank in New York City.

### Location

Global, online.