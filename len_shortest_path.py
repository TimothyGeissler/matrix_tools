import numpy as np

def matrix_square(A, i, j):
    result = np.eye(len(A), dtype=int)  # Initialize result to the identity matrix
    n = 1
    result = np.dot(result, A)
    while A[i][j] == 0:
        A = np.dot(A, A)
        n+=1
    print("Final adjacency matrix (power = " + str(n) + ")\n")
    print(A)
    return (A[i][j], n)

# Example usage:
A = np.array([[0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 0, 0, 1, 0]])  # Your adjacency matrix or any other 2x2 matrix
i = 1
j = 4

# Normalize for matrix indices
result = matrix_square(A, i - 1, j - 1)
print("Num paths: " + str(result[0]) + " of length " + str(result[1]) + " from node #" + str(i) + " to node #" + str(j))