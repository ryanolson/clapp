# -*- coding: utf-8 -*-
"""
    forms.py
    ~~~~~~~~~~~

    :copyright: (c) 2013 by Ryan Olson.
    :license: BSD, see LICENSE for more details.
"""
from flask import flash

def flash_errors(form):                                                                                                                                                                                            
    """Flashes form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'error')
