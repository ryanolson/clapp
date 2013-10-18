# -*- coding: utf-8 -*-

import hashlib
import re
import string
import urllib

from schematics.models import Model
from schematics.types import StringType, EmailType, UUIDType
from schematics.types.compound import ModelType, ListType, DictType
from schematics.serialize import blacklist
from werkzeug import security

from flask.ext.login import UserMixin
from flask.ext.couchdb import ViewField
from flask.ext.couchdb.schematics_document import Document

class Email(Model):
    
    address = EmailType(required=True)
    status = StringType(choices=['valid', 'pending'])
    activation_code = StringType()

    class Options:
        serialize_when_none = False
        roles = {
            'safe': blacklist('activation_code'),
        }

    def activate_with_code(code):
        if code == self.activation_code:
            self.status = 'valid'
            self.activation_code = None

    def gravatar_url(self, size=40, default=None):
        if default is None:
           default = 'mm'
        gravatar_url = "http://www.gravatar.com/avatar/{hash}?{args}"
        return gravatar_url.format(hash=hashlib.md5(self.address.lower()).hexdigest(),
                                   args=urllib.urlencode({'d':default, 's':str(size)})) 
    @property
    def uniquify(self):
        """Removes dots and +XXX from Gmail addresses."""
        ua = self.address.lower()
        if 'gmail.com' not in ua:
            return ua
        gmail_regex = re.compile('[%s]' % re.escape(string.punctuation))
        ua = ua.split('@')[0].split('+')[0] # first split on @, then on +
        ua = gmail_regex.sub('', ua)
        return '{user}@gmail.com'.format(user=ua)


class APIKey(Model): 

    key = UUIDType(required=True)
    secret = UUIDType(required=True)

    class Options:
        serialize_when_none = False
        roles = {
            'safe': blacklist('secret'),
        }


class User(Document, UserMixin):

    name = StringType(required=True)
    emails = DictType(ModelType(Email), default=lambda: {})
    primary_email = StringType()
    roles = ListType(StringType())

    _password = StringType(required=True, serialized_name="password")

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        # validate against password rules
        self._password = security.generate_password_hash(password)

    password = property(_get_password, _set_password)

    class Options:
        roles = {
            'safe': blacklist('password'),
        }


    by_email = ViewField('user', """\
        function(doc) {
            if(doc.doc_type == "User") {
                if(doc.emails) {
                    for(var e in doc.emails) {
                        emit(e, doc);
                        if(doc.emails[e].address) {
                            emit(doc.emails[e].address, doc);
                        }
                    }
                }
            }
        }
    """)

    by_name = ViewField('user', """\
        function(doc) {
            if(doc.doc_type == "User") {
                emit(doc.name, doc);
            }
        }
    """)

    def __init__(self, **kwargs):
        kwargs['doc_type'] = 'User'
        if 'password' in kwargs and '_rev' not in kwargs:
            self._set_password(kwargs.pop('password'))
        super(User, self).__init__(**kwargs)
     
    def check_password(self, password):
        if self.password is None:
            return False
        return security.check_password_hash(self.password, password)

    def add_email(self, email):
        new_email = Email(dict(address=email))
        if new_email.uniquify not in self.emails:
            self.emails[new_email.uniquify] = new_email

    def is_admin(self):
        return False

    @classmethod
    def authenticate(cls, login, password):

        def authenticate_user(user):
            if user:
                return user.check_password(password)

        for user in User.by_email[login]:
            if authenticate_user(user):
                return user

        for user in User.by_name[login]:
            if authenticate_user(user):
                return user

        return None

    @classmethod
    def get_by_id(cls, user_id):
        return cls.load(user_id)

    @classmethod
    def check_name(cls, name):
        results = User.by_name[name]
        print var(results)
        print len(results)
        print var(results)
        return len(results) == 0
