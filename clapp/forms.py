# -*- coding: utf-8 -*-
"""
    forms.py
    ~~~~~~~~

    :author: Ryan Olson
    :copyright: (c) 2013 by Ryan Olson
    :license: BSD, see LICENSE for more details.
"""
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(Form):
    username_or_email = TextField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])

