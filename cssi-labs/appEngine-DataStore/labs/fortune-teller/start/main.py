#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
import webapp2
import os
import jinja2
import random
import urllib
import json

from google.appengine.api import urlfetch

KEY = 'AIzaSyAMKTAcvtv-kpqeh8Z8itGvHEBPk2En9T0'
URL = 'https://www.googleapis.com/customsearch/v1?'
CX = '010084031095991901722:hq0uahcboms'

def get_fortune():
    #add a list of fortunes to the empty fortune_list array
    fortune_list=['fortune1', 'fortune2']
    #use the random library to return a random element from the array
    random_fortune = fortune_list[random.randint(0,1)]
    return(random_fortune)


#remember, you can get this by searching for jinja2 google app engine
# jinja_current_directory = "insert jinja2 environment variable here"
jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class FortuneHandler(webapp2.RequestHandler):

    def get(self):
        results_template = jinja_current_directory.get_template('templates/fortune-results.html')
        # make a function call that returns a random fortune.
        self.response.write(results_template.render())


    #add a post method
    #def post(self):

class GoodbyeHandler(webapp2.RequestHandler):
    def get(self):

        self.response.write('My response is Goodbye World')

class HelloHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello World. Welcome to the root route of my app')

class SimpleUrlFetcher(webapp2.RequestHandler):
    def get(self):
        query = 'hub'
        query_params = {'key': KEY, 'cx':CX, 'q':query}
        result = urlfetch.fetch(URL + urllib.urlencode(query_params))
        if result.status_code == 200:
            self.response.write(result.status_code)
            self.response.write(result.content)
        else:
            self.response.status_code = result.status_code

#the route mapping
app = webapp2.WSGIApplication([
    #this line routes the main url ('/')  - also know as
    #the root route - to the Fortune Handler
    ('/', HelloHandler),
    ('/predict', FortuneHandler), #maps '/predict' to the FortuneHandler
    ('/farewell', GoodbyeHandler),
    ('/simple', SimpleUrlFetcher)


], debug=True)










































#
