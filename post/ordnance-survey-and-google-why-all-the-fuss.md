---
title: >-
  Ordnance Survey and Google: Why All the Fuss?
slug: ordnance-survey-and-google-why-all-the-fuss
date: 2008-11-20T19:44:36
themes: ['Notebook']
tags: ['Government']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 374
---

Lots of people have been up in arms about a letter sent out by Ordnance Survey about the "Use of Google Maps for display and promotion purposes". With titles like ["Are the Show Us A Better Way winners safe from Ordnance Survey?" (Guardian)](http://www.guardian.co.uk/technology/blog/2008/nov/12/ordnance-survey-google-maps-copyright), ["Home Secretary's crime maps not allowed say Ordnance Survey" (localgov.co.uk)](http://www.localgov.co.uk/index.cfm?method=news.detail&id=73538) or ["The mapping mess - Google v OS" (bbc.co.uk)](http://www.bbc.co.uk/blogs/technology/2008/11/the_mapping_mess_google_v_os.html) these seemed to indicate some particularly unreasonable behaviour by OS.

However, after actually reading the [original OS letter](http://www.freeourdata.org.uk/docs/use-of-google-maps-for-display-and-promotion.pdf) I'm far from convinced. In essence OS say:

  * If you have created the data yourself you can do whatever you like with it including plotting it on Google maps.
  * **However**, if you have *derived* the data from an OS map then you can't. You can't because a) as derived data OS have rights in it b) plotting it on a Google map according to Google's to T&C gives Google a perpetual, royalty-free license to that data. Since, unsurprisingly (and not unreasonably) OS don't want to give Google such a license they don't want you plotting it on a Google map.
  * What the implications of this are then depend heavily on:
    1. Whether Google will change their licensing conditions (at least for their free service)
    2. What *derived* data is

Much of the discussion centred on the last of these items: what is derived data? OS state:

>  Simply put, Ordnance Survey derived data is any data created using Ordnance Survey base
 data. For example, if you capture a polygon or a point or any other feature using any
 Ordnance Survey data, either in its data form or as a background context to the
 polygon/point/other feature capture, this would constitute derived data.
> 
>  It should also be borne in mind that data from other suppliers may be based on Ordnance
 Survey material, and thus the above considerations may still apply. We therefore recommend
 that you verify whether any third-party mapping you use may have been created in some way
 from Ordnance Survey data before displaying it on Google Maps.
> 
> NOTE: Again, the answer to this question is based on our understanding of which of Googleâ€™s
 standard terms and conditions we believe would apply. In the event that Google is prepared to
 offer you terms and conditions which do not involve you purporting to grant Google a licence of
 Ordnance Survey base or derived data, we would have no objection to your hosting such data
 on top of Google Maps in this scenario.

My understanding of this is that if you extract the geodata from an OS map (i.e. polygon, points, features) by some extraction method (such as tracing) then that's derived data and OS can control what you do. This is pretty standard: if I copy text from a book by typing it out longhand I'm still infringing copyright.

However, this does **not** mean if I'm using OS maps as a base-layer and, for example, by clicking at some particular point I generate a lat-long (say to indicate where I live, or where a crime happened) then that lat-long  is 'derived' data.

Now, of course, this could be a fine line: if I happened to click on a bunch of points, say to indicate a walk I went on, and these also showed the route of road there could be debate as to whether I'm infringing the OS rights in the feature or not.

Nevertheless, the basic principle (as I understand it) is clear: geodata created when using OS tools and maps is always yours unless it is directly replicating the underlying OS data. If this interpretation is correct then this whole debate is a bit of a storm in a teacup and projects such as crime-mapping or providing a loofinder aren't at any risk from OS's licensing terms.

