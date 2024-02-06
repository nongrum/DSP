#1. Python program to add two Matrices
def add_matrices(mat1, mat2):

    result = [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
    return result

# Example Usage:
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result = add_matrices(matrix1, matrix2)

print("Matrix 1:")
for row in matrix1:
    print(row)

print("Matrix 2:")
for row in matrix2:
    print(row)

print("Result after adding matrices:")
for row in result:
    print(row)

#2. Python program to multiply two matrices
def multiply_matrices(mat1, mat2):
    """
    Multiply two matrices.
    """
    result = [[sum(mat1[i][k] * mat2[k][j] for k in range(len(mat2))) for j in range(len(mat2[0]))] for i in range(len(mat1))]
    return result

# Example Usage:
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result = multiply_matrices(matrix1, matrix2)

print("Matrix 1:")
for row in matrix1:
    print(row)

print("Matrix 2:")
for row in matrix2:
    print(row)

print("Result after multiplying matrices:")
for row in result:
    print(row)

# 3. Python program for Matrix Product
       
import numpy as np

def matrix_product(mat1, mat2):
    """
    Matrix product using NumPy.
    """
    result = np.dot(mat1, mat2)
    return result

# Example Usage:
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

result = matrix_product(matrix1, matrix2)

print("Matrix 1:")
print(matrix1)

print("Matrix 2:")
print(matrix2)

print("Result using NumPy's matrix product:")
print(result)

#4. Adding and Subtracting Matrices in Python

def transpose_matrix(mat):
    """
    Transpose a matrix in a single line using zip.
    """
    result = [list(row) for row in zip(*mat)]
    return result

# Example Usage:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result = transpose_matrix(matrix)

print("Original Matrix:")
for row in matrix:
    print(row)

print("Transposed Matrix:")
for row in result:
    print(row)
# 5. Transpose a matrix in a Single line in Python
    

def transpose_matrix(mat):
    """
    Transpose a matrix in a single line using zip.
    """
    result = [list(row) for row in zip(*mat)]
    return result

# Example Usage:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result = transpose_matrix(matrix)

print("Original Matrix:")
for row in matrix:
    print(row)

print("Transposed Matrix:")
for row in result:
    print(row)

#6. Python | Matrix creation of n*n

def create_matrix(n):
    """
    Create an n x n matrix with consecutive numbers.
    """
    matrix = [[j + 1 + n * i for j in range(n)] for i in range(n)]
    return matrix

# Example Usage:
size = 3

result = create_matrix(size)

print(f"{size} x {size} Matrix:")
for row in result:
    print(row)
#. Python | Get Kth Column of Matrix
    
def get_kth_column(mat, k):
    """
    Get the Kth column of a matrix.
    """
    result = [row[k] for row in mat]
    return result

# Example Usage:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
column_index = 1

result = get_kth_column(matrix, column_index)

print("Original Matrix:")
for row in matrix:
    print(row)

print(f"{column_index}th Column of the Matrix:")
print(result)

#8. Python – Vertical Concatenation in Matrix

import numpy as np

def vertical_concatenation(mat1, mat2):
    """
    Perform vertical concatenation of two matrices using NumPy.
    """
    result = np.vstack((mat1, mat2))
    return result

# Example Usage:
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

result = vertical_concatenation(matrix1, matrix2)

print("Matrix 1:")
print(matrix1)

print("Matrix 2:")
print(matrix2)

print("Result after vertical concatenation using NumPy:")
print(result)

