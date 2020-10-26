# Scott Schulze
# 10/24/2020
# Forecasting code for week 9, using an AR model, with two datasets
# retrieved via web page and rest API

# %%
# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import urllib.request as req
import urllib
from sklearn.linear_model import LinearRegression
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
    'end': '202010230000',                # Update this on Saturday
    'obtimezone': 'UTC',
    'vars': 'air_temp, precip_accum',
    'stids': 'QVDA3',
    'units': 'temp|F,precip|mm',
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
# The complete format of this dictonary is descibed here:
# https://developers.synopticdata.com/mesonet/v2/getting-started/
# Keys shows you the main elements of your dictionary
responseDict.keys()
# You can inspect sub elements by looking up any of the keys in the dictionary
responseDict['UNITS']
# Each key in the dictionary can link to differnt data structures
# For example 'UNITS is another dictionary'
type(responseDict['UNITS'])
responseDict['UNITS'].keys()
responseDict['UNITS']['position']

# where as STATION is a list
type(responseDict['STATION'])
# If we grab the first element of the list that is a dictionary
type(responseDict['STATION'][0])
# And these are its keys
responseDict['STATION'][0].keys()

# Long story short we can get to the data we want like this:
dateTime = responseDict['STATION'][0]['OBSERVATIONS']['date_time']
airT = responseDict['STATION'][0]['OBSERVATIONS']['air_temp_set_1']

# Now we can combine this into a pandas dataframe
data2 = pd.DataFrame({'Temperature': airT}, index=pd.to_datetime(dateTime))
# %%

# Now convert this to weekly data using resample
data_weekly = data2.resample('W').mean()
print(len(data_weekly))
# %%