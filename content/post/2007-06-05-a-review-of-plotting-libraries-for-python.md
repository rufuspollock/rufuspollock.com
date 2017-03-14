---
title: >-
  A Review of Plotting Libraries for Python
slug: a-review-of-plotting-libraries-for-python
date: 2007-06-05T14:59:40
themes: []
tags: [u'Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 184
---

An (ongoing) summary of my experience with some of the utilities available for plotting from a python perspective.

Last updated: 2008-03-06

### Ploticus

  * (+) Fast, powerful, mature, well-documented
  * (-) Not python based

C-based rather than python-based but fast and powerful. There is a (fairly crude) set of python bindings available here: <http://www.srcc.lsu.edu/~davids/ploticus_module.html>. Alternatively one can just call the ploticus command from a python script.

### Matplotlib

  * (+) Fairly powerful, mature, well-documented, nice pure python API
  * (-) A little slow; requires a backend to be installed (so installation on a server is a problem)
  * Could support object-orientation better

### PyChart

<http://home.gna.org/pychart/>
  
  * (+) Pure python, quite simple to use, good documentation
  * (-) Not quite as nice looking or as powerful as e.g. ploticus

### Biggles

<http://biggles.sourceforge.net/>

  * last updated: 2004-03-08
  * looks fine but does not seem to be actively developed any longer

#### Example

See: <http://home.gna.org/pychart/examples/index.html>. This is the bar/line example from there:

<img src="http://home.gna.org/pychart/examples/barline-small.png" alt="bar/line chart" />

    from pychart import *
    theme.get_options()

    data = [(10, 20, 30), (20, 65, 33),
        (30, 55, 30), (40, 45, 51),
        (50, 25, 27), (60, 75, 30)]

    ar = area.T(size = (150,120),
                y_grid_interval=10,
                x_axis=axis.X(label="X label", label_offset=(0,-7)),
                y_axis=axis.Y(label="Y label"),
                legend = legend.T(), y_range = (0, None))

    ar.add_plot(bar_plot.T(label="foo", data=data),
                line_plot.T(label="bar", data=data, ycol=2))
    ar.draw()


