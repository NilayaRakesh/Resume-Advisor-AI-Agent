from sentence_transformers import SentenceTransformer
import numpy as np
from numpy.typing import NDArray

model = SentenceTransformer('all-MiniLM-L6-v2')

# converts text into an embedding (a n-dimentional vector), which represents the semantics of the text
def get_embedding(text: str) -> NDArray[np.float32]:
    return model.encode([text])[0]

# compares embedding vectors using the angle between the vectors in a n-dimentional space
def cosine_similarity(vec1: NDArray[np.float32], vec2: NDArray[np.float32]) -> float:
    return float(np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))