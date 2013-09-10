"""
Benchmarkr Webapp
~~~~~~~~~~~~~~~~~

Copyright 2013 Cray, Inc.


"""
from setuptools import setup, find_packages

setup(
    name='CloudApp',
    version='0.1dev',
    packages=find_packages(exclude=["dependencies"]),
    zip_safe=False,
    platforms='any',
    setup_requires=[
        'setuptools>=0.8',
    ],
    install_requires=[
        'Fabric',
        'Flask',
        'Flask-Babel',
        'Flask-Bootstrap>=2.3.2.10',
        'Flask-CouchDB-Schematics>=0.1.0-beta',
        'Flask-Login',
        'Flask-Principal',
        'Flask-Script',
        'Flask-WTF',
        'Flower',
        'celery-with-redis',
        'authomatic',
        'gunicorn',
        'pygments',
        'python-openid',
        'pytz',
        'raven',
        'translitcodec',
    ],
    scripts=[
        'scripts/cactl',
    ],
    dependency_links = [
        'https://github.com/ryanolson/flask-bootstrap/tarball/master#egg=Flask-Bootstrap-2.3.2.10',
        'https://github.com/ryanolson/flask-couchdb-schematics/tarball/master#egg=Flask-CouchDB-Schematics-0.1.0-beta',
    ]
)
