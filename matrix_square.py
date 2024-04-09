import numpy as np
import fractions

np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})

def matrix_square(A, n):
    result = np.eye(len(A), dtype=int)  # Initialize result to the identity matrix
    while n > 0:
        if n % 2 == 1:
            result = np.dot(result, A)
        A = np.dot(A, A)
        n //= 2
    return result

# Example usage:
#A = np.array([[0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 0, 0, 1, 0]])  # Your adjacency matrix or any other 2x2 matrix
A = np.array([
    [0, 1, 0, 0, 0, 0],
    [1/3, 1/3, 1/3, 0, 0, 0],
    [0, 1/3, 1/3, 1/3, 0, 0],
    [0, 0, 1/3, 1/3, 1/3, 0],
    [0, 0, 0, 1/3, 1/3, 1/3],
    [0, 0, 0, 0, 1, 0]
])
np.set_printoptions(precision=3)
n = 1000  # Power to which the matrix is raised
result = matrix_square(A, n)
print(result)