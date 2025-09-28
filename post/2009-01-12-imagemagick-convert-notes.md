---
title: >-
  Imagemagick convert notes
slug: imagemagick-convert-notes
date: 2009-01-12T12:17:37
themes: []
tags: ['Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 380
---

Helping myself remember how to do common things using imagemagick's (excellent but many-optioned) convert utility.

    convert -scale 10% {in} {out}

    # convert to black and white
    convert -type Grayscale {in} {out}
    convert -monochrome {in} {out}

    # invert colours
    convert -negate in out

    convert -rotate {in} {out} 

    # make the given colour (e.g. here white) transparent
    convert -transparent white {in} {out}
    # make transparent white
    convert -fill white -opaque none {in} {out}

### Make square (for thumbnailing)

    convert -background transparent -gravity center -extent 145x145 file1 file2


