"""
ndarray = N-dimensional array
"""

import numpy

height_weight = numpy.array([
    [1.73, 1.68, 1.57, 1.89],
    [65, 69.5, 70.4, 50.4]
])

print(type(height_weight))

print(height_weight.shape)  # display no. of rows and columns

print(height_weight[1, 3])  # before comma specifies row and after specifies column
print(height_weight[:, 1:3])  # select all rows of column 1:3

print(height_weight[1] / height_weight[0] ** 2)
