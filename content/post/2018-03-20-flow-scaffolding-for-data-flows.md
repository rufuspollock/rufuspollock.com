---
title: "Flow: a Tool for Scaffolding Data Flows"
date: 2018-03-20
themes: ["Data Systems"]
posttype: notebook
featured: no
tags: ["ideas"]
---

*This post outlines an idea for a tool that I've been thinking about for a while.*

**UPDATE: working sketch of the tool here https://github.com/datopian/dataflow-demo**

Flow is a scaffolding tool for quickly building data flows.

Think of it as the zen of data engineering that can start small and scale big.

Flow allows you to build data processing flows quickly using existing tools on your laptop. If you later want to deploy these Flow makes that easy too.

Analogy: think of flow as the missing convention for laying out your webapp on disk. Not much but a great start.

Aside: we could go even simpler and start with a pattern. (What are examples of that e.g. semantic versioning, or git flow or ...). There are then tools that support that pattern.

## Pattern

Principles

* Use Data Package specs as the minimal metadata wrapper data to enable passing data between processors (specifically tabular data apackage)
* Each step can be cleanly separated and data cached between steps
* The simplest flows are linear.
* Reason logically but support asynchronous execution behind the scenes
* Use pandas (?)
* Use singer taps

TODO: metaphor of the factory vs metaphor of the pipes. Data Assembly Lines vs Data Pipes.

```
Flask       Flow

Werkzeug => Pandas
Flask    => Flow (the minimal wrapper that stitches the stages together)
```

### What does it look like?

RETL = retrieve, extract, transform, load ...

What does it look like.

```python
# process.py

url = 'http://example.com/the-data.csv'
local = 'cache/the-data.csv'

def retrieve()
    '''Get the data from the url and cache it.'''
    urllib.urlretrieve(url, local)

def extract_and_transform():
    # load the csv, standardize ... tidy ...

def load()
    # in this case save to disk, but you might load to a DB etc
    ...

def run():
    retrieve()
    extract_and_transform()
    load()
```

## Usage

`flow ...`
