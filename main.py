

import webapp2
import jinja2
import os

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/index.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())

class BlogHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/new_post.html')
        self.response.write(template.render())
    def post(self):
        post_title = self.request.get('post_title')
        name = self.request.get('name')
        post_content = self.request.get('post_content')

        post_vars = {
            "post_title": post_title,
            "name": name,
            "post_content": post_content,
        }
        template = jinja_env.get_template('templates/view_post.html')
        self.response.write(template.render(post_vars))

        # print(post_title)
        # print(name)
        # print(post_content)
        # self.response.write('You created a new post')


class BoulderingHtml(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/bouldering.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())

class SportHtml(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/sportclimbing.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())

class IceHtml(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/iceclimbing.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())

class TradHtml(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/tradclimbing.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/bouldering.html', BoulderingHtml),
    ('/sportclimbing.html', SportHtml),
    ('/iceclimbing.html', IceHtml),
    ('/tradclimbing.html', TradHtml),
    ('/newpost',BlogHandler),
], debug=True)
