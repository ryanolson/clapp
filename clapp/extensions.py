# -*- coding: utf-8 -*-
"""
    extensions.py
    ~~~~~~~~~~~~~

    Initialize Flask and Jinja extensions.

    :copyright: (c) 2013 by Ryan Olson.
    :license: BSD, see LICENSE for more details.
"""

from flask.ext.babel import Babel
babel = Babel()

from flask.ext.bootstrap import Bootstrap
bootstrap = Bootstrap()

from flask.ext.couchdb import CouchDB
couchdb = CouchDB()

