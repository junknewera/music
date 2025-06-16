from typing import List, Dict
from .build_tfidf import build_tfidf


def build_features(beats: List[Dict]) -> Dict[int, Dict]:
    """Build feature representations for beats."""
    tag_docs = [beat["tags"] for beat in beats]
    tfidf_vectors = build_tfidf(tag_docs)

    features = {}
    for idx, beat in enumerate(beats):
        features[beat["beat_id"]] = {
            "tfidf": tfidf_vectors[idx],
            "bpm": beat["bpm"],
            "key": beat["key"],
        }
    return features
