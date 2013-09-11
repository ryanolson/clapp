# -*- coding: utf-8 -*-
"""
    helpers.py
    ~~~~~~~~

    Helper functions for clapp

    :copyright: (c) 2013 by Ryan Olson
    :license: BSD, see LICENSE for more details.
"""
import re
from datetime import datetime

import translitcodec
from flask.ext.babel import gettext, ngettext


def slugify(text, delim=u'-'):
    """Generates an ASCII-only slug."""
    regex = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.:]+')
    result = []
    for word in regex.split(text.lower()):
        word = word.encode('translit/long')
        if word:
            result.append(word)
    return unicode(delim.join(result))

def timesince(dt, default=None):
    """
    Returns string representing "time since" e.g.
    3 days ago, 5 hours ago etc.
    """
    
    if default is None:
        default = gettext("just now")

    now = datetime.utcnow()
    diff = now - dt
    
    periods = (
        (diff.days / 365, "year", "years"),
        (diff.days / 30, "month", "months"),
        (diff.days / 7, "week", "weeks"),
        (diff.days, "day", "days"),
        (diff.seconds / 3600, "hour", "hours"),
        (diff.seconds / 60, "minute", "minutes"),
        (diff.seconds, "second", "seconds"),
    )

    for period, singular, plural in periods:
        
        if not period:
            continue

        singular = u"%%(num)d %s ago" % singular
        plural = u"%%(num)d %s ago" % plural

        return ngettext(singular, plural, num=period)

    return default

