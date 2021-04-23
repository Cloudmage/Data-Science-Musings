# Make sure you have installed the relevant modules before importing them
# pip install numpy
# pip install matplotlib
# pip install pandas
# pip install geopandas
# pip install plotly
# pip install pyproj


# import relevant modules
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
from pathlib import Path
import plotly.express as px
import fiona
import os
import glob
from pyproj import Proj, transform

# Read in the CSV files into a dataframe
# data is in a directory called d:\powerdata
df = pd.concat(map(pd.read_csv, glob.glob(os.path.join('', "D:\powerdata\*.csv"))))

locpath = os.path.join('',"D:\powerdata\geodata.gpkg")

gdf = gpd.read_file(locpath)

gdf.loc[0:5,['Postcode','geometry']]

# Rename the column names to remove spaces
cols = ['postcode','meters','consumption','mean_consumption','median_consumption']
df.columns = cols

# take the postcode and geometry columns from geodata
gpd_edit = gdf.loc[:,['Postcode','geometry']]

# Set the indexs on the data frames
merged = df.set_index('Postcode').join(gpd_edit.set_index('Postcode'))

# clean up the data to remove the entries with blank geometry data
rows_to_drop = merged[merged['geometry'] ==None ].index
merged.drop(rows_to_drop, inplace=True)

merged['eastings'] = 0
merged['northings'] = 0

eastings = merged.apply(
    lambda row: (row['geometry'].x),
    axis=1)

northings = merged.apply(
    lambda row: (row['northings'].y),
    axis=1)

merged['eastings']=eastings
merged['northings']=northings

# take eastings and northings data and convert to longitude and latitude
v84 = Proj(proj="latlong",towgs84="0,0,0",ellps="WGS84")
v36 = Proj(proj="latlong",K=0.9996012717, ellps="airy",
    towgs84="446.448,-125.157,542.060,0.1502,0.2470, 0.8421,-20.4894")
vgrid = Proj(init="world:bng")

def vectorized_convert(df):
    vlon36, vlat36 = vgrid(df['eastings'].values,
                           df['northings'].values,
                           inverse=True)
    converted = transform(v36, v84, vlon36, vlat36)
    df['longitude'] = converted[0]
    df['latitude'] = converted[1]
    return df

# drop some columns from the dataframe
merged = merged.drop(columns=['meters','consumption','geometry','northings','eastings'])
merged = merged.reset_index()

# plot data onto map
fig = px.scatter_mapbox(merged, lat="latitude", lon="longitude", color="median_consumption", zoom=5, mapbox_style='open-street-map',
                        hover_name='Postcode', hover_data=['median_consumption'])
fig.show()
