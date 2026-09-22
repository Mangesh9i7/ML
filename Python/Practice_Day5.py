# # NumPy ======================================================================

import numpy as np

# # Check NumPy version
# print("NumPy Version:", np.__version__)


# # 1-Dimensional Array ========================================================

# arr1 = np.array([1, 2, 3, 4, 5])

# print("\n1-Dimensional Array:")
# print(arr1)


# # 2-Dimensional Array ========================================================

# arr2 = np.array([
#     [1, 4, 5],
#     [4, 9, 4],
#     [6, 5, 5]
# ])

# print("\n2-Dimensional Array:")
# print(arr2)


# # Multi-Dimensional Array ====================================================

# matrix = np.array([
#     [4, 5, 9],
#     [8, 9, 7]
# ])

# print("\n2-Dimensional Matrix:")
# print(matrix)
# print(' ')

# # nparray with default value
# # np.zeros(shape) (3) for 1-D, (3,3) for 2-D
# r_array = np.zeros((3,3))
# print(r_array)


# # Creating sequence of numbers oin numpy

# arr = np.arange(1, 11, 1)
# print(arr)


# # Creating Identity matrix
## eye(size)

# i_matrix = np.eye(3)
# print(i_matrix)

# # Array Properties and Operations in numpy ========================
## Attributes of array in numpy
## 1] Shape

# arr2 = np.random.randint(2, 10, size=(2, 3))

# print(arr2)
# print(arr2.shape)

## 2] Size :- Total number of element in array

# arr = np.array([[10,20,30], [40,50,60]])
# print(arr.size)


## 3] ndim :- use to find dimensoins of array 
# arr_1d = np.array( [1,2,3])
# arr_2d = np.array([[1,2,3], [4,5,6]])
# arr_3d = np.array( [[[1,2], [3,4], [5,6],[7,8]]])

# print(arr_1d.ndim)
# print(arr_2d.ndim)
# print(arr_3d.ndim)

## 4] dtype :- Data type of the element of array

# arr = np.array([1, 5, 8, 6])
# print(arr.dtype)

## 5] astype :- Use to change data type of the elements of array

# arr = np.array([1.5, 5.8, 5.4, 6.4])
# new_arr = arr.astype(int)
# print(new_arr)
# print(new_arr.dtype)


