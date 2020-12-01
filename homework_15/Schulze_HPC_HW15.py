# Scott Schulze
# 10/24/2020
# Forecasting code for week 9, using an AR model, with two datasets
# retrieved via rest API

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import urllib.request as req
import urllib
from sklearn.linear_model import LinearRegression
import datetime
import os

# %%
# Build a function for the flow predicition


def predictions(previous_flow):
    ''''This function is given the previous week's flow value as an input
    Then uses the previously calculated model intercept and coefficient
    to find the first week's prediction. Then uses the first prediction to
    make the predicition for the second week's forecast. Before returning
    both forecast values. Reverted to a 2-week forecast on 10/24/2020.

    Variables:
    previous_flow: previous_flow is given to the function as the average flow
    from the previous week and is the initialization point for
    prediction: prediction is an array, set to the size of the forecasts being
    generated, the outputs from the model are stored here.
    '''
    prediction = np.zeros(2)
    for i in range(len(prediction)):
        if i == 0:
            prediction[i] = model.intercept_ + model.coef_ * previous_flow
        elif i == 1:
            prediction[i] = model.intercept_ + model.coef_ * prediction[i-1]
    return prediction
# %%
# Mesonet source for the additional data.

# Creating the URL for the rest API
# Insertion of my token


mytoken = '8a9ebdf8eaba4686b060300750c1658a'

# This is the base url that will be the start our final url
base_url = "http://api.mesowest.net/v2/stations/timeseries"

# Specific arguments for the data that we want
args = {
    'start': '199701010000',              # Must be this date for dataset
    'end': '202010240000',                # Update this on Sunday
    'obtimezone': 'UTC',
    'vars': 'air_temp',
    'stids': 'QVDA3',
    'units': 'temp|F',
    'token': mytoken}

# Takes your arguments and paste them together
# into a string for the api
# (Note you could also do this by hand, but this is better)
apiString = urllib.parse.urlencode(args)
print(apiString)

# add the API string to the base_url
fullUrl = base_url + '?' + apiString
print(fullUrl)

# Now we are ready to request the data
# this just gives us the API response... not very useful yet
response = req.urlopen(fullUrl)

# What we need to do now is read this data
# The complete format of this
responseDict = json.loads(response.read())

# %%
# This creates a dictionary for you
# Long story short we can get to the data we want like this:
dateTime = responseDict['STATION'][0]['OBSERVATIONS']['date_time']
airT = responseDict['STATION'][0]['OBSERVATIONS']['air_temp_set_1']
print("ok")
# %%
# Now we can combine this into a pandas dataframe
data2 = pd.DataFrame({'Temperature': airT}, index=pd.to_datetime(dateTime))
print("ok")
# %%
# Now convert this to weekly data using resample
data_weekly = data2.resample('W').mean().round(1)
print(len(data_weekly))
print("ok")

# %%
# Create a variable for the previous week's average temperature
# This is used later to potentially modify the flow estimation
# I don't remember how to get just the value here. ***
lwt = data_weekly.tail(1).round(1)
print("Last week's average temperature was ", lwt, "°F.")

# %%
# Getting the flow data from the website
# Replace parts of my url with variables
site = '09506000'
start = '1990-01-01'
end = '2020-10-24'      # Update this on Sunday
url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=" \
    + site + "&referred_module=sw&period=&begin_date=" + start \
    + "&end_date=" + end

# Reading the data into a pandas dataframe as before
data = pd.read_table(url, skiprows=30, names=['agency_cd', 'site_no',
                                              'datetime', 'flow', 'code'],
                     parse_dates=['datetime'], index_col='datetime')

# %%
# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data.index).year
data['month'] = pd.DatetimeIndex(data.index).month
data['day'] = pd.DatetimeIndex(data.index).dayofweek
data['dayofweek'] = pd.DatetimeIndex(data.index).dayofweek


# Aggregate flow values to weekly
flow_weekly = data.resample("W").mean().round(2)

# Find the last week's flow. This is used by the function to make the
# prediction for each of the two weeks
flow_weekly.info()
lwf = flow_weekly[['flow']].tail(1)

# %%
# Building an autoregressive model

# Step 1: setup the arrays you will build your model on
# This is an autoregressive model so we will be building
# it based on the lagged timeseries

flow_weekly['flow_tm1'] = flow_weekly['flow'].shift(1)
flow_weekly['flow_tm2'] = flow_weekly['flow'].shift(2)

# %%
# Step 2 - pick what portion of the time series you want to use for training.
# Trying to make a training set using the lowest 200 weeks
train_low = flow_weekly[['flow', 'flow_tm1',
                         'flow_tm2']].sort_values(by='flow', ascending=False)
train_low_data = train_low.tail(275)

# Making a test set using the most recent 13 weeks
test_low = flow_weekly[:-13][['flow', 'flow_tm1', 'flow_tm2']]

# %%
# Step 3: Fit a linear regression model using sklearn
model = LinearRegression()
# See the tutorial to understand the reshape step here
x = train_low_data['flow_tm1'].values.reshape(-1, 1)
y = train_low_data['flow'].values
model.fit(x, y)

# Look at the results
# Not necessary for the forecasting, but a good sanity check.
# r^2 values
r_sq = model.score(x, y)
print('coefficient of determination:', np.round(r_sq, 2))

# print the intercept and the slope
print('intercept:', np.round(model.intercept_, 2))
print('slope:', np.round(model.coef_, 2))

# %%
# Step 4 Make a prediction with your model
# Using the function here to predict week 1 and 2 flows, given from the
# previous week's average flow. As of 10/24/2020, the previous week's average
# temperature is also considered, adding 4 cfs if the average weekly
# temperature was less than 80°F. This is meant to be run by the person
# entering the forecast for the week, and is therefore very explicit,
# if repititious.

flow_prediction = predictions(lwf.values)
for i in range(len(flow_prediction)):
    print(i)
    if lwt.values <= 80:
        print("Please enter ", flow_prediction[i].round(1)+4,
              " for the week ", i+1, " forecast.")
        print(" ")
    else:
        print("Please enter ", flow_prediction[i].round(1),
              " for the week ", i+1, " forecast.")
        print(" ")


# %%
