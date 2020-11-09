# Scott Schulze
# HAS Tools Homwork week 10
# 10/30/2020
# Plotting a map using GIS tools in Python

# %%
# Import libraries

import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd
import fiona
from shapely.geometry import Point
import contextily as ctx
import os

# %%
# Reading in  the shapefile using geopandas
file = os.path.join('../data', 'gagesII_9322_sept30_2011.shp')
gages = gpd.read_file(file)

# Inspect to be sure it is what I am looking for
print(type(gages))
print(gages.head())
print(gages.columns)
print(gages.shape)

# %%