from typing import List, Dict


def generate_users(n_users: int = 50) -> List[Dict]:
    """Generate synthetic user profiles."""
    return [{"user_id": uid} for uid in range(n_users)]
