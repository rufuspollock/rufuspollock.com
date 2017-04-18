---
title: >-
  External Monitors with Ubuntu and Intel GMA X3100 integrated graphics
slug: external-monitors-with-ubuntu-and-intel-gma-x3100-integrated-graphics
date: 2008-02-13T23:14:27
themes: []
tags: ['Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 271
---

I recently took delivery of a Novatech X40r system (Novatech are one of the few suppliers who allow me to get a machine without Windows). The most recent version of Ubuntu (Gutsy) installed without any issues -- though I couldn't quite seem to get the display resolution to match the screen resolution. Next step was to plug in my external monitor: nothing happened. This post quickly details how I got this fixed. Most of it is derived from an [excellent post in the ubuntu forums [1]][1] and this [freedesktop bug post [2]][2]. It is important to note that this may be specific to the graphic card being used: Intel GMA X3100 integrated graphics.

[1]: http://ubuntuforums.org/showpost.php?p=4003194&postcount=584
[2]: http://bugs.freedesktop.org/show_bug.cgi?id=12229

[1] <http://ubuntuforums.org/showpost.php?p=4003194&postcount=584>  
[2] <http://bugs.freedesktop.org/show_bug.cgi?id=12229>

### Instructions

For most part just follow the excellent instructions in [1]. Details of where these needed to be modded can be found below:

STEP 1:  my output from xrandr -q in step 1 was

<pre><code>
$ xrandr -q
Screen 0: minimum 320 x 200, current 1280 x 800, maximum 1280 x 1280
VGA disconnected (normal left inverted right)
LVDS connected 1280x800+0+0 (normal left inverted right) 304mm x 190mm
   1280x800       59.9*+   60.0  
   1280x768       60.0  
   1024x768       60.0  
   800x600        60.3  
   640x480        59.9  
TV connected 1024x768+0+0 (normal left inverted right) 0mm x 0mm
   1024x768       30.0* 
   800x600        30.0  
   848x480        30.0  
   640x480        30.0  
</code></pre>

As one can see there is this spurious TV entry. For the time being ignore this and proceed through the next steps.

STEP 3: In step 3 nothing happened immediately and on manual activation I received an error:

<pre><code>
$ xrandr --output VGA --auto
xrandr: cannot find crtc for output VGA
</code></pre>

My xrandr -q output was:

<pre><code>
$ xrandr -q
Screen 0: minimum 320 x 200, current 1280 x 800, maximum 1280 x 1280
VGA connected (normal left inverted right)
   1280x1024      59.9  
   1024x768       59.9  
   800x600        59.9     56.2  
   640x480        60.0  
LVDS connected 1280x800+0+0 (normal left inverted right) 304mm x 190mm
   1280x800       59.9*+   60.0  
   1280x768       60.0  
   1024x768       60.0  
   800x600        60.3  
   640x480        59.9  
TV connected 1024x768+0+0 (normal left inverted right) 0mm x 0mm
   1024x768       30.0* 
   800x600        30.0  
   848x480        30.0  
   640x480        30.0  
</code></pre>

As one can see the new monitor is detected. After some Googling I came across [2]. This suggested there might be some conflict between the spurious TV entry and new monitor (essentially it appears the auto-detection code on some newish chipsets generates false-positives for the existence of a TV-out and this conflicts with activating additional monitors). I therefore did:

     $ xrandr --output TV --off

Having done this activation of the new monitor worked:

     $ xrandr --output VGA --auto

Even better the incorrect match of the display resolution to the screen resolution on the laptop went away suggesting that the existence of the TV item was also affecting the LVDS display.


