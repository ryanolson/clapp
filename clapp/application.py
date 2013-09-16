# -*- coding: utf-8 -*-
"""
    application.py
    ~~~~~~~~~~~~~~

    :copyright: (c) 2013 by Ryan Olson.
    :license: BSD, see LICENSE for more details.
"""
import os
import logging

from flask import Flask, Blueprint, render_template

from . import extensions
from . import helpers
from .config import Config



__all__ = ['create_app']


def create_app(cls, config=None, blueprints=None, documents=None, **kwargs):
    return cls(__name__, config=None, blueprints=None, documents=None, **kwargs).app


class Clapp(object):

    def __init__(self, name, config=None, blueprints=None, documents=None, **kwargs):
        """Create a Clapp Flask factory."""

        self.blueprints = blueprints or []
        self.documents = documents or []

        self.app = Flask(name, **kwargs)
        self.configure_app(config)
        self.configure_logging()
        self.configure_blueprints(self.blueprints)
        self.configure_template_filters()
        #self.configure_error_handlers()
        self.configure_extensions()
        self.configure_documents(self.documents)
        self.app.logger.debug("{} was loaded.".format(config))

    def configure_app(self, config=None):
        """Different ways of configurations."""

        # http://flask.pocoo.org/docs/api/#configuration
        self.app.config.from_object(Config)
    
        # http://flask.pocoo.org/docs/config/#instance-folders
        self.app.config.from_pyfile('production.cfg', silent=True)
    
        if config:
            self.app.config.from_object(config)

    def configure_blueprints(self, blueprints):
        """Configure blueprints in views."""

        clapp = Blueprint('clapp', __name__, template_folder='templates', 
            static_folder='static', static_url_path=self.app.static_url_path + '/clapp')
    
        self.app.register_blueprint(clapp)

        for blueprint in blueprints:
            self.app.register_blueprint(blueprint)

    def configure_extensions(self):
        """Configure extensions."""

        # flask-babel
        extensions.babel.init_app(self.app)

        # flask-bootstrap
        extensions.bootstrap.init_app(self.app)

        # flask-couchdb-schematics
        extensions.couchdb.init_app(self.app)
        extensions.couchdb.connect_db(self.app)
    
    def configure_documents(self, documents):
        """Configure CouchDB Documents."""

        for document in documents:
            extensions.couchdb.add_document(document)
        extensions.couchdb.sync(self.app)

    def configure_template_filters(self):
        """Configure Jinja Template Filters and Extensions."""

        @self.app.template_filter()
        def timesince(value):
            return helpers.timesince(value)
    
        @self.app.template_filter()
        def slugify(text, delim=u'_'):
            return helpers.slugify(text, delim)
    
    def configure_logging(self):
        """Configure file(info) and email(error) logging."""

        if self.app.debug or self.app.testing:
            self.app.logger.setLevel(logging.INFO)
            return

        self.app.logger.setLevel(logging.INFO)

        info_log = os.path.join(self.app.config['LOG_FOLDER'], 'info.log')
        info_file_handler = logging.handlers.RotatingFileHandler(info_log, maxBytes=100000, backupCount=10)
        info_file_handler.setLevel(logging.INFO)
        info_file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]')
        )
        self.app.logger.addHandler(info_file_handler)

    def configure_error_handlers(self):
        """Configure Flask Error Handlers."""

        @self.app.errorhandler(403)
        def forbidden_page(error):
            return render_template("clapp/errors/forbidden_page.html"), 403

        @self.app.errorhandler(404)
        def page_not_found(error):
            return render_template("clapp/errors/page_not_found.html"), 404

        @self.app.errorhandler(500)
        def server_error_page(error):
            return render_template("clapp/errors/server_error.html"), 500

