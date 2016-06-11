from getConfig import conf
import graphlab
import plotly
import plotly.graph_objs as go




train_data = conf['train_data']
test_data = conf['test_data']
path = conf['path']
title = conf['title']

print "Starting Exploratory Analysis"

train_data_full = graphlab.load_sframe('train_data.sf')
train_data = train_data_full.sample(0.005, seed=0)

print "Glimpse of Data"
print train_data

for i in train_data.column_names():
	print "Column ", i 
	col_array = train_data.select_column(i)
	print "Max = ", col_array.max()
	print "Min = ", col_array.min()
	print "Average = ", col_array.mean()
	print "Number of Unique Values", len(col_array.unique())
	print ''


print ''
print "Column Names"
columnNumber = 0
columnArray = []
for i in train_data.column_names():
	print "[" + str(columnNumber) + "] " + i
	columnNumber += 1
	columnArray.append(i)


source = input("Choose title variable (x) most important variable based on which target is changing: ")
target = input("Choose target variable (y) which needs to be predicted: ")
color = input("Choose target variable for color: ")
# Create a trace
x = train_data.select_column(columnArray[source]).apply(lambda (x): int(x)).to_numpy().tolist()
y = train_data.select_column(columnArray[target]).apply(lambda (x): int(x)).to_numpy().tolist()

def plotGraph(trace):
	global title, source, target
	plotly.offline.plot({
	    "data": [trace],
	    "layout": go.Layout(
	    	title = title,
	    	xaxis = dict(
	    		title=columnArray[source]
	    	),
	    	yaxis = dict(
	    		title=columnArray[target]
	    	)
	    )
	})

traceScatter = go.Scatter(
	    x = x,
	    y = y,
	    mode = 'markers'
	)

traceHist = go.Histogram2d(
        x = x,
        y = y
    )

plotGraph(traceScatter)
# plotGraph(traceHist)



