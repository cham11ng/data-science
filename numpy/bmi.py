"""
Numeric Python
Numpy Array
Calculation over entire arrays
"""

import numpy

height_array = numpy.array([1.73, 1.68, 1.57, 1.89])  # contains only single type
weight_array = numpy.array([65, 69.5, 70.4, 50.4])

bmi_array = weight_array / height_array ** 2

print(bmi_array)

print((bmi_array > 18.5) & (bmi_array < 24.9))

print("Normal Weight = ", end='')
print(bmi_array[(bmi_array > 18.5) & (bmi_array < 24.9)])
