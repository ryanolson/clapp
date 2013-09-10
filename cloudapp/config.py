# -*- coding: utf-8 -*-
"""
    config.py
    ~~~~~~~~~

    Basic site configuration, including Flask, Flask extensions,
    and other components.

    :copyright: (c) 2013 by Ryan Olson.
    :license: BSD, see LICENSE for more details.
"""

class BaseConfig(object):
    """Base CloudApp configuration"""

    DEBUG = True
    TESTING = False
    
    # http://flask.pocoo.org/docs/quickstart/#sessions
    SECRET_KEY = 'change me'


class Config(BaseConfig):
    pass


class TestConfig(BaseConfig):
    TESTING = True
    CSRF_ENABLED = False

