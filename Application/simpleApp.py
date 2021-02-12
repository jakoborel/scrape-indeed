from spyre import server

class SimpleApp(server.App):
	title = "Simple App"

	inputs = [{"type" : 'text',
				"key" : 'words',
				"label" : 'Input',
				"value" : 'Enter here.',
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
		words = params['words']
		return "This is the input in HTML: <b>%s</b>" % words

app = SimpleApp()
app.launch()