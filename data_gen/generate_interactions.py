import random
from typing import List, Dict

ACTION_WEIGHTS = {
    "play_beat": 1.0,
    "like_beat": 3.5,
    "download_beat": 5.0,
    "purchase_beat": 6.0,
    "unlike_beat": -2.0,
}
ACTIONS = list(ACTION_WEIGHTS.keys())


def generate_interactions(
    users: List[Dict], beats: List[Dict], max_per_user: int = 50
) -> List[Dict]:
    """Generate synthetic interaction events."""
    events = []
    for user in users:
        n = random.randint(1, max_per_user)
        for _ in range(n):
            beat = random.choice(beats)
            action = random.choices(ACTIONS, weights=[5, 2, 1, 1, 0.5])[0]
            events.append(
                {
                    "user_id": user["user_id"],
                    "beat_id": beat["beat_id"],
                    "action": action,
                    "weight": ACTION_WEIGHTS[action],
                }
            )
    return events
