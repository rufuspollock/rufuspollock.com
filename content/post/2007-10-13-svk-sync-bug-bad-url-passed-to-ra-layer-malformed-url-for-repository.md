---
title: >-
  svk Sync Bug "Bad URL passed to RA layer: Malformed URL for repository"
slug: svk-sync-bug-bad-url-passed-to-ra-layer-malformed-url-for-repository
date: 2007-10-13T12:02:44
themes: []
tags: [u'Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 229
---

I record briefly my experience resolving this issue in case it helps others. As background I note that I use svk to allow local commit and replay for some of the subversion repos I use and over the last week I'd started encountering problems when trying to svk sync on one of these receiving the following error message:

    Bad URL passed to RA layer: Malformed URL for repository

The solution to this is the following patch provided by [Peter Werner](http://0x.hu) to the svk-devel list a few days ago:

    -------------- next part --------------
    --- SVN-Mirror-0.73.orig/lib/SVN/Mirror/Ra.pm 2007-03-19 23:59:12.000000000 +0100
    +++ SVN-Mirror-0.73/lib/SVN/Mirror/Ra.pm  2007-10-07 08:37:36.000000000 +0200
    @@ -168,6 +168,9 @@
         $self->{config} ||= SVN::Core::config_get_config(undef, $self->{pool});
         $self->{auth} ||= $self->_new_auth;
     
    +    # escape URI (% is already escaped)
    +    $arg{'url'} =~ s/([^-_:.%\/a-zA-Z0-9])/sprintf("%%%02X", ord($1))/eg if defined $arg{'url'};
    +
         SVN::Ra->new( url => $self->{rsource},
          auth => $self->{auth},
          config => $self->{config},

In addition to this solution below I report the process by which I discovered it. I do this as it provides an interesting case study of the way that open source communities work, and particularly how 'user-driven bug-fixing' happens.

  1. Searching on the web turned up a variety of earlier reports [1][2][3] of this issue which it seemed related to having a spaces in svn url names (see [1.1] and [2] in particular). This seemed plausible as a source of the error as it occurred after someone had added a directory with spaces in it to the repository (a very rare occurrence).
  2. This issue did not seem to occur for all users and CLK (the maintainer) suggested upgrading SVN::Mirror to 0.73. [2.1]
  3. This I did but the bug was still there (as other users had noted [2.2]) however the source now seemed to be pinpointed as being in the SVN::Mirror perl module. Unfortunately I'm not a perl hacker ...
  4. Finally a hand search of the svk lists turned up a post from less than a week ago [4] (obviously too recent for Google to have picked up yet as I had earlier done a specific search for the error name over the svk lists ...). In addition to reporting the problem this mail provided a 2 liner patch to a specific perl module. I applied this patch, tried svk sync and hey presto! the bug was gone.

The issue progressed from an unconfirmed one whose aetiology was unclear [1], to a confirmed one whose cause was fairly well known [2] (though not its source in code), solutions were suggested and tested by users [2.1, 2.2], the issue remained unresolved for several more months with the fix eventually provided by an independent user to the list [4].

It is also especially noteworthy that much of this tracking down was only possible because the software involved was open enabling users to poke around to see what was wrong. For example, tying the bug to spaces in the underlying repository url resulted from the original reporter of the issue hand-modifying a svn source file so as to make the error message more verbose [1.1] -- something which is clearly only possible if the code is open.


  * [1]:<http://lists.bestpractical.com/pipermail/svk-devel/2007-January/000570.html>
  * [1.1]:<http://lists.bestpractical.com/pipermail/svk-devel/2007-January/000571.html>
  * [2]: <http://lists.bestpractical.com/pipermail/svk-devel/2007-March/000755.html>
  * [2.1]: <http://lists.bestpractical.com/pipermail/svk-devel/2007-March/000757.html>
  * [2.2]: <http://lists.bestpractical.com/pipermail/svk-devel/2007-March/000766.html>
  * [3]: <http://lists.bestpractical.com/pipermail/svk-devel/2007-June/000944.html>
  * [4]: <http://lists.bestpractical.com/pipermail/svk-devel/2007-October/001065.html>


