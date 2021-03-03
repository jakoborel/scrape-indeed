import plotly.graph_objects as go

import pandas as pd
from spyre import server

class SimpleApp(server.App):
	title = "Simple App"

	inputs = [{"type" : 'text',
				"key" : 'words',
				"label" : 'Input',
				"value" : 'Enter here.'}]
				# used to refresh output when input is changed
				#"action_id" : 'html'}]

	# # used to trigger when to perform an action (reloading output)
	controls = [dict(type="button",
					id="button1",
					label="Submit")]

	outputs = [dict(type="html",
					id="html",
					# add control linked to the control id to refresh output
					control_id="button1"
					)]
				# dict(type="plot",
				# 	id="plot")]

	# define how html output looks
	# Use params to call to input variables
	def getHTML(self, params):
		words = params['words']
		df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_us_cities.csv')
		df.head()

		df['text'] = df['name'] + '<br>Population ' + (df['pop']/1e6).astype(str)+' million'
		limits = [(0,2),(3,10),(11,20),(21,50),(50,3000)]
		colors = ["royalblue","crimson","lightseagreen","orange","lightgrey"]
		cities = []
		scale = 5000

		fig = go.Figure()

		for i in range(len(limits)):
		    lim = limits[i]
		    df_sub = df[lim[0]:lim[1]]
		    fig.add_trace(go.Scattergeo(
		        locationmode = 'USA-states',
		        lon = df_sub['lon'],
		        lat = df_sub['lat'],
		        text = df_sub['text'],
		        marker = dict(
		            size = df_sub['pop']/scale,
		            color = colors[i],
		            line_color='rgb(40,40,40)',
		            line_width=0.5,
		            sizemode = 'area'
		        ),
		        name = '{0} - {1}'.format(lim[0],lim[1])))

		fig.update_layout(
		        title_text = '2014 US city populations<br>(Click legend to toggle traces)',
		        showlegend = True,
		        geo = dict(
		            scope = 'usa',
		            landcolor = 'rgb(217, 217, 217)',
		        )
		    )

		#fig.show()
		return fig.show()
		#return "Here is the 2014 US City Populations: <b>%s</b>" % words

	# # This opens a new tab instead of being put right in page. Not sure how to fix that. 
	# def plot(self, params):
	# 	# load data
	# 	df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_us_cities.csv')
	# 	df.head()

	# 	df['text'] = df['name'] + '<br>Population ' + (df['pop']/1e6).astype(str)+' million'
	# 	limits = [(0,2),(3,10),(11,20),(21,50),(50,3000)]
	# 	colors = ["royalblue","crimson","lightseagreen","orange","lightgrey"]
	# 	cities = []
	# 	scale = 5000

	# 	fig = go.Figure()

	# 	for i in range(len(limits)):
	# 	    lim = limits[i]
	# 	    df_sub = df[lim[0]:lim[1]]
	# 	    fig.add_trace(go.Scattergeo(
	# 	        locationmode = 'USA-states',
	# 	        lon = df_sub['lon'],
	# 	        lat = df_sub['lat'],
	# 	        text = df_sub['text'],
	# 	        marker = dict(
	# 	            size = df_sub['pop']/scale,
	# 	            color = colors[i],
	# 	            line_color='rgb(40,40,40)',
	# 	            line_width=0.5,
	# 	            sizemode = 'area'
	# 	        ),
	# 	        name = '{0} - {1}'.format(lim[0],lim[1])))

	# 	fig.update_layout(
	# 	        title_text = '2014 US city populations<br>(Click legend to toggle traces)',
	# 	        showlegend = True,
	# 	        geo = dict(
	# 	            scope = 'usa',
	# 	            landcolor = 'rgb(217, 217, 217)',
	# 	        )
	# 	    )

	# 	fig.show()

app = SimpleApp()
app.launch()