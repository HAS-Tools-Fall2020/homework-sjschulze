# Scott Schulze
# Has Tools week 10 practice
# 10/28/2020
# %%
# Import libraries
import os
import matplotlib.pyplot as plt
import goepandas as gpd
import earthpy as et

# %%
# Get the dataset and set working directory

data = et.data.get_data('spatial-vector-lidar')
os.chdir(os.path.join(ed.io.HOME, 'earth-analytics'))

# %%
# Define the file path
plot_centroid_path = os.path.join("data", "spatial-vector-lidar", "california", "neon-sjer-site",
                                  "vector_data", "SJER_plot_centroids.shp")
# %%
# Import the shapefile using geopandas
sjer_plot_locations = gpd.read_file(plot_centroid_path)
# %%
# View the top 6 rows of the attribute table
sjer_plot_locations.head(6)

# %%
# View the geometry type of each row
sjer_plot_locations.geom_type

# %%
# View object type
type(sjer_plot_locations)

# %%
# View CRS of object
sjer_plot_locations.crs

# %%
# View the spatial extent
sjer_plot_locations.total_bounds

# %%
# View the size of the data (rows,columns)
sjer_plot_locations.shape

# %%
# We can perform a very basic plot by using the plot method
sjer_plot_locations.plot()

# %% 
# Better practice to set up an axis object to more easily plot different sublayers together.
fig, ax = plt.subplots(figsize = (10, 10))

# Then plot and provid the ax arguement with the ax object
sjer_plot_locations.plot(ax=ax)
plt.show()

# %%
# Note that the axis name can be whatever we want it to be
fig, ax1 = plt.subplots(figsize = (10, 10))
sjer_plot_locations.plot(ax=ax1)
plt.show()

# %%
# Now we can make it fancier, add a legend, plot the data and add a title
fig, ax = plt.subplots(figsize = (10, 10))

# Plot the data and add a legend
sjer_plot_locations.plot(column='plot_type', categorical=True, legend=True
                         figsize=(10,6), markersize=45, cmap="set2", ax=ax)
# Add a title
ax.set_title('SJER Plot Locations\nMadera County, CA')
plt.show()
# %%
# Now we can make it fancier, add a legend, plot the data and add a title
fig, ax = plt.subplots(figsize = (10, 10))

# Now make it fancier by changing the marker and color map
sjer_plot_locations.plot(column='plot_type', categorical=True, legend=True
                         marker='*', markersize=65, cmap="OrRd", ax=ax)
# Add a title
ax.set_title('SJER Plot Locations\nMadera County, CA')
plt.show()

# %%
# Define path to crop boundary
sjer_crop_extent_path = os.path.join('data', 'spatial_vector_lidar', 'california',
                                     'neon-sjer-site', 'vector_data', 'SJER_crop.shp')

# Import crop boundary
sjer_crop_extent = gpd.read_file(sjer_crop_extent_path)

# %% 
# Plot this new data
fig, ax = plt.subplots(figsize=(10,10))

# First setup the plot using the crop_extent layer as the base layer
sjer_crop_extent.plot(color='lightgrey', edgecolor='black', alpha=.5, ax=ax)

# Now add another layer using the same ax
