# Just getting used to Pandas DataFrames
# In prep for homework 5
# 9/26/20

# %%
import pandas as pd
import matplotlib.pyplot as plt
import earthpy as et                # This one is new
import os

# %%

# Average monthly precip for Boulder, CO

avg_monthly_precip = pd.DataFrame(columns = ["month","precip_in"],
    data = [
                ["Jan",0.70],["Feb",0.75],["Mar",1.85],["Apr",2.93],["May",3.05],["June",2.02],["July",1.93],["Aug",1.62],["Sept",1.84],["Oct",1.31],["Nov",1.39],["Dec",0.84]
    ]
)

# Notice the nicely formatted output without the use of print
avg_monthly_precip

# %%

# Plotting more efficently with Pandas

f, ax = plt.subplots()
avg_monthly_precip.plot(x="month",y="precip_in", title = "Plot of the DataFrame above using Pandas .plot", ax = ax)
plt.show()
# %%

# Same plot, done another way

f, ax = plt.subplots()
ax.plot(avg_monthly_precip.month,avg_monthly_precip.precip_in)

ax.set(title = 'plot of Pandas DataFrame using matplot lib approach')
plt.show()

# No legend on this one, all months listed, still not an accurate representation...

# %%

# Two methods for gettting the datafile used above
avg_monthly_precip_url = "https://ndownloader.figshare.com/files/12710618"

# Or, using earthpy

et.data.get_data(url = avg_monthly_precip_url)

# %%
# Now set the working directory to earth-analytics
os.chdir(os.path.join(et.io.HOME,"earth-analytics","data"))

# %%

# Import the data from the .csv file
fname = os.path.join("earthpy-downloads","avg-precip-months-seasons.csv")

avg_monthly_precip = pd.read_csv(fname)

avg_monthly_precip

# %%

# Plotting like before only using a barstyle graph instead
# Haven't got this to work, don't know how and can't figure it out.
#f, ax = plt.subplots()
#ax.bar(x = DataFrame.column, height = DataFrame.column)
#plt.show()
# %%

# View the first 5 rows of the imported dataset
avg_monthly_precip.head()

# Now view the last 5 rows
avg_monthly_precip.tail()

# %%
# Get the information about the DataFrame
avg_monthly_precip.info()

# %%
# Get the column names
avg_monthly_precip.columns

# %%
# Get the number of rows and columns
avg_monthly_precip.shape

# %%

# Summary statistics of all numeric columns, same as above, just praciting rounding
avg_monthly_precip.describe().round(2)

# %%

# Can also do other features, not covered in .describe

# Median value of the dataset
avg_monthly_precip.median()

# %%
# Sum of the annual precip
avg_monthly_precip.sum()
# %%

# Interrogate an individual column  in the dataset
avg_monthly_precip[['precip']].describe().round(2)

# %%

# Use describe to describe only one column as a DataFrame
avg_monthly_precip[['precip']].describe().round(2)


# %%

# Use describe to give summary stats on precip column as a series
avg_monthly_precip['precip'].describe().round(2)
# %%

# Sort precipitation in descending order
avg_monthly_precip.sort_values(by = 'precip', ascending = False)
# %%

# Performing calculations on the DataFrame, column specific
# Convert inch values in precip to millimeters
avg_monthly_precip['precip'] *= 25.4

avg_monthly_precip.round(3)
# %%
# Creating a new column with precip in the units of inches
avg_monthly_precip['precip_in'] = avg_monthly_precip['precip']/25.4
avg_monthly_precip
# %%
# Now plot this as bar graphs
f, ax = plt.subplots()

ax.bar(x = avg_monthly_precip.months, height = avg_monthly_precip.precip, color = 'purple')
ax.set(title = 'Plot of Average Monthly Precipitation in mm')
plt.show()
# %%

# Group data by season and summarize precip
precip_by_season = avg_monthly_precip.groupby(['seasons'])[['precip']].describe().round(2)
precip_by_season
# %%

# View the multi-column index of this new DataFrame
precip_by_season.columns
# %%

# Now drop down a level so there is only one index
precip_by_season.columns = precip_by_season.columns.droplevel(0)
precip_by_season
# %%

# Now plot the new DataFrame
f, ax = plt.subplots()

ax.bar(precip_by_season.index,precip_by_season['mean'],color = 'purple')
plt.show()
# %%

# Save the median of precip for each season to the DataFrame
avg_monthly_precip_median = avg_monthly_precip.groupby(['seasons'])[['precip']].median().round(2)
avg_monthly_precip_median
avg_monthly_precip_median.info()
# %%

# Save to new DataFrame with original index
avg_monthly_precip_median = avg_monthly_precip.groupby(["seasons"], as_index = False)[['precip']].median().round(2)
avg_monthly_precip_median
# %%

# Save the summary stats of precip for each season to the DataFrame
avg_monthly_precip_stats = avg_monthly_precip.groupby(['seasons'])[['precip']].describe()
avg_monthly_precip_stats.round(2)
# %%

# Reset the index
avg_monthly_precip_stats.reset_index(inplace = True)
avg_monthly_precip_stats.round(2)
# %%
