import json
import pandas as pd
import plotly.express as px

uk_con = json.load(open("west.geojson", 'r'))

print(uk_con["features"][0]["properties"])

con_id_map = {}
for feature in uk_con['features']:
  feature['id'] = feature['properties']['PCON20CD']
  con_id_map[feature['properties']['PCON20NM']] = feature['id']

df=pd.read_csv("final (1).csv")
df['id'] = df['name'].apply(lambda x: con_id_map[x])
df.head()

fig = px.choropleth_mapbox(df, locations='id', geojson=uk_con, color='lab_voter %', hover_name="name", mapbox_style="carto-positron", animation_frame="YEAR", animation_group="id", zoom=4, center = {"lat": 55, "lon": 0})
fig.update_layout(width=800,
    height=900,
    autosize=False,
    margin=dict(t=0, b=0, l=0, r=0))
fig.show()

import plotly.io as pio
pio.write_html(fig, file='LABOUR MAP.html', auto_open=True)
