# %%

# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week5.txt'
print(os.getcwd())
#os.chdir('..')         # needed this to undo changes from training
fpath = os.path.join('\data', filename)
print(os.getcwd())
print(fpath)



# %%
#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)
# %%
# Getting the information for question 1
data.info()
data.columns

# %%
# Information to inform my weekly forecasts.
data.tail(n=7)
forecast_data = pd.DataFrame(data.tail(n=7))
forecast_data
forecast_data.columns
forecast_data[['flow']].describe().round(2)

# %%
# Question 2 information; isolating and making calculations on the flow column
data[['flow']].describe().round(2)
# %%
# Repeating, just delineating by month also
data_by_month = data.groupby(['month'])[['flow']].describe().round(2)
data_by_month
# %%

# Sort flow in descending order

sorted_data = data.sort_values(by = 'flow', ascending = False)
sorted_data[['flow','year','month','day']].tail()
# %%
sorted_data[['flow','year','month','day']].head()
# %%
# Find the max and min for each month
flow_by_month = data.groupby(['month'])[['flow']].describe()
flow_by_month

for i in range(12):
    print(i)
    i = i + 1
    data_jan = data[data['month']==i]
    print(data_jan.sort_values(by = 'flow', ascending = False).tail(1)[['flow','year']])
    print(data_jan.sort_values(by = 'flow', ascending = False).head(1)[['flow','year']])

# %%
# Find flows within 10% of my guess in September and print the full dates

wk_1_guess = 52
percent_var = 0.1
wk_1_uppper = wk_1_guess + wk_1_guess*percent_var
wk_1_lower = wk_1_guess - wk_1_guess*percent_var

data[((data['flow'] > wk_1_lower) & (data['flow'] < wk_1_uppper) & (data['month'] ==9))][['datetime','flow']]

# %%
