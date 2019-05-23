
import os
import jinja2
import webapp2

# __file__ is set to the name of a module (file) when it is loaded. 
# Here os.path.dirname(__file__) returns the name of the directory the file is located in
# Concatenate the name of the current directory with the word 'templates'
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape = True)

# instantiate jinja environment. Look for rendered templates in this directory. 

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a,**kw)

	def render_str(self, template, **params):
		'''A helper function to be inherited by handler MainPage.
		Takes in template, a file name, and parameters to render a jinja2 template.'''
		t = jinja_env.get_template(template)
		return t.render(**params)

	def render(self, template, **kw):
		''' Writes template to browser. 
		Note that t.render is a built-in jinja function distinct but with the same name.'''
		self.write(self.render_str(template, **kw))

class MainPage(Handler):
	def get(self):
		# Gets all parameters named "food" in the URL and adds them to the shopping list. 
		self.render("shopping_list.html", items=self.request.get_all("food"))

class FizzBuzzHandler(Handler):
	def get(self):
		self.render("fizzbuzz.html", n=self.request.get("n"))

app = webapp2.WSGIApplication([('/', MainPage),
	('/fizzbuzz', FizzBuzzHandler),
	],
	debug = True)