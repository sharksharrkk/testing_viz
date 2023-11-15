import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/marestaing/hosting/main/visited_states.csv')

fig = go.Figure(data=go.Choropleth(
    locations=df['code'], # Spatial coordinates
    z = df['number students'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'plasma',
    colorbar_title = "number of people who visited each state",
))

fig.update_layout(
    title_text = 'The United states',
    geo_scope='usa', # limite map scope to USA
)

fig.show()