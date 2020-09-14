# Start code for assignment 3
# this code sets up the lists you will need for your homework
# and provides some examples of operations that will be helpful to you

# Modified by Scott Schulze 
# 9/13/2020


# %%
# Import the modules we will use
import os
import numpy as np
import pandas 
import matplotlib.pyplot as plt

print("all good here!")                 # Making sure everything loads properly
# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week3.txt'
fpath = os.path.join('../data', filename)
print(os.getcwd())
print(fpath)

# %%
# DON'T change this part -- this creates the lists you 
# should use for the rest of the assignment
# no need to worry about how this is being done now we will cover
# this in later sections. 

#Read the data into a pandas dataframe
data=pandas.read_table(fpath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

#make lists of the data
flow = data.flow.values.tolist()
date = data.datetime.values.tolist()
year = data.year.values.tolist()
month = data.month.values.tolist()
day = data.day.values.tolist()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

# %%
# Here is some starter code to illustrate some things you might like to do
# Modify this however you would like to do your homework. 
# From here on out you should use only the lists created in the last block:
# flow, date, yearr, month and day

# Calculating some basic properites
print(min(flow),"cfs")      # added 'cfs' to the end, units are everything!
print(max(flow),"cfs")
print(round(np.mean(flow),1),"cfs")   # Rounded to 1 decimal place instead of 13.
print(round(np.std(flow),1),"cfs")


# %% 
# Making and empty list that I will use to store
# index values I'm interested in
#ilist = []

# Loop over the length of the flow list
# and adding the index value to the ilist
# if it meets some criteria that I specify
#for i in range(len(flow)):
    #    if flow [i] > 600 and month[i] == 7:
                #ilist.append(i)

# see how many times the criteria was met by checking the length
# of the index list that was generated
###print(len(ilist))

# %%
# Alternatively I could have  written the for loop I used 
# above to  create ilist like this
#ilist2 = [i for i in range(len(flow)) if flow[i] > 600 and month[i]==7]
#print(len(ilist2))

# Grabbing out the data that met the criteria
# This  subset of data is just the elements identified 
# in the ilist
#subset = [flow[j] for j in ilist]



# %%

# Answering question 1.
print(type(flow))
print(type(year))
print(type(month))
print(type(day))

print(len(flow))
print(len(year))
print(len(month))
print(len(day))
print(month[8])


# %%

# Answering question 2...

klist = []                                          # Create an empty list to put my values into
wk1guess = 42                                       # Create the variable for my first week's guess

for k in range(len(flow)):
    if flow [k] > wk1guess and month [k] == 9:            
        klist.append(k)

print(len(klist))
numobs = len(flow)/12                               # gives the number of september observations
percent = len(klist)/numobs*100


print("The flow is greater than my predicition ",round(percent,1),"% of the time.")
#print(klist)

# %%

# Before 2000
llist = []

for yr in range(1989,2001,1):
    for l in range( len(flow)):     
        if month [l] == 9 and flow [l] > wk1guess and year[l] == yr:
            llist.append(flow[l])

difference = 938-300
print(len(llist))
print("The forecast value was exceeded ",round(len(llist)/difference*100,1),"% of the time for the period from 1989 to 2000.")

#print(llist) 

# %%

# 2010 and later
mlist = []

for yr in range(2010, 2020,1):
    for m in range(len(flow)):
        if month [m] == 9 and flow [m] > wk1guess and year[m] == yr:
            mlist.append(flow[m]) 

difference = 938-360
print(len(mlist))
print("The forecast value was exceeded ",round(len(mlist)/difference*100,1),"% of the time for the period from 2010 to 2020.")
#print(mlist)

# %%

# Question 4. Trying to find the difference in average flow from the first  
# half of September to the second half.

nlist = []
olist = []

for yr in range(len(year)):
    for n in range(len(flow)):
        if month [n] == 9:
            for day in range(1,16,1):       # First half of the month, days 1-15
                nlist.append(flow[day])     
            for day in range(16,31,1):        # 2nd half of the month, days 16-30
                olist.append(flow[day])

print("First half of September (average): ",round(np.mean(nlist),1),"cfs")
print("Second half of September (average): ",round(np.mean(olist),1),"cfs")
print("The average flow drops by ",round(round(np.mean(nlist),1)-round(np.mean(olist),1),1),"cfs from the first half to the second half of September.")

# %%
