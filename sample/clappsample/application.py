# -*- coding: utf-8 -*-
"""
    application.py
    ~~~~~~~~~~~~~~

    :copyright: (c) 2013 by Ryan Olson.
    :license: BSD, see LICENSE for more details.
"""

from clapp.application import Clapp
from .config import Config

def create_app():
    return Clapp(__name__, config=Config).app
