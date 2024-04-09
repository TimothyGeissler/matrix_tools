import numpy as np

transition_matrix = np.array([[0.5, 0.4, 0.1],
                              [0.2, 0.3, 0.5],
                              [0.1, 0.1, 0.8]])

# Transpose the transition matrix
transposed_matrix = np.transpose(transition_matrix)

# Compute the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(transposed_matrix)

# Find the index of the eigenvalue closest to 1
index = np.argmin(abs(eigenvalues - 1))

# Extract the corresponding eigenvector
stationary_distribution = np.real(eigenvectors[:, index])

# Normalize the stationary distribution
stationary_distribution /= np.sum(stationary_distribution)

print("Stationary distribution of bikes at each station:")
print("Station A:", stationary_distribution[0])
print("Station B:", stationary_distribution[1])
print("Station C:", stationary_distribution[2])