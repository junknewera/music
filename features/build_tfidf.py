from collections import Counter
from typing import Dict, List
import math


def build_tfidf(documents: List[List[str]]) -> Dict[int, Dict[str, float]]:
    """Build TF-IDF vectors for list of tag lists."""
    df = Counter()
    for tags in documents:
        unique_tags = set(tags)
        for tag in unique_tags:
            df[tag] += 1

    n_docs = len(documents)
    idf = {tag: math.log(n_docs / (df[tag])) for tag in df}

    tfidf_vectors = {}
    for idx, tags in enumerate(documents):
        tf = Counter(tags)
        vec = {tag: (tf[tag] / len(tags)) * idf[tag] for tag in tf}
        tfidf_vectors[idx] = vec
    return tfidf_vectors


def cosine_sim(v1: Dict[str, float], v2: Dict[str, float]) -> float:
    common = set(v1) & set(v2)
    num = sum(v1[t] * v2[t] for t in common)
    den1 = math.sqrt(sum(v1[t] ** 2 for t in v1))
    den2 = math.sqrt(sum(v2[t] ** 2 for t in v2))
    if den1 == 0 or den2 == 0:
        return 0.0
    return num / (den1 * den2)
