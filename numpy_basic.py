# -*- coding: utf-8 -*-
"""numpy basic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12tpCLmxZeseaDv_klGU79nQo2M64UhH6
"""

import numpy as np

vector=np.array([1,3,4])
vector

matrix=np.mat([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])
matrix

#reshape
matrix.reshape((2,6))

#transpose
matrix.T

#dotproduct
a=np.array([1,2,3])
b=np.array([4,5,6])
np.dot(a,b)

np.add(a,b)

np.subtract(a,b)

np.multiply(a,b)

mat=np.array([[1,2],[3,4]])
np.linalg.inv(mat)

