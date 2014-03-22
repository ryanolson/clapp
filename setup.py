# -*- coding: utf-8 -*-
"""
    setup.py
    ~~~~~~~~

    :copyright: (c) 2013 by Ryan Olson.
    :license: BSD, see LICENSE for more details.
"""

from setuptools import setup, find_packages

setup(
    name='clapp',
    version='0.1.1-dev',
    packages=find_packages(exclude=["dependencies", "sample"]),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    setup_requires=[
        'setuptools>=0.8',
    ],
    install_requires=[
        'gunicorn',
        'pytz',
        'raven',
        'translitcodec',
        'Flask-WTF',
        'Flask-Script',
        'Flask-Babel',
        'Flask-Bootstrap3>=3.0.0.1',
        'Fabric',
        'Flask-CouchDB-Schematics>=0.1.0-beta',
        'couchdb-schematics>=1.0.0',
        'CouchDB',
        'Flask',
    ],
    scripts=[
    ],
    dependency_links = [
        'https://github.com/ryanolson/flask-bootstrap3/tarball/master#egg=Flask-Bootstrap3-3.0.0.1',
        'https://github.com/ryanolson/flask-couchdb-schematics/tarball/master#egg=Flask-CouchDB-Schematics-0.1.0-beta',
    ]
)
