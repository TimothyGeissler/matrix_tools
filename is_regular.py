import numpy as np

def is_regular_markov_chain(transition_matrix):
    n = len(transition_matrix)
    print("Matrix size = " + str(n) + "x" + str(n))

    for k in range(1, (n - 1) ** 2 + 2):
        T_k = np.linalg.matrix_power(transition_matrix, k)
        if (T_k > 0).all():
            print("All > 0 for k = " + str(k))
            return True

    return False

# Example usage:
transition_matrix = np.array([[1, 0],
                              [1/2, 2/3]])

if is_regular_markov_chain(transition_matrix):
    print("The Markov chain is regular.")
else:
    print("The Markov chain is not regular.")
