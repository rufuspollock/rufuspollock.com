---
title: >-
  SQLAlchemy Migrate with Pylons
slug: sqlalchemy-migrate-with-pylons
date: 2009-07-27T19:57:31
themes: []
tags: ['Tech']
projects: []
posttypes: []
featured: False
provenance: [ wordpress, rufuspollock.org, migration-201703 ]
wordpress:
  - post_id: 430
---

Instructions on using [sqlalchemy migrate][migrate] with Pylons, especially to convert an existing pylons project to use [sqlalchemy migrate][migrate]

[migrate]:http://code.google.com/p/sqlalchemy-migrate/

This is based off several excellent sources including this [guide](http://truefalsemaybe.com/2008/09/sqlalchemy-migrations/) and [these](http://groups.google.com/group/migrate-users/browse_thread/thread/f493fbe9786519a5) [threads](http://groups.google.com/group/migrate-users/browse_thread/thread/bdd1e3ccd95b28e8/c10aa1ed75619676).

One important point to note is that you are likely to end up with two versions of your model tables: one in yourapp/model and one in yourapp/migration/versions/*.py with the former representing your tables at HEAD and the second containing upgrade/downgrade scripts whose final result is HEAD. This duplication is a bit annoying and I discuss how it can be avoided below.

1\. Install sqlalchemy migrate for your project e.g.

      pip -E {your-virtualenv} install sqlalchemy-migrate
      # or
      easy_install sqlalchemy-migrate

NB: latest version of migrate are only compatible with sqlalchemy >= 0.5 (for previous version of sqlalchemy you need migrate <= 0.4.5)

2\. Create the migrate repository (i.e. store for upgrade scripts ...).

In your project directory

      migrate create myapp/migration/ "MyApp"

Now create a temporary helper script:

      migrate manage dbmanage.py --repository=myapp/migration/ --url={your-sqlalchemy-db-uri}

3\. Set up db version control

      python dbmanage.py version_control

Check the current version (should be 0)

      python dbmanage.py version

4\. Create a migration script for your existing db

      python dbmanage.py script "Add existing tables"

This will create a script in myapp/migration/versions/001_add_existing_tables.py

Copy into that file the definition for all your existing tables (and other database stuff such as constraints) and then create those tables in the upgrade() function (and delete them in downgrade()).

**That's it! (in theory)**

### Additional Issues

#### 1. Duplication of model/db code

You now have two places for model/db code:

  1. Your migration scripts
  2. Your actual model

This doesn't have to be a problem but it is an obvious way for bugs to creep especially when some people start by creating their DB from the model code and others from the migration scripts.

**Warning: this method will not work if do stuff in your table creation that is not persisted into the actual DB sql (e.g. column default values based on a function, custom db types ...).**

One way to avoid the duplication is to have all table creation and alteration confined to your migration scripts and then have your model tables set up directly from the DB using the autoload=True option. The one disadvantage of this is you can't see the complete DB set up in one places as tables construction may be spread over several migrate scripts. One solution to this is provided by the experimental 'create_model' command which dumps the current DB model in the required sqlalchemy table code.

More discussion in this [migrate-users thread](http://groups.google.com/group/migrate-users/browse_thread/thread/f493fbe9786519a5)

#### Bringing the Migration DB up to date

If you do set up your DB (from new) directly from your model code rather than the migration scripts then this requires that you set up the migration stuff and update the migrate version to the correct number. (I note there is an experimental update_db_to_model command which is supposed to do this for you). You can do this as follows (assuming your migrate repository is at YOURAPP:

          from migrate.versioning.api import version_control, version
          import YOURAPP.migration.versions
          v = version(YOURAPP.migration.__path__[0])
          # log.info( "Setting current version to '%s'" % v )
          # url is your sqlalchemy db url 
          version_control(url, YOURAPP.migration.__path__[0], v)

#### Extras

  * Should wrap upgrade/downgrade in transactions. I found one way to do this [here](http://www.luckydonkey.com/2008/07/27/sqlalchemy-migrate-upgrade-scripts-in-a-transaction/) but testing indicated this didn't work for me (rollback was not working properly when there was an error)

