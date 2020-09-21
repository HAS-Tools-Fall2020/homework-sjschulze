# %%

# Scott Schulze
# 9/17/20
# training and refresh

import numpy as np

# %%
# Working with lists as a review
list2 = [True, 'test', 3.14, 3]

print(type(list2))
print([type(i)for i in list2])

# This does not work
#list2 + 7

print(list2)

list3 = [2,1,3.14,4]
print(list3)

#Neither does this
#list3 + 7
print(list3)
for i in list3:
    i + 7
print(list3)

# %%

# numpy arrays

# This is almost the same as list3, but we have turned it into an array and
# all of the values are now floats

array1 = np.array([2,1,3.14,4])

print(array1)
#print(list3)

print(array1.ndim)
print(array1.shape)
print(array1.size)

array1 + 7

print(array1)



# %%

# 1d array of 0, forced to be integers

arr_zero = np.zeros(10, dtype = int)
print(arr_zero)
print(arr_zero.ndim)
print(arr_zero.shape)
print(arr_zero.size)

# %%

# 1d array of 0, set at default floats

arr_zero = np.zeros(10,)
print(arr_zero)
print(arr_zero.ndim)
print(arr_zero.shape)
print(arr_zero.size)

# %%

# 2d array of zeros, then changed to 7's

arr_zero = np.zeros(3,5)
print(arr_zero)

# fill with 7's

# %%
# Slicing in 
test_array = np.ones((3,5))*7
print(test_array)

test_array[0:1,0:1] = 15
print(test_array)

test_array[1, ] = 2
print(test_array)

test_array[::,4] = 30
print(test_array)

test_array[1,::2 ] = 27
print(test_array)

# Not good practice, but shows how you can loop through arrays if we want
for i in range(5):
    test_array[1,i] = 75
print(test_array)
# %%

# Universal functions
# Vectorized opperations -- much faster
# If you can use these, do.

print(test_array)
test_array = test_array * 7
print(test_array)

test_array > 115
# %%
