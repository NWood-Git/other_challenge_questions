# Matrix Multiplication - 6/8/2020
# input 2 np arrays
import numpy as np


def matrix_mult(mat_a, mat_b):
    result_rows = np.shape(mat_a)[0]
    result_columns = np.shape(mat_b)[1]
    if np.shape(mat_a)[1] != np.shape(mat_b)[0]:
        return "You cannot multiply these matrices!"
    else:
        result_matrix = np.zeros((result_rows, result_columns))
        for i in range(result_rows):
            for j in range(result_columns):
                for k in range(np.shape(mat_a)[1]):
                    result_matrix[i][j] += mat_a[i][k] * mat_b[k][j]
        return result_matrix


x = np.array(([1,2,3],
              [4,5,6]))

y = np.array(([1,2],
              [3,4],
              [5,6]))

# print(x.dot(y))
print(matrix_mult(x,y))
print()
print(x.dot(y) == matrix_mult(x,y))