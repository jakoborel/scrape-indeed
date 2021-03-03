from WebScraping.scrapeIndeed import *
from spyre import server


class App(server.App):
	title = "Analyze Online Job Postings"

	inputs = [{"type" : 'text',
				"key" : 'query',
				"label" : 'Job title'},
			  {"type" : 'text',
			  	"key" : 'location',
			  	"label" : 'Location'},
			  {"type" : 'text',
			  	"key" : 'salary',
			  	"label" : 'Salary'}]

	# used to trigger when to perform an action (reloading output)
	controls = [dict(type="button",
					id="button1",
					label="Submit")]

	outputs = [dict(type="html",
					id="html",
					#add control linked to the control id to refresh output
					control_id="button1"),
				dict(type="table",
					id="df",
					control_id="button1")]

	# define how html output looks
	# Use params to call to input variables
	def getHTML(self, params):
		return "This is the link: <b>%s</b>" % build_url(params['query'], params['location'], params['salary'])

	def getData(self, params):
		return build_df(build_url(params['query'], params['location'], params['salary']))

app = App()
app.launch()