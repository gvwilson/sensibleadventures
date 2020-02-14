#!/usr/bin/env python

import pandas as pd
import plotly.express as px

data = pd.read_csv('words.csv')
fig = px.line(data, x='Date', y='Words').update_traces(mode='lines+markers')
fig.show()
