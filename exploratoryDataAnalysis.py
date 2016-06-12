from getConfig import conf
import graphlab
import plotly
import plotly.graph_objs as go




train_sf = conf['train_data_sf']
test_sf = conf['test_data_sf']
path = conf['path']
title = conf['title']

print "Starting Exploratory Analysis"

train_data_full = graphlab.load_sframe(train_sf)
train_data = train_data_full.sample(0.005, seed=0)

print "Glimpse of Data"
print train_data

# for i in train_data.column_names():
# 	print "Column ", i 
# 	col_array = train_data.select_column(i)
# 	print "Max = ", col_array.max()
# 	print "Min = ", col_array.min()
# 	print "Average = ", col_array.mean()
# 	print "Number of Unique Values", len(col_array.unique())
# 	print ''


print ''
print "Column Names"
columnNumber = 0
columnArray = []
for i in train_data.column_names():
	print "[" + str(columnNumber) + "] " + i
	columnNumber += 1
	columnArray.append(i)


source = raw_input("Choose variable(s) (x) separated by comma based on which target is changing: ")
target = input("Choose target variable (y) which needs to be predicted: ")
color = input("Choose target variable for color: ")
# Create a trace

def plotGraph(trace, src, targ):
	global title
	print "plot graph"
	print plotly.offline.plot({
	    "data": [trace],
	    "layout": go.Layout(
	    	title = title,
	    	xaxis = dict(
	    		title=columnArray[src]
	    	),
	    	yaxis = dict(
	    		title=columnArray[targ]
	    	)
	    )},
	    filename = columnArray[src] + " vs " + columnArray[targ]
	    # output_type = 'div'
	)

def plotScatter(x, y, src, targ):
	print "plot scatter"
	traceScatter = go.Scatter(
		    x = x,
		    y = y,
		    mode = 'markers'
		)
	plotGraph(traceScatter, src, targ)

def formGraphData():
	global title, source, target
	xValues = map(lambda x: int (x), source.split(','))
	y = train_data.select_column(columnArray[target]).apply(lambda (x): int(x)).to_numpy().tolist()
	for ids in xValues:
		x = train_data.select_column(columnArray[ids]).apply(lambda (x): int(x)).to_numpy().tolist()
		plotScatter(x, y, ids, target)

formGraphData()

# traceHist = go.Histogram2d(
#         x = x,
#         y = y
#     )

# plotGraph(traceScatter)
# plotGraph(traceHist)



