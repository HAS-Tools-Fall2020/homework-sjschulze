# Scott Schulze
# 10/9/2020
# Forecasting code for week 7, using an AR model, as run by a classmate

# %%
# Import the modules  and libraries we will use and set aliases
import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# %%
# Build a function for the flow predicition


def predictions(previous_flow):
    ''''This function is given the previous week's flow value as an input
    Then uses the previously calculated model intercept and coefficient
    to find the first week's prediction. Then uses the first prediction to
    make the predicition for the second week's forecast. Before returning
    both forecast values.
    '''
    prediction = np.zeros(2)
    prediction[0] = model.intercept_ + model.coef_ * previous_flow
    prediction[1] = model.intercept_ + model.coef_ * prediction[0]
    return prediction

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
# Change this for your personal system


filename = 'streamflow_week6.txt'
filepath = os.path.join('../data', filename)
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
train_low_data = train_low.tail(200)

# Making a test set using the most recent 12 weeks
test_low = flow_weekly[:-12][['flow', 'flow_tm1', 'flow_tm2']]

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
# Using the function here to predict week 1 and 2 flows

flow_prediction = predictions(lwf.values)
print(flow_prediction.round(1))
print("Please enter ", flow_prediction[0].round(1),
      " for the week 1 forecast.")
print("Please enter ", flow_prediction[1].round(1),
      " for the week 2 forecast.")
# %%
