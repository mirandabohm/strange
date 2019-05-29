
import os
import webapp2
import jinja2
from google.appengine.ext import db
from google.appengine.api import users

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

class Art(db.Model):
	'''Models an individual blog post with title, content, and date/time'''
	subject = db.StringProperty(required = True)
	content = db.TextProperty(required = True)
	created = db.DateTimeProperty(auto_now_add = True)

class Handler(webapp2.RequestHandler):
	def write(self, *args, **kwargs):
		self.response.out.write(*args, **kwargs)

	def render_template(self, template, **kwargs):
		template = jinja_env.get_template(template)
		return template.render(**kwargs)

	def render(self, template, **kwargs):
		self.write(self.render_template(template, **kwargs))

class Blog(Handler):
    def get(self):
        blogposts = db.GqlQuery("SELECT * FROM Art ORDER BY created DESC")
        self.render('frontpage.html', blogposts = blogposts)

# class Blog(Handler):
# 	def render_content(self, subject="", content="", error=""):
# 		blogposts = db.GqlQuery("SELECT * FROM Blogpost ORDER by created DESC")
# 		self.render('frontpage.html', blogposts=blogposts)
# 		#self.render('frontpage.html', subject=subject, content=content, error=error, blogposts=blogposts)

class Permalink(Handler):
    def get(self, post_id):
        blogpost = Art.get_by_id(int(post_id))
        self.render("permalink.html", perm_post = blogpost)

class NewPost(Handler):
	def get(self):
		# self.render('newpost.html')
		self.render('newpost.html', subject_line=self.request.get('subject'))

	def post(self):
		self.subject = self.request.get('subject')
		self.content = self.request.get('content')

		if self.subject and self.content:
			blogpost = Art(subject = self.subject, content = self.content)
			blogpost.put()
			identifier = blogpost.key().id()
			# self.response.out.write(identifier)
			# self.redirect("/blog/%d" % key.id()) 
			self.redirect('/' + str(identifier))
			#5733953138851840
		else:
			self.render('newpost.html', error='Need subject and content, please.')

app = webapp2.WSGIApplication([('/', Blog),
	('/newpost', NewPost),
	(r'/(\d+)', Permalink)
	],
	debug = True)