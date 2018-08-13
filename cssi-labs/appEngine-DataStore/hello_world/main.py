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

import webapp2
import jinja2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# class MainPage(webapp2.RequestHandler):
#     def get(self):
#         welcome_template = the_jinja_env.get_template('templates/welcome.html')
#         self.response.write(welcome_template.render())

# class second(webapp2.RequestHandler):
#     def get(self):
#         self.response.headers['Content-Type'] = 'text/plain'
#         self.response.write('<h1>Hello, World!</h1>')

class MainPage(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_env.get_template('templates/welcome.html')

        template_dic = {"country": "usa",
                       "region_name": "north east",
                       "region_num": 121,
                       "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Philadelphia_from_South_Street_Bridge_July_2016_panorama_3b.jpg/1200px-Philadelphia_from_South_Street_Bridge_July_2016_panorama_3b.jpg",
                       "city": ["new york","boston", "philadelphia"],
	               "message": "welcome to: "
                       }

        self.response.write(welcome_template.render(template_dic))

# class ShowMemeHandler(webapp2.RequestHandler):
#     def post(self):
#         results_template = the_jinja_env.get_template('templates/results.html')
#         firstname = self.request.get('firstname')
#         lastname = self.request.get('lastname')
#
#         webform_dict = {"fn": firstname, "ln": lastname}
#         self.response.write(results_template.render(webform_dict))

class ShowMemeHandler(webapp2.RequestHandler):
    """docstring for ShowMemeHandler."""
    def get(self):
        self.response.write("hello from ShowMemeHandler")

    def post(self):
        firstname = self.request.get('firstname')
        lastname = self.request.get('lastname')
        age = self.request.get('age')

        #self.response.write(firstname)
        results_template = the_jinja_env.get_template('templates/results.html')

        webform_dict = {"fn": firstname, "ln": lastname, "age": age}
        self.response.write(results_template.render(webform_dict))





app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/showresults', ShowMemeHandler)
], debug=True)

























#
