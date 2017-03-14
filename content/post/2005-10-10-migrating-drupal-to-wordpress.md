---
title: >-
  Migrating Drupal to Wordpress
slug: migrating-drupal-to-wordpress
date: 2005-10-10T20:26:57
themes: []
tags: [u'Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 62
---

Here are some scripts along with instructions for migrating a drupal site to wordpress.

## README.txt ##

These instructions are 'implemented' in code as a small python script called migrate-drupal-data.py which you can find below. 

1. Dump your drupal database. To find out how to do this refer to the manual for your db (for mysql from the command line you use mysqldump and for postgres it is pg_dump)

2. Load the drupal dump into your wordpress db:

          mysql -u [username] -p [password] < [path-to-drupal-dump]

3. Edit the convert-drupal-data.sql script replacing 'weblog_' with your wordpress prefix

4. Run convert-drupal-data.sql script against your wordpress db:

          mysql -u [username] -p [password] < convert-drupal-data.sql

    WARNING: this will delete all existing posts, comments and categories from your wordpress db. If you don't want to do that edit the script as indicated therein).

5. Finished.

## Scripts ##

### convert-drupal-data.sql ###

<pre>
-- taken from
-- http://vrypan.net/log/archives/2005/03/10/migrating-from-drupal-to-wordpress/
-- and then improved :-)

-- these lines will result in the deletion of all existing posts, comments
-- and categories. Comments these out using '--' or /* ... */ if you don't
-- want that to happen 
DELETE FROM weblog_wp_categories ;
DELETE FROM weblog_wp_posts ;
DELETE FROM weblog_wp_post2cat ;
DELETE FROM weblog_wp_comments ;

/*
-- does not work (think it is to do with password issues)
-- also causes problems with auto-increment
delete from weblog_wp_users;

INSERT INTO weblog_wp_users
  (ID, user_login, user_pass, user_nickname, user_email, user_registered)
  SELECT
  uid, name, pass, name, mail, FROM_UNIXTIME(timestamp)
  FROM users;
*/

INSERT into weblog_wp_categories(
  cat_ID,cat_name, category_nicename, category_description, category_parent
  )
  SELECT term_data.tid, name, name, description, parent
  FROM term_data, term_hierarchy
  WHERE term_data.tid=term_hierarchy.tid;

INSERT INTO weblog_wp_posts(
  ID, post_author, post_date, post_content, post_title, post_excerpt,
  post_name, post_modified
  )
  SELECT nid, 1, FROM_UNIXTIME(created), body, title, teaser, concat('OLD',nid), FROM_UNIXTIME(changed)
  FROM node
  WHERE type='blog' OR type='page' OR type='story' OR type='forum' ;

INSERT INTO weblog_wp_post2cat (post_id,category_id)
  SELECT nid,tid
  FROM term_node ;

INSERT INTO weblog_wp_comments (
  comment_post_ID, comment_date, comment_content, comment_parent
  )
  SELECT nid, FROM_UNIXTIME(timestamp), concat(subject,' ', comment), thread
  FROM comments ;

DROP TABLE term_data;
DROP TABLE term_hierarchy;
DROP TABLE node;
DROP TABLE term_node;
DROP TABLE comments;
DROP TABLE users;
</pre>

### migrate-drupal-data.py ###

<pre>
#!/usr/bin/env python
import os

# target wordpress db information
user = 'your_user_name'
db = 'your_db_name'

# replace this with the path to your dump from drupal
drupalDbDump = '~/tmp/drupal-db-dump.sql'

# path to drupal conversion sql script
templateConvertDrupalSql = 'convert-drupal-data.sql'

# tmp file used as an intermediary 
convertDrupalData = 'tmp_sql.sql'

# default wordpress prefix used in templateConvertDrupalSql script
# you shouldn't have to change this
templatePrefix = 'weblog_'

# your wordpress prefix
wpPrefix = ''

def prepareConvertSql():
    ff = file(templateConvertDrupalSql)
    tstr = ff.read()
    ff.close()
    tstr = tstr.replace(templatePrefix, wpPrefix)
    ff2 = file(convertDrupalData, 'w')
    ff2.write(tstr)
        ff2.close()

if __name__ == '__main__':
    sqlCmd = 'mysql -u %s -p %s < %s'
    cmdInsertDrupalData = sqlCmd % (user, db, drupalDbDump)
    cmdConvertDrupalData = sqlCmd % (user, db, convertDrupalData)

    # getData()
    prepareConvertSql()
    os.system(cmdInsertDrupalData)
    os.system(cmdConvertDrupalData)
</pre>



