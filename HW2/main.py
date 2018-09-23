from functions import *
import numpy as np

x = np.array([[1, 0, 1], [2, 0, 2], [3, 0, 3], [4, 4, 4]])

print(prod_non_zero_diag(x))
x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
print(max_after_zero(x))

