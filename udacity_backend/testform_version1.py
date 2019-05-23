import webapp2

form = """
<form method="post">
	<input name="month">
	<input name="day">
	<input name="year">
	<input type="submit">
</form>

"""

class MainPage(webapp2.RequestHandler):
    def post(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(form)

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/testform',TestHandler)
], debug=True)