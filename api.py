import json

import webapp2

class APIHandler(webapp2.RequestHandler):
    def get(self):
        start_time = self.request.get('start_time', '')
        end_time = self.request.get('end_time','')
        task_name = self.request.get('task_name', '')
        max_hours = self.request.get('max_hours', '')



        response = {'start_time': start_time, 'end_time':end_time, 'task_name': task_name,}
        self.response.headers['Content-Type']= 'application/json'
        self.response.write(json.dumps(response))





app = webapp2.WSGIApplication([
        ('/api', APIHandler)
    ], debug=True)

