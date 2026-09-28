import numpy as np
Q = np.array([1, 0])

A = np.array([0.9, 0.1])
B = np.array([0.8, 0.2])
C = np.array([0, 1])

list = [A,B,C]
magnitute_Q = np.linalg.norm(Q)
cosine_similarites = []
for i in list:
    dot_product = np.dot(Q,i)
    magnitute_A = np.linalg.norm(i)

    cosine_similarity = dot_product / (magnitute_A * magnitute_Q)
    cosine_similarites.append(cosine_similarity)

print(cosine_similarites)