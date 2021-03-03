from spyre import server
from scrape-indeed.WebScraping.scrapeIndeed import build_url

class App(server.App):
	title = "Analyze Online Job Postings"

	inputs = [{"type" : 'text',
				"key" : 'query',
				"label" : 'Job title:',
				# used to refresh output when input is changed
				"action_id" : 'html'}]

	# # used to trigger when to perform an action (reloading output)
	# controls = [dict(type="button",
	# 				id="button1",
	# 				label="Submit")]

	outputs = [dict(type="html",
					id="html",
					# add control linked to the control id to refresh output
					#control_id="button1"
					)]

	# define how html output looks
	# Use params to call to input variables
	def getHTML(self, params):
		query = params['query']
		return "This is the link: <b>%s</b>" % build_url(query)

app = App()
app.launch()