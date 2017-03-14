---
title: >-
  Set Trackpad Sensitivity for Thinkpad on Ubuntu
slug: set-trackpad-sensitivity-for-thinkpad-on-ubuntu
date: 2010-07-11T00:07:47
themes: []
tags: [u'Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 617
---

On a Lenovo Thinkpad the trackpad is the red button that acts as a mouse. To set the sensistivity and speed of your trackpad on for ubuntu/debian linux do (as root):
   
    echo -n 180 > /sys/devices/platform/i8042/serio1/speed
    echo -n 250 > /sys/devices/platform/i8042/serio1/sensitivity

To have these applied every time you user the computer (probably what you want!) just add those two lines to `/etc/rc.local` before the final exit 0 so results looks like:

<pre><code>
echo -n 180 > /sys/devices/platform/i8042/serio1/speed
echo -n 250 > /sys/devices/platform/i8042/serio1/sensitivity

exit 0
</code></pre>


