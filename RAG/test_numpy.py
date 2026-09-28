import numpy as np

A = np.array([1, 0])
B = np.array([0.8, 0.6])

dot_product = np.dot(A, B)

magnitude_A = np.linalg.norm(A)
magnitude_B = np.linalg.norm(B)

cosine_similarity = dot_product / (
    magnitude_A * magnitude_B
)

print(cosine_similarity)


A = np.array([1, 2])
B = np.array([2, 4])

dot_product = np.dot(A,B)

magnitude_A = np.linalg.norm(A)
magnitude_B = np.linalg.norm(B)

cosine_similarity = dot_product / (magnitude_A * magnitude_B)

print(cosine_similarity)