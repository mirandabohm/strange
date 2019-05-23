import webapp2
import jinja2
import os
import string
from collections import deque

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

class Helper(webapp2.RequestHandler):
	def write(self, *args, **kwargs):
		self.response.out.write(*args, **kwargs)

	def render_str(self, template, **params):
		# Renders jinja2 template, which will allow us to insert Python into the page.
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kwargs):
		# Writes template to browswer. 
		self.write(self.render_str(template, **kwargs))

class MainPage(Helper):
	def get(self):
		# Get the page. 
		self.render("cipher_logic.html")

	def post(self):
		self.render("cipher_logic.html", information=self.return_cipher(self.request.get("text")))
		#self.render("cipher_logic.html")

	def return_cipher(self, text_entry):
		"""For each item, return its shifted value. Choose the shift list based 
		on original state of capitalization. """
		cipher = ""
		low = string.ascii_lowercase
		high = string.ascii_uppercase
		for letter in text_entry:
			low2 = deque(low)
			if letter not in low and letter not in high:
				cipher += letter
			else:
				low2.rotate(-low.index(letter.lower()))
				if letter.islower(): 
					cipher += low2[13]
				if letter.isupper():
					cipher += low2[13].upper()
		return cipher

app = webapp2.WSGIApplication([
	('/', MainPage)
	], debug = True)