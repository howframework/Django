Live Demo
=========

http://djangohow-k4ml.rhcloud.com/

Django on OpenShift
===================

This git repository helps you get up and running quickly w/ a Django installation
on OpenShift.  The Django project name used in this repo is 'openshift'
but you can feel free to change it.  Right now the backend is sqlite3 and the
database runtime is @ $OPENSHIFT_DATA_DIR/sqlite3.db.

When you push this application up for the first time, the sqlite database is
copied from wsgi/openshift/sqlite3.db.  This is the stock database that is created
when 'python manage.py syncdb' is run with only the admin app installed.

You can delete the database from your git repo after the first push (you probably
should for security).  On subsequent pushes, a 'python manage.py syncdb' is
executed to make sure that any models you added are created in the DB.  If you
do anything that requires an alter table, you could add the alter statements
in GIT_ROOT/.openshift/action_hooks/alter.sql and then use
GIT_ROOT/.openshift/action_hooks/deploy to execute that script (make sure to
back up your database w/ 'rhc app snapshot save' first :) )


Running on OpenShift
----------------------------

Create an account at http://openshift.redhat.com/ and install the [command line tools client][1].

Create a python-2.6 application

    rhc app create -a djangohow -t python-2.6

Add this upstream repo

    cd djangohow
    git remote add upstream -m master https://github.com/howframework/Django.git
    git pull -s recursive -X theirs upstream master
    
Then push the repo upstream

    git push

That's it, you can now checkout your application at (default admin account is admin/admin):

    http://djangohow-$yournamespace.rhcloud.com
    
[1]:https://openshift.redhat.com/app/getting_started

Local Development
=================
Make sure to have virtualenv installed first. The easiest way is to install using linux package manager such as apt-get or yum.

    sudo apt-get install virtualenv
    cd djangohow
    virtualenv --no-site-packages .
    ./bin/python setup.py install
    ./bin/python manage.py syncdb
    ./bin/python manage.py runserver
    
You can then access the application now running at http://localhost:8000/.
