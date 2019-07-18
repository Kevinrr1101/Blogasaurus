

import webapp2
import jinja2
import os

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('index.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())

class BoulderingHtml(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('bouldering.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())

class BoulderingHtml(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('bouldering.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())

class BoulderingHtml(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('bouldering.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/bouldering.html', BoulderingHtml),
], debug=True)
