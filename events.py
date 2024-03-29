import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):
  def get(self):
    template = jinja_environment.get_template('templates/events.html')
    self.response.out.write(template.render())
	
class EventDay(webapp2.RequestHandler):
  def get(self, date):
    template = jinja_environment.get_template('templates/events/events-' + date + '.html')
    self.response.out.write(template.render())

app = webapp2.WSGIApplication([('/events', MainPage),
							   (r'/events/(.*)', EventDay)],
                              debug=True)