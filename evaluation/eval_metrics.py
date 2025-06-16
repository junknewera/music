from typing import List, Set
import math


def precision_at_k(recommended: List[int], relevant: Set[int], k: int) -> float:
    if k == 0:
        return 0.0
    rec_k = recommended[:k]
    hit = sum(1 for r in rec_k if r in relevant)
    return hit / k


def recall_at_k(recommended: List[int], relevant: Set[int], k: int) -> float:
    if not relevant:
        return 0.0
    rec_k = recommended[:k]
    hit = sum(1 for r in rec_k if r in relevant)
    return hit / len(relevant)


def ndcg_at_k(recommended: List[int], relevant: Set[int], k: int) -> float:
    dcg = 0.0
    for i, r in enumerate(recommended[:k]):
        if r in relevant:
            dcg += 1 / math.log2(i + 2)
    ideal_hits = min(len(relevant), k)
    idcg = sum(1 / math.log2(i + 2) for i in range(ideal_hits))
    if idcg == 0:
        return 0.0
    return dcg / idcg


def catalog_coverage(recommended_lists: List[List[int]], catalog_size: int) -> float:
    rec_items = set()
    for recs in recommended_lists:
        rec_items.update(recs)
    return len(rec_items) / catalog_size if catalog_size else 0.0
