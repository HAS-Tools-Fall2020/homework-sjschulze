# Scott Schulze
# 11-16-2020
# HAS Tools
# Homework Week 12

# %%
# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import urllib.request as req
import urllib
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
# netcdf4 needs to be installed in your environment for this to work
import xarray as xr
import rioxarray
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import seaborn as sns
import geopandas as gpd
import fiona
import shapely
from netCDF4 import Dataset
# %%
# %%
# Build a function for flow prediction


def predictions(previous_flow):
    ''''This function is given the previous week's flow value as an input
    Then uses the previously calculated model intercept and coefficient
    to find the first week's prediction. Then uses the first prediction to
    make the predicition for the second week's forecast. Before returning
    both forecast values. As of 10/15/2020, this function was expanded to
    allow for a 16 week forecast, to keep the model from diverging too
    sharply, the week 3-16 forecasts utilized the model forecast output from
    week 2 as the basis for prediction.

    Variables:
    previous_flow: previous_flow is given to the function as the average flow
    from the previous week and is the initialization point for the 'testing'
    of the linear regression model.
    prediction: prediction is an array, set to the size of the forecasts being
    generated, the outputs from the model are stored here. This is what is
    returned to the user.
    '''
    prediction = np.zeros(16)
    for i in range(len(prediction)):
        if i == 0:
            prediction[i] = model.intercept_ + model.coef_ * previous_flow
        else:
            prediction[i] = model.intercept_ + model.coef_ * prediction[i-1]
    return prediction

# %%
# Assigns the directory for the program to locate the data file to be used


filename = 'streamflow_week12.txt'
filepath = os.path.join('../../data', filename)
print(os.getcwd())
print(filepath)

# %%
# Read the data into a pandas dataframe
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no', 'datetime', 'flow',
                            'code'], parse_dates=['datetime'])

# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).dayofweek
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

# Aggregate flow values to weekly
flow_weekly = data.resample("W", on='datetime').mean()

# Find the last week's flow. This is used by the function to make the
# prediction for the first week, then the subsequent weeks follow from there.

lwf = flow_weekly[['flow']].tail(1)
print(lwf)
# %%
# Bring in the historical data
# Net CDF file historical time series
data_path = os.path.join('./data',
                         'Reanalysis_Precip.nc')

# Read in the dataset as an x-array
dataset = xr.open_dataset(data_path)
# look at it
dataset


# We can inspect the metadata of the file like this:
metadata = dataset.attrs
metadata
# And we can grab out any part of it like this:
metadata['dataset_title']
metadata['history']

# we can also look at other  attributes like this
dataset.values
dataset.dims
dataset.coords

# Focusing on just the precip values
precip = dataset['prate']
precip

# Now to grab out data first lets look at spatail coordinates:
dataset['prate']['lat'].values.shape
# The first 4 lat values
dataset['prate']['lat'].values
dataset['prate']['lon'].values

# Now looking at the time;
dataset["prate"]["time"].values
dataset["prate"]["time"].values.shape


# Now lets take a slice: Grabbing data for just one point
lat = dataset["prate"]["lat"].values[0]
lon = dataset["prate"]["lon"].values[0]
print("Long, Lat values:", lon, lat)
one_point = dataset["prate"].sel(lat=lat,lon=lon)
one_point.shape

# use x-array to plot timeseries
one_point.plot.line()
precip_val = one_point.values

# Make a nicer timeseries plot
f, ax = plt.subplots(figsize=(12, 6))
one_point.plot.line(hue='lat',
                    marker="o",
                    ax=ax,
                    color="grey",
                    markerfacecolor="purple",
                    markeredgecolor="purple")
ax.set(title="Time Series For a Single Lat / Lon Location")

#Conver to dataframe
one_point_df = one_point.to_dataframe()

# %%
# Building an autoregressive model

# Step 1: setup the arrays you will build your model on
# This is an autoregressive model so we will be building
# it based on the lagged timeseries

flow_weekly['flow_tm1'] = flow_weekly['flow'].shift(1)
flow_weekly['flow_tm2'] = flow_weekly['flow'].shift(2)

# %%
# Step 2: Pick what portion of the time series you want to use for training.
# Training using a set of the lowest 275 weeks. This was to mitigate
# underforecast error, without increasing the r^2 value further.
train_low = flow_weekly[['flow', 'flow_tm1',
                         'flow_tm2']].sort_values(by='flow', ascending=False)
train_low_data = train_low.tail(275)

# %%
# Step 3: Fit a linear regression model using sklearn
model = LinearRegression()
# See the tutorial to understand the reshape step here

x = train_low_data['flow_tm1'].values.reshape(-1, 1)
y = train_low_data['flow'].values
model.fit(x, y)

# Look at the results from the model
# Not necessary for the forecasting, but good for checking model confidence.
# r^2 values
r_sq = model.score(x, y)

# print the intercept and the slope and then coefficient of determination
print('intercept:', np.round(model.intercept_, 2))
print('slope:', np.round(model.coef_, 2))
print('coefficient of determination:', np.round(r_sq, 2))

# %%
# Step 4 Make a prediction with your model
# Using the function here to predict week 1 and 2 flows, given from the
# previous week's average flow. This is meant to be run by the person entering
# the forecast for the week, and is therefore very explicit, if repititious.

flow_prediction = predictions(lwf.values)
use_historical == True
if use_historical == True:
    for i in range(len(flow_prediction)):
        print("Please enter ", flow_prediction[i].round(2),
            " for the week ", i+1, " forecast.")
        print(" ")
else:
    for i in range(len(flow_prediction)):
        print("Please enter ", flow_prediction[i].round(2),
            " for the week ", i+1, " forecast.")
        print(" ")
# %%
