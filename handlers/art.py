from base import BaseHandler
from models import Art

class ArtHandler(BaseHandler):

	def get(self):
		art_query = Art.all().order('-created')
		arts = [art for art in art_query.run(limit=10)]
		self.render('art.html', arts=arts)

	def post(self):
		title = self.request.get('title')
		art = self.request.get('art')

		if title and art:
			a = Art(title=title, art=art)
			a.put()
			self.redirect('/')
		else:
			error = "We need both a title and artwork!"
			self.render('art.html', error=error)


class ArtSearchHandler(BaseHandler):

	def get(self):
		query = self.request.get('q')
		arts = list(Art.all())

		if query:
			f = lambda art: query in art.title
			arts = filter(f, arts)
			self.render('results.html', arts=arts)
		else:
			error = "You can't search for nothing!"
			self.render('art.html', error=error)