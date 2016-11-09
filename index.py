#!/usr/bin/env python

# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START imports]
import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# [END imports]

DEFAULT_GUESTBOOK_NAME = 'default_guestbook'


# We set a parent key on the 'Greetings' to ensure that they are all
# in the same entity group. Queries across the single entity group
# will be consistent. However, the write rate should be limited to
# ~1/second.


# [START greeting]
class SubscriptionForm(ndb.Model):
    email = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)
    processed = ndb.BooleanProperty(default=False,indexed=True)

# [END greeting]



# [START guestbook]

class LaunchPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render({}))


class NotifyMe(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('notifyme.html')
        self.response.write(template.render({}))

"""class DemoRegistration(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('temp.html')
        self.response.write(template.render({}))

    def post(self):
        name = self.request.get('your_name')
        title = self.request.get('your_title')
        email = self.request.get('company_email')
        company = self.request.get('company_name')
        website = self.request.get('company_website')

        form = RegistrationForm()
        form.name = name
        form.title = title
        form.email = email
        form.company = company
        form.website = website
        form.processed = False
        form.put()

        query_params={'text':'Thank You. We will reach you out soon.'}
        self.redirect('/request/demo/?' + urllib.urlencode(query_params))
# [END guestbook]"""


# [START app]
app = webapp2.WSGIApplication([
    ('/', LaunchPage),
    ('/notify',NotifyMe),
], debug=True)
# [END app]
