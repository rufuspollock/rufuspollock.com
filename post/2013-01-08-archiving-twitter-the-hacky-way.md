---
title: >-
  Archiving Twitter the Hacky Way
slug: archiving-twitter-the-hacky-way
date: 2013-01-08T08:00:00
themes: []
tags: ['Tech']
projects: ['Open Knowledge']
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 1249
---

<p>There are many circumstances where you want to archive a tweets - maybe just from your own account or perhaps for a hashtag for an event or topic.</p>

<p>Unfortunately Twitter search queries do not give data more than 7 days old and for a given account you can only get approximately the last 3200 of your tweets and 800 items from your timeline. [Update: People have pointed out that <a href="http://blog.twitter.com/2012/12/your-twitter-archive.html">Twitter released a feature to download an archive of your personal tweets at the end of December</a> - this, of course, still doesn’t help with queries or hashtags]</p>

<p>Thus, if you want to archive twitter you’ll need to come up with another solution (or pay them, or a reseller, a bunch of money - see Appendix below!). Sadly, most of the online solutions have tended to disappear or be acquired over time (e.g. twapperkeeper). So a DIY solution would be attractive. After reading various proposals on the web I’ve found the following to work pretty well (but see also this <a href="http://mashe.hawksey.info/2012/01/twitter-archive-tagsv3/">excellent google spreadsheet based solution</a>).</p>

<p>The proposed process involves 3 steps:</p>

<ol>
  <li>Locate the Twitter Atom Feed for your Search</li>
  <li>Use Google Reader as your Archiver</li>
  <li>Get your data out of Google Reader (a 1000 items at a time!)</li>
</ol>

<p>One current drawback of this solution is that each stage has to be done by hand. It could be possible to automate more of this, and especially the important third step, if I could work out how to do more with the <a href="http://undoc.in/">Google Reader API</a>. Contributions or suggestions here would be very welcome!</p>

<p><strong><em>Note that the above method will become obsolete as of March 5 2013 when <a href="https://dev.twitter.com/docs/api/1.1/overview#New_Twitter_client_policies">Twitter close down RSS and Atom feeds</a> - continuing their long march to becoming a <del>fully</del> more closed and controlled ecosystem.</em></strong></p>

<p><strong><em>As you struggle, like me, to get precious archival information out of Twitter it may be worth reflecting on just how much information you’ve given to Twitter that you are now unable to retrieve (at least without paying) …</em></strong></p>

<h2 id="twitter-atom-feed">Twitter Atom Feed</h2>

<p>Twitter still have Atom feeds for their search queries:</p>

<p><a href="http://search.twitter.com/search.atom?q=my_search">http://search.twitter.com/search.atom?q=my_search</a></p>

<p>Note that if you want to search for a hash tag like #OpenData or a user e.g. @someone you’ll need to escape the symbols:</p>

<p><a href="http://search.twitter.com/search.atom?q=%23OpenData">http://search.twitter.com/search.atom?q=%23OpenData</a></p>

<p>Unfortunately twitter atom queries are limited to only a few items (around 20) so we’ll need to continuously archive that feed to get full coverage.</p>

<h2 id="archiving-in-google-reader">Archiving in Google Reader</h2>

<p>Just add the previous feed URL in your Google Reader account. It will then start archiving.</p>

<p>Aside: because the twitter atom feed is limited to a small number of items and the check in google reader only happens every 3 hours (1h if someone else is archiving the same feed) you can miss a lot of tweets. One option could be to use Topsy’s RSS feeds <a href="http://otter.topsy.com/searchdate.rss?q=%23okfn">http://otter.topsy.com/searchdate.rss?q=%23okfn</a> (though not clear how to get more items from this feed either!)</p>

<h2 id="gettting-data-out-of-google-reader">Gettting Data out of Google Reader</h2>

<p>Google Reader offers a decent (though still beta) API. Unoffical docs for it can be found here: <a href="http://undoc.in/">http://undoc.in/</a></p>

<p>The key URL we need is:</p>

<p><a href="http://www.google.com/reader/atom/feed/%5Bfeed_address%5D?n=1000">http://www.google.com/reader/atom/feed/[feed_address]?n=1000</a></p>

<p>Note that the feed is limited to a maximum of 1000 items and you can only access it for your account if you are logged in. This means:</p>

<ul>
  <li>If you have more than a 1000 items you need to find the continuation token in each set of results and then at &amp;c={continuation-token} to your query.</li>
  <li>Because you need to be logged in your browser you need to do this by hand :-( (it may be possible to automate via the API but I couldn’t get anything work - any tips much appreciated!)</li>
</ul>

<p>Here’s a concrete example (note, as you need to be logged in this won’t work for you):</p>

<p><a href="http://www.google.com/reader/atom/feed/http://search.twitter.com/search.atom%3Fq%3D%2523OpenData?n=1000">http://www.google.com/reader/atom/feed/http://search.twitter.com/search.atom%3Fq%3D%2523OpenData?n=1000</a></p>

<p>And that’s it! You should now have a local archive of all your tweets!</p>

<h2 id="appendix">Appendix</h2>

<p>Increasing Twitter is selling access to the full Twitter archive and there are a variety of 3rd services (such as Gnip, DataSift, Topsy <a href="https://dev.twitter.com/programs/twitter-certified-products/products#Data">and possibly more</a>) who are offering full or partial access for a fee.</p>



