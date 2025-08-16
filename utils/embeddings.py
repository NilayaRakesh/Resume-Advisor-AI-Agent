from sentence_transformers import SentenceTransformer
import numpy as np
from numpy.typing import NDArray

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text: str) -> NDArray[np.float32]:
    return model.encode([text])[0]

def cosine_similarity(vec1: NDArray[np.float32], vec2: NDArray[np.float32]) -> float:
    return float(np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))