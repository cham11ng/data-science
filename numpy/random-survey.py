"""
Generate Random Survey Data
Calculate Survey Data

Random Parameters
numpy.random.normal(distribution mean, distribution standard deviation, number of samples)
"""

import numpy

height = numpy.round(numpy.random.normal(1.75, 0.20, 5000), 2)
weight = numpy.round(numpy.random.normal(60.32, 15, 5000), 2)

city = numpy.column_stack((height, weight))

print(numpy.mean(city[:, 0]))
