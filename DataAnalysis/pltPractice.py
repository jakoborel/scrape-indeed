import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes

y = np.array([35, 25, 25, 15])
labels = ["Apples", "Bananas", "Cherries", "Dates"]
colors = ["black", "hotpink", "b", "#4CAF50"]

# Create pie chart.
plt.pie(y, labels=labels, colors=colors)
plt.show()

# Simple bar chart
plt.bar(labels, y)
plt.show()

# A stacked bar chart example
N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
ind = np.arange(N) # the x locations for the groups
width = 0.35
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(ind, menMeans, width, color='r')
ax.bar(ind, womenMeans, width,bottom=menMeans, color='b')
# These dont want to work?
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
ax.set_yticks(np.arange(0, 81, 10))
ax.legend(labels=['Men', 'Women'])
plt.show()