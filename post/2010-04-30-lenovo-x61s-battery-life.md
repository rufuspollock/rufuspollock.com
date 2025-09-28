---
title: >-
  Lenovo X61s Battery Life
slug: lenovo-x61s-battery-life
date: 2010-04-30T20:00:41
themes: []
tags: ['Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 561
---

I have a 2y old Lenovo X61s running ubuntu jaunty. Ever since I acquired I've been rather unimpressed by battery life-time which seems to be max 1.25-1.5h (2h if I've just got it on but not doing anything). This lifetime is achieved when:

  * Switching off wifi, bluetooth, usb etc
  * Switching laptop mode on
  * Turning down backlight to around 30% or below
  * Plus anything else powertop suggests

I should note I'm usually doing some kind of actual work though nothing too intense (if I start running lots of tests that use the DB, or using a browser battery life falls). Under these conditions I can get power usage down to 11-12W though more usual during actual work is 12-14W.

I've finally got around to doing some googling around (I'm thinking of getting another battery) and discovered:

  * There are three battery types for X61s:
     * Thinkpad X6x 4 cell slim line battery    28.8 Watt hours (3 hours @ 9.3 W/hr)
     * Thinkpad X6x 4 cell cylindrical battery  37.4 Watt hours (4 hours @ 9.3 W/hr)
     * Thinkpad X6x 8 cell battery              74.8 Watt hours (8 hours @ 9.3 W/hr)  
  * I almost certainly have 4-cell slimline (least power).
  * According to this [useful thread](http://old.nabble.com/x61s-battery-life-time-td15333975.html) my battery life is poor but within the parameters (in particular 2.5h battery life mentioned seems to depend on power usage around 9.5w)

Based on these calculations and [8-cell battery](http://www-307.ibm.com/pc/support/site.wss/document.do?sitestyle=lenovo&lndocid=MIGR-68026) (409g and around Â£60-[140](http://shop.lenovo.com/SEUILibrary/controller/e/gbweb/LenovoPortal/en_GB/catalog.workflow:item.detail?GroupID=38&Code=40Y7003&current-category-id=D332312ED67F4C719F2B854A4A547854)) should get me around 3h battery time. An improvement but not amazing.

