import numpy as np
np.random.seed(33) # set the random seed for reproducibility

# builtin functions

print(f"\n np.array([1, 2, 3]) = {np.array([1, 2, 3])}") # create a 1D array
print(f"\n np.array([[1, 2], [3, 4]]) = {np.array([[1, 2], [3, 4]])}") # create a 2D array
print(f"\n np.zeros((2, 3)) = {np.zeros((2, 3))}") # create a 2D array of zeros with shape (2, 3)
print(f"\n np.ones((4, 5)) = {np.ones((4, 5))}") # create a 2D array of ones with shape (4, 5)
print(f"\n np.eye(3) = {np.eye(3)}") # create a 2D array with ones on the diagonal and zeros elsewhere (identity matrix)
print(f"\n np.arange(0, 10, 2) = {np.arange(0, 10, 2)}") # create a 1D array of evenly spaced values within a specified range (start, stop, step)
print(f"\n np.linspace(0, 1, 5) = {np.linspace(0, 1, 5)}") # create a 1D array of evenly spaced values between a specified start and stop value (inclusive) with a specified number of samples
print(f"\n np.random.rand(3, 4) = {np.random.rand(3, 4)}") # create a 2D array of random values between 0 and 1 with shape (3, 4)
print(f"\n np.random.randint(0, 10, size=(2, 3)) = {np.random.randint(0, 10, size=(2, 3))}") # create a 2D array of random integers between a specified low (inclusive) and high (exclusive) value with a specified shape
print(f"\n np.random.normal(loc=0, scale=1, size=(2, 3)) = {np.random.normal(loc=0, scale=1, size=(2, 3))}") # create a 2D array of random values drawn from a normal distribution with specified mean (loc), standard deviation (scale), and shape (size)

# max and min functions
print(f"\n np.max([1, 2, 3]) = {np.max([1, 2, 3])}") # find the maximum value in a 1D array
print(f"\n np.min([[1, 2], [3, 4]]) = {np.min([[1, 2], [3, 4]])}") # find the minimum value in a 2D array
print(f"\n np.max([[1, 2], [3, 4]], axis=0) = {np.max([[1, 2], [3, 4]], axis=0)}") # find the maximum value along the specified axis
print(f"\n np.min([[1, 2], [3, 4]], axis=1) = {np.min([[1, 2], [3, 4]], axis=1)}") # find the minimum value along the specified axis

# max and min index functions
print(f"\n np.argmax([1, 2, 3]) = {np.argmax([1, 2, 3])}") # find the index of the maximum value in a 1D array
print(f"\n np.argmin([[1, 2], [3, 4]]) = {np.argmin([[1, 2], [3, 4]])}") # find the index of the minimum value in a 2D array
print(f"\n np.argmax([[1, 2], [3, 4]], axis=0) = {np.argmax([[1, 2], [3, 4]], axis=0)}") # find the indices of the maximum values along the specified axis
print(f"\n np.argmin([[1, 2], [3, 4]], axis=1) = {np.argmin([[1, 2], [3, 4]], axis=1)}") # find the indices of the minimum values along the specified axis

# these functions can also be called on ndarray objects directly
arr_1d = np.array([1, 2, 3])
arr_2d = np.array([[1, 2], [3, 4]])

print(f"\n arr_1d.max() = {arr_1d.max()}") # find the maximum value in a 1D array
print(f"\n arr_2d.min() = {arr_2d.min()}") # find the minimum value in a 2D array
print(f"\n arr_2d.max(axis=0) = {arr_2d.max(axis=0)}") # find the maximum value along the specified axis
print(f"\n arr_2d.min(axis=1) = {arr_2d.min(axis=1)}") # find the minimum value along the specified axis
print(f"\n arr_1d.argmax() = {arr_1d.argmax()}") # find the index of the maximum value in a 1D array
print(f"\n arr_2d.argmin() = {arr_2d.argmin()}") # find the index of the minimum value in a 2D array
print(f"\n arr_2d.argmax(axis=0) = {arr_2d.argmax(axis=0)}") # find the indices of the maximum values along the specified axis
print(f"\n arr_2d.argmin(axis=1) = {arr_2d.argmin(axis=1)}") # find the indices of the minimum values along the specified axis

# demo the use of dtype, shape, size, reshape, and astype
arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)
print(f"\n arr = {arr}") # original array
print(f"\n arr.dtype = {arr.dtype}") # data type of the array
print(f"\n arr.shape = {arr.shape}") # shape of the array
print(f"\n arr.size = {arr.size}") # total number of elements in the array
reshaped_arr = arr.reshape((3, 2))
print(f"\n reshaped_arr = {reshaped_arr}") # reshaped array
print(f"\n reshaped_arr.shape = {reshaped_arr.shape}") # shape of the reshaped array
int_arr = arr.astype(np.int32)
print(f"\n int_arr = {int_arr}") # array converted to int32
print(f"\n int_arr.dtype = {int_arr.dtype}") # data type of the converted array

# demo indexing and slicing
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\n arr = {arr}") # original array
print(f"\n arr[0] = {arr[0]}") # access the first row of the array
print(f"\n arr[1] = {arr[1]}") # access the second row of the array
print(f"\n arr[0, 1] = {arr[0, 1]}") # access the element in the first row and second column
print(f"\n arr[1, 2] = {arr[1, 2]}") # access the element in the second row and third column
print(f"\n arr[:, 0] = {arr[:, 0]}") # access the first column of the array
print(f"\n arr[:, 1] = {arr[:, 1]}") # access the second column of the array
print(f"\n arr[:, 2] = {arr[:, 2]}") # access the third column of the array
print(f"\n arr[0, :] = {arr[0, :]}") # access the first row of the array
print(f"\n arr[1, :] = {arr[1, :]}") # access the second row of the array
print(f"\n arr[0:2, 1:3] = {arr[0:2, 1:3]}") # access a subarray of the original array (rows 0 to 1 and columns 1 to 2)
print(f"\n arr[::2, ::2] = {arr[::2, ::2]}") # access every other row and every other column of the array

# demo broadcasting
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([10, 20, 30])
print(f"\n arr1 = {arr1}") # original array 1
print(f"\n arr2 = {arr2}") # original array 2
broadcasted_sum = arr1 + arr2
print(f"\n broadcasted_sum = {broadcasted_sum}") # result of broadcasting arr2 to match the shape of arr1 and performing element-wise addition
broadcasted_product = arr1 * arr2
print(f"\n broadcasted_product = {broadcasted_product}") # result of broadcasting arr2 to match the shape of arr1 and performing element-wise multiplication    

# demo comparing arrays
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[1, 0, 3], [4, 5, 0]])
print(f"\n arr1 = {arr1}") # original array 1
print(f"\n arr2 = {arr2}") # original array 2
print(f"\n arr1 == arr2 = {arr1 == arr2}") # element-wise comparison of arr1 and arr2 for equality
print(f"\n arr1 != arr2 = {arr1 != arr2}") # element-wise comparison of arr1 and arr2 for inequality
print(f"\n arr1 > arr2 = {arr1 > arr2}") # element-wise comparison of arr1 and arr2 for greater than
print(f"\n arr1 < arr2 = {arr1 < arr2}") # element-wise comparison of arr1 and arr2 for less than
print(f"\n arr1 >= arr2 = {arr1 >= arr2}") # element-wise comparison of arr1 and arr2 for greater than or equal to
print(f"\n arr1 <= arr2 = {arr1 <= arr2}") # element-wise comparison of arr1 and arr2 for less than or equal to

# demo logical operations on arrays
arr1 = np.array([[True, False, True], [False, True, False]])
arr2 = np.array([[False, True, False], [True, False, True]])
print(f"\n arr1 = {arr1}") # original array 1
print(f"\n arr2 = {arr2}") # original array 2
print(f"\n np.logical_and(arr1, arr2) = {np.logical_and(arr1, arr2)}") # element-wise logical AND operation between arr1 and arr2
print(f"\n np.logical_or(arr1, arr2) = {np.logical_or(arr1, arr2)}") # element-wise logical OR operation between arr1 and arr2
print(f"\n np.logical_not(arr1) = {np.logical_not(arr1)}") # element-wise logical NOT operation on arr1
print(f"\n np.logical_xor(arr1, arr2) = {np.logical_xor(arr1, arr2)}") # element-wise logical XOR operation between arr1 and arr2

# demo the use of np.where for conditional selection
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\n arr = {arr}") # original array
condition = arr > 3
print(f"\n condition = {condition}") # boolean array indicating where the condition is true
selected_elements = np.where(condition, arr, 0) # select elements from arr where condition is true, otherwise select 0
print(f"\n selected_elements = {selected_elements}") # result of np.where based on the condition

# demo the use of np.unique for finding unique elements in an array
arr = np.array([1, 2, 2, 3, 4, 4, 5])
print(f"\n arr = {arr}") # original array
unique_elements = np.unique(arr) # find unique elements in the array
print(f"\n unique_elements = {unique_elements}") # result of np.unique showing unique elements

# demo numpy operations for mathematical functions
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\n arr = {arr}") # original array
print(f"\n np.sum(arr) = {np.sum(arr)}") # sum of all elements in the array
print(f"\n np.mean(arr) = {np.mean(arr)}") # mean of all elements in the array
print(f"\n np.std(arr) = {np.std(arr)}") # standard deviation of all elements in the array
print(f"\n np.var(arr) = {np.var(arr)}") # variance of all elements in the array
print(f"\n np.median(arr) = {np.median(arr)}") # median of all elements in the array
print(f"\n np.cumsum(arr) = {np.cumsum(arr)}") # cumulative sum of the elements in the array
print(f"\n np.cumprod(arr) = {np.cumprod(arr)}") # cumulative product of the elements in the array
print(f"\n np.sqrt(arr) = {np.sqrt(arr)}") # element-wise square root of the array
print(f"\n np.exp(arr) = {np.exp(arr)}") # element-wise exponential of the array
print(f"\n np.log(arr) = {np.log(arr)}") # element-wise natural logarithm of the array
print(f"\n np.sin(arr) = {np.sin(arr)}") # element-wise sine of the array
print(f"\n np.cos(arr) = {np.cos(arr)}") # element-wise cosine of the array
print(f"\n np.tan(arr) = {np.tan(arr)}") # element-wise tangent of the array
