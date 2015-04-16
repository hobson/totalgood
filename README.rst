TotalGood
=========

|Build Status| |Coverage Status|

A webapp for collecting and prioritizing ideas.

Installation
------------

Fedora
~~~~~~

If you're on Fedora >= 16 but haven't used the django ORM with a
postgres database before, then you'll need to install some binary
packages:

::

    sudo yum install -y postgresql postgresql-server postgresql-libs postgresql-devel

Then download the latest source code:

::

    git clone https://github.com/hobson/totalgood.git

And run a development webserver

::

    cd totalgood/totalgood
    manage.py migrate
    manage.py runserver
    firefox http://localhost:8000

Warning
~~~~~~~

This software is in alpha testing. Install at your own risk.

--------------

Development
-----------

I love merging PRs and adding contributors to the ``__authors__`` list:

::

    git clone https://github.com/hobson/totalgood.git

.. |Build Status| image:: https://travis-ci.org/hobson/totalgood.svg?branch=master
   :target: https://travis-ci.org/hobson/totalgood
.. |Coverage Status| image:: https://coveralls.io/repos/hobson/totalgood/badge.png
   :target: https://coveralls.io/r/hobson/totalgood
