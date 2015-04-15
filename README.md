# `totalgood`

[![Build Status](https://travis-ci.org/hobson/totalgood.svg?branch=master "Travis Build & Test Status")](https://travis-ci.org/hobson/totalgood)
[![Coverage Status](https://coveralls.io/repos/hobson/totalgood/badge.png)](https://coveralls.io/r/hobson/totalgood)
[![Version Status](https://pypip.in/v/totalgood/badge.png)](https://pypi.python.org/pypi/totalgood/)
[![Downloads](https://pypip.in/d/totalgood/badge.png)](https://pypi.python.org/pypi/totalgood/)
[![License](https://pypip.in/license/totalgood/badge.svg?style=flat](https://github.com/hobson/totalgood/)

## Python User Group utilities

A webapp for collecting and prioritizing ideas.

## Installation

### On a Posix System

To get the latest and greatest source and perhaps help us out:

    git clone https://github.com/hobson/totalgood.git

If you're a user and not a developer, and have an up-to-date posix OS with the postgres development binaries and header fileds installed, then just use `pip`.

    pip install totalgood

### Fedora

If you're on Fedora >= 16 but haven't used the django ORM with a postgres database before, then you'll need to install some binary packages before pip will succeed.

    sudo yum install -y postgresql postgresql-server postgresql-libs postgresql-devel
    pip install totalgood

### Bleeding Edge

Even the releases are very unstable, but if you want to have the latest, most broken code

    pip install git+git://github.com/hobsonlane/totalgood.git@master

### Warning

This software is in alpha testing.  Install at your own risk.

---

## Development

I love merging PRs and adding contributors to the `__authors__` list:

    git clone https://github.com/hobson/totalgood.git
