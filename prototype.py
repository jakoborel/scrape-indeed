from DataAnalysis.cleanData import *
from spyre import server
import pandas as pd


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

	tabs = ["Dashboard", "Table"]

	outputs = [dict(type="html",
					id="html",
					tab="Table",
					#add control linked to the control id to refresh output
					control_id="button1"),
				dict(type="table",
					id="df",
					tab="Table",
					control_id="button1")]

	# define how html output looks
	# Use params to call to input variables
	def getHTML(self, params):
		return "Temporary prototype data used to display visuals:"

	def getData(self, params):
		return pd.read_csv("Data_Job_SF.csv")

app = App()
app.launch()