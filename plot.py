# import plotly
# from plotly.graph_objs import Scatter, Layout

# plotly.offline.plot({
#     "data": [Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
#     "layout": Layout(title="hello world")
# })

import plotly
import plotly.graph_objs as go

x = [4085, 32933, 2233, 1250, 2665, 31689, 42434, 1146, 48077, 1644, 5380, 1240, 1238, 31309, 32933, 32393, 35651, 5310, 1250, 32936]
y = [4, 3, 8, 7, 44, 5, 10, 38, 30, 3, 5, 6, 3, 12, 1, 7, 5, 6, 5, 5]


traceScatter = 	go.Scatter(x = x, y = y, mode='markers'	)


traceHist =     go.Histogram2d(
        x = x,
        y = y
    )


data = [traceScatter, traceHist]

plotly.offline.plot({
    "data": data,
    "layout": go.Layout(title="hello world")
})