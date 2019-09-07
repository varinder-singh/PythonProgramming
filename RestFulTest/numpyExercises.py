import numpy as np

# arr = np.arange(0, 10)
# slice_of_arr = arr[0:6]
#
# print(slice_of_arr)
#
# slice_of_arr[ : ] = 99
# # assigning values affect the original array
# print(slice_of_arr)
#
# print(arr)
#
# arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))
#
# print(arr_2d)
# # either arr[row, col] or arr[row][col] results the same in NP arrays in python
# print(arr_2d[2, 2])
#
# # double square brackets help selecting entire row at once. can select more than one row by placing comma
# print(arr_2d[[2]])
#
# #comparing array elements with a number
# arr_1_d = np.arange(0, 11)
#
# print(arr_1_d)
#
# print(arr_1_d > 5)

#print(arr_1_d)

###################################### Numpy Operations ################################################

arr_1_np = np.arange(0,11)

print(arr_1_np + arr_1_np)

print(arr_1_np)

print(np.sqrt(arr_1_np))

print(np.sin(arr_1_np))

print(np.exp(arr_1_np))