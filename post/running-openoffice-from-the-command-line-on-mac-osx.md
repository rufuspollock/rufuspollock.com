---
title: >-
  Running OpenOffice from the Command Line on Mac OSX
slug: running-openoffice-from-the-command-line-on-mac-osx
date: 2007-08-12T20:43:46
themes: []
tags: ['Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 206
---

This is a simple hack to enable you to start OpenOffice and, more importantly, open documents with it from the command line. I've got the standard X port of OpenOffice 2.0 installed, so if you have something different you may need to change the path to soffice given below (to find soffice on your machine try from the command line $ locate soffice):

First let's make the script that starts openoffice available in a convenient way e.g. by symlinking into ~/bin or /usr/bin:

     $ cd ~/bin
     $ ln -s /Applications/OpenOffice.org\ 2.0.app/Contents/openoffice.org/program/soffice ./

Now you can do stuff like:

     $ soffice -help

You'll see there are different switches which allow you to start a text document, a spreadsheet etc. One annoyance to note is that if you get soffice to load a file by doing:

    $ soffice [options] ${filename}

The application it will use (writer, calc, math ...) will depend solely on the extension of the filename and will ignore any options you give it. So e.g. if you do:

    $ soffice -writer some.csv

Then this will load in calc even though the -writer option was given. For more details (on this very old bug) see:

http://www.openoffice.org/servlets/ReadMsg?list=allbugs&msgNo=94354

Fortunately this isn't too much of a problem since the extension mapping is pretty reasonable.

