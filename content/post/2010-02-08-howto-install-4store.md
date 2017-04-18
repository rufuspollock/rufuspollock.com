---
title: >-
  Howto Install 4store
slug: howto-install-4store
date: 2010-02-08T13:20:46
themes: []
tags: ['Books', 'Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 554
---

My experiences (with the assistance of Will Waites) of installing [4store][] On Ubuntu Jaunty.

[4store]: http://4store.org/

No packaged versions of code (there is one in fact from Yves Raimond from mid 2009 but now out of date ...), so need to get from github.

Recommend using [will waites fork](http://github.com/wwaites/4store) which adds useful features like:

  * multiple connections
  * triple deletion

Note I had to make various fixes to get this to compile on my ubuntu machine. See diff below.

Install standard ubuntu/debian dependencies:

  * See 4store wiki
  * rasqal needs to be latest version
    * Get it
    * ./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var
    * make, make install
  * Now install

Now to start a DB:

  * 4s-backend-setup {db-name}
  * 4s-backend {db-name}

Now for the python bindings also created by will waites and which can be found [here](http://github.com/wwaites/py4s)

  * On my Jaunty needed to convert size_t to int everywhere
  * Needed to run with latest cython (v0.12) installed via pip/easy_install
  * To run tests need backend db called py4s_test (harcoded)

To run multiple backends at once you will probably need to have avahi dev libraries (not sure which!).

### Diff for wwaites 4store fork (updated diff as of 2010-04-28)

<pre><code style="font-size: 0.7em;">
diff --git a/src/backend/Makefile b/src/backend/Makefile
index 51a957c..e64eb13 100644
--- a/src/backend/Makefile
+++ b/src/backend/Makefile
@@ -2,7 +2,7 @@ include ../discovery.mk
 include ../rev.mk
 include ../darwin.mk
 
-CFLAGS = -Wall -Wstrict-prototypes -Werror -g -std=gnu99 -O2 -I.. -DGIT_REV=\"$(gitrev)\" `pkg-config --cflags raptor glib-2.0`
+CFLAGS = -Wall -Wstrict-prototypes -g -std=gnu99 -O2 -I.. -DGIT_REV=\"$(gitrev)\" `pkg-config --cflags raptor glib-2.0`
 LDFLAGS = $(ldfdarwin) $(ldflinux) -lz `pkg-config --libs raptor glib-2.0 $(avahi)`
 
 LIB_OBJS = chain.o bucket.o list.o tlist.o rhash.o mhash.o sort.o \
diff --git a/src/common/Makefile b/src/common/Makefile
index 9b33e94..60cd04f 100644
--- a/src/common/Makefile
+++ b/src/common/Makefile
@@ -21,7 +21,7 @@ ifdef dnssd
   mdns_flags = -DUSE_DNS_SD
 endif
 
-CFLAGS = -std=gnu99 -fno-strict-aliasing -Wall -Werror -Wstrict-prototypes -g -O2 -I../ -DGIT_REV=\"$(gitrev)\" $(mdns_flags) `pkg-config --cflags $(pkgs)`
+CFLAGS = -std=gnu99 -fno-strict-aliasing -Wall -Wstrict-prototypes -g -O2 -I../ -DGIT_REV=\"$(gitrev)\" $(mdns_flags) `pkg-config --cflags $(pkgs)`
 LDFLAGS = $(ldfdarwin) $(lfdlinux)
 LIBS = `pkg-config --libs $(pkgs)`
 
diff --git a/src/frontend/results.c b/src/frontend/results.c
index 485ac31..162aa3d 100644
--- a/src/frontend/results.c
+++ b/src/frontend/results.c
@@ -381,12 +381,12 @@ fs_value fs_expression_eval(fs_query *q, int row, int block, rasqal_expression *
             return v;
         }
 
-        case RASQAL_EXPR_SUM:
-        case RASQAL_EXPR_AVG:
-        case RASQAL_EXPR_MIN:
-        case RASQAL_EXPR_MAX:
-        case RASQAL_EXPR_LAST:
-            return fs_value_error(FS_ERROR_INVALID_TYPE, "unsupported aggregate operation");
+        //case RASQAL_EXPR_SUM:
+        //case RASQAL_EXPR_AVG:
+        //case RASQAL_EXPR_MIN:
+        //case RASQAL_EXPR_MAX:
+        //case RASQAL_EXPR_LAST:
+        //    return fs_value_error(FS_ERROR_INVALID_TYPE, "unsupported aggregate operation");
 
 #endif
 </code></pre>

### Diff to wwaites py4s (updated diff as of 2010-04-28)

<pre><code style="font-size: 0.7em;">
diff --git a/_py4s.pxd b/_py4s.pxd
index 5251289..0e26250 100644
--- a/_py4s.pxd
+++ b/_py4s.pxd
@@ -110,7 +110,7 @@ cdef extern from "frontend/results.h":
 
 cdef extern from "frontend/import.h":
        int fs_import_stream_start(fsp_link *link, char *model_uri, char *mimety
-       int fs_import_stream_data(fsp_link *link, unsigned char *data, size_t co
+       int fs_import_stream_data(fsp_link *link, unsigned char *data, int count
        int fs_import_stream_finish(fsp_link *link, int *count, int *errors)
 
 cdef extern from "frontend/update.h":
</code></pre>

