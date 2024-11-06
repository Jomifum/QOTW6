# Question of the Week 6
#By J Fuentes
import numpy as np
import pandas as pd

# 1. Similarities and differences between pandas and numpy
# Pandas is more suited for data manipulation and analysis, while NumPy is for numerical operations on arrays.

# Example with code:
# NumPy example
arr = np.array([1, 2, 3, 4, 5])
print("NumPy array:", arr)

# Pandas example
df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
print("Pandas DataFrame:\n", df)

# 2. What is the ndarray in NumPy?
# The ndarray is the core data structure in NumPy, representing a multi-dimensional, homogeneous array of fixed-size items.

# 3. Create a 1D array of numbers from 0 to 9
array_1d = np.arange(10)
print("1D array from 0 to 9:", array_1d)

# 4. Extract all odd numbers from array1
array1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
odd_numbers = array1[array1 % 2 != 0]
print("Odd numbers from array1:", odd_numbers)

# 5. Get the common items between a and b
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
common_items = np.intersect1d(a, b)
print("Common items between a and b:", common_items)

# 6. From array a remove all items present in array b
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 6, 7, 8, 9])
result = np.setdiff1d(a, b)
print("Array a without items from array b:", result)

# 7. Find out if iris has any missing values
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', usecols=[0, 1, 2, 3], dtype=float)
missing_values = np.isnan(iris).sum()
print("Number of missing values in iris dataset:", missing_values)
