# # import plotly
# # from plotly.graph_objs import Scatter, Layout

# # plotly.offline.plot({
# #     "data": [Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
# #     "layout": Layout(title="hello world")
# # })

# import plotly
# import plotly.graph_objs as go

# x = [4085L, 32933, 2233, 1250, 2665, 31689, 42434, 1146, 48077, 1644, 5380, 1240, 1238, 31309, 32933, 32393, 35651, 5310, 1250, 32936]
# y = [4, 3, 8, 7, 44, 5, 10, 38, 30, 3, 5, 6, 3, 12, 1, 7, 5, 6, 5, 5]


# traceScatter = 	go.Scatter(x = x, y = y, mode='markers'	)


# traceHist =     go.Histogram2d(
#         x = x,
#         y = y
#     )


# data = [traceScatter, traceHist]

# plotly.offline.plot({
#     "data": data,
#     "layout": go.Layout(title="hello world")
# })

import plotly.offline as py
import plotly.graph_objs as go

trace1 = go.Scatter(
    x=[1, 2, 3],
    y=[4, 5, 6]
)
trace2 = go.Scatter(
    x=[20, 30, 40],
    y=[50, 60, 70],
    xaxis='x2',
    yaxis='y2'
)
data = [trace1, trace2]
layout = go.Layout(
    xaxis=dict(
        domain=[0, 0.7]
    ),
    xaxis2=dict(
        domain=[0.8, 1]
    ),
    yaxis2=dict(
        anchor='x2'
    )
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='custom-size-subplot')