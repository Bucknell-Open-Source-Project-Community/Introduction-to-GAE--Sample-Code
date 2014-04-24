import webapp2
from handlers import *

application = webapp2.WSGIApplication([
	('/', ArtHandler),
	('/search', ArtSearchHandler)
], debug=True)