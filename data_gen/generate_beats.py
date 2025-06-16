import random
import string
from typing import List, Dict

KEYS = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
TAG_POOL = [
    "hip hop",
    "rock",
    "pop",
    "electronic",
    "ambient",
    "trap",
    "lofi",
    "house",
    "techno",
    "jazz",
    "funk",
    "soul",
    "indie",
    "alternative",
]


def _rand_word(min_len: int = 3, max_len: int = 8) -> str:
    length = random.randint(min_len, max_len)
    return "".join(random.choices(string.ascii_lowercase, k=length))


def generate_beats(n_beats: int = 100) -> List[Dict]:
    """Generate synthetic beats metadata."""
    beats = []
    for beat_id in range(n_beats):
        bpm = random.randint(60, 180)
        key = random.choice(KEYS)
        minor = random.choice(["min", "maj"])
        price = round(random.uniform(10.0, 40.0), 2)
        tags = random.sample(TAG_POOL, k=random.randint(1, 3))
        producer = _rand_word()
        beats.append(
            {
                "beat_id": beat_id,
                "bpm": bpm,
                "key": f"{key}{minor}",
                "tags": tags,
                "price": price,
                "producer": producer,
            }
        )
    return beats
