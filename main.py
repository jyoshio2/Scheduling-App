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
from datetime import datetime
from datetime import time
from google.appengine.ext.webapp import template
import utils

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = utils.template('template', 'home_page.html')
        self.response.write(template.render(page, {}))


app = webapp2.WSGIApplication([
        ('/', MainHandler)
    ], debug=True)



# class Task:
#     start_date = datetime(2019, 04, 28, 23, 55, 59, 342380)
#     end_date = datetime(2019, 04, 29, 11, 55, 59, 0, 0)
#
#
#
#     def __init__(self, start_date,end_date, estimate_time,name):
#         pass
#
#
