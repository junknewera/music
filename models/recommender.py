import json
from typing import Dict, List
from collections import defaultdict, Counter
from math import log1p

from .cache import SimpleCache
from features.beat_features import build_features
from features.build_tfidf import cosine_sim


class OptimizedBeatRecommendationModel:
    def __init__(self):
        self.beats = []
        self.users = []
        self.events = []
        self.features = {}
        self.user_profiles = defaultdict(Counter)
        self.popularity = Counter()
        self.cache = SimpleCache()

    def load_data(
        self, beats_path: str, users_path: str, interactions_path: str
    ) -> None:
        with open(beats_path) as f:
            self.beats = json.load(f)
        with open(users_path) as f:
            self.users = json.load(f)
        with open(interactions_path) as f:
            self.events = json.load(f)

    def build_optimized_models(self) -> None:
        self.features = build_features(self.beats)
        for event in self.events:
            if event["action"] == "unlike_beat":
                continue
            beat_id = event["beat_id"]
            user_id = event["user_id"]
            weight = event["weight"]
            for tag in self.features[beat_id]["tfidf"]:
                self.user_profiles[user_id][tag] += weight
            self.popularity[beat_id] += weight

    def _score(self, user_id: int, beat_id: int) -> float:
        user_vec = self.user_profiles[user_id]
        beat_vec = self.features[beat_id]["tfidf"]
        content = cosine_sim(user_vec, beat_vec)
        pop = log1p(self.popularity[beat_id])
        return 0.65 * content + 0.35 * pop

    def get_fast_recommendations(
        self, user_id: int, n_recommendations: int = 10
    ) -> List[Dict]:
        cached = self.cache.get((user_id, n_recommendations))
        if cached:
            return cached
        user_interacted = {e["beat_id"] for e in self.events if e["user_id"] == user_id}
        scores = []
        for beat in self.beats:
            if beat["beat_id"] in user_interacted:
                continue
            s = self._score(user_id, beat["beat_id"])
            scores.append((s, beat))
        scores.sort(reverse=True, key=lambda x: x[0])
        recs = [b for _, b in scores[:n_recommendations]]
        self.cache.set((user_id, n_recommendations), recs)
        return recs

    def save_model(self, path: str) -> None:
        state = {
            "beats": self.beats,
            "users": self.users,
            "events": self.events,
            "features": self.features,
            "user_profiles": {
                uid: dict(cnt) for uid, cnt in self.user_profiles.items()
            },
            "popularity": dict(self.popularity),
        }
        with open(path, "w") as f:
            json.dump(state, f)

    def load_model(self, path: str) -> None:
        with open(path) as f:
            state = json.load(f)
        self.beats = state["beats"]
        self.users = state["users"]
        self.events = state["events"]
        self.features = {int(k): v for k, v in state["features"].items()}
        self.user_profiles = defaultdict(
            Counter, {int(k): Counter(v) for k, v in state["user_profiles"].items()}
        )
        self.popularity = Counter({int(k): v for k, v in state["popularity"].items()})
