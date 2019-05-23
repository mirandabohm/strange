import os
import jinja2
import webapp2
import validate_info

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env =jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape = True)

class PieHandler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a,**kw)

	def render_str(self, template, **kw):
		t = jinja_env.get_template(template)
		return t.render(kw)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class MainPage(PieHandler):
	def get(self, **kw):
		self.render("ass2.html", default_username=self.request.get("email"))

	def write_form(self, username="", password="", verify="", email=""):
		pass

	def post(self):
		'''Get values from the form. Then check them for validity.'''
		self.user_username = self.request.get("username")
		self.user_password = self.request.get("password")
		self.user_verify = self.request.get("in_verify")
		self.user_email = self.request.get("email")

		self.username = validate_info.validate_username(self.user_username)
		self.password = validate_info.validate_password(self.user_password)
		self.verify = validate_info.validate_verify(self.user_password, self.user_verify)
		self.email = validate_info.validate_email(self.user_email)

		if self.username and self.password and self.verify and self.email:
			self.redirect("/welcome?username=" + self.user_username)
			self.response.out.write("username")
		else:
			self.render("ass2.html", username=self.user_username, username_okay=self.username, \
				password=self.password, passwords_match=self.verify, user_email=self.user_email)
		#self.response.out.write(username, password, verify, email)
		# repost the form, but keep values in there. 
		# write error messages if necessary. 
		# post error messages to the form. 
		# format them in red

class WelcomeHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write("<h2>Welcome " + self.request.get("username") + "!</h2>")

app = webapp2.WSGIApplication([('/', MainPage),
	('/welcome', WelcomeHandler)
	],
	debug = True)