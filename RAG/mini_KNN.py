import numpy as np

Q = np.array([1, 0])

documents = {
    "A": np.array([0.9, 0.1]),
    "B": np.array([0.8, 0.2]),
    "C": np.array([0, 1]),
}


def cosine_similarity(a, b):
    dot_product = np.dot(a, b)

    magnitude_a = np.linalg.norm(a)
    magnitude_b = np.linalg.norm(b)

    return dot_product / (magnitude_a * magnitude_b)


results = []

for name, vector in documents.items():
    score = cosine_similarity(Q, vector)
    results.append((name, score))


# Highest similarity first
results = sorted(
    results,
    key=lambda x: x[1],
    reverse=True
)

top_k = results[:2]

print(top_k)