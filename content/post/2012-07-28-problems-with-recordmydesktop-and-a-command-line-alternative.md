---
title: >-
  Problems with RecordMyDesktop and a Command Line Alternative
slug: problems-with-recordmydesktop-and-a-command-line-alternative
date: 2012-07-28T16:46:35
themes: []
tags: ['Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1203
---

I have been trying to create screencasts using RecordMyDesktop on Ubuntu. While the app itself functioned well I had a serious problem with the image quality: switching windows seemed to lead to massive diagonal pixelation of the captured images rendering the screencast useless.

I played around for a while with various RecordMyDesktop settings (frame rate, full capture etc) but to no avail. Some searching on the web brought me to [this forum post](http://forums.pcpitstop.com/index.php?/topic/198340-gtk-record-my-desktop-pixelation/) which appeared to describe an exactly similar problem -- the screenshot in the original question was almost identical in pixellation effect to what I was seeing. (Aside: interestingly the user says there problem arose after they installed compiz so that may be part of the cause ...)

While the forum did not have a resolution for RecordMyDesktop it did provide a working ffmpeg command line command that worked **perfectly**:

    ffmpeg -f alsa -itsoffset 00:00:02.000 -ac 2 -i hw:0,0 -f x11grab -s $(xwininfo -root | grep 'geometry' | awk '{print $2;}') -r 15 -i :0.0 -sameq -f avi -s wvga -y screencast.avi

