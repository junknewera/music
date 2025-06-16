from .generate_beats import generate_beats
from .generate_users import generate_users
from .generate_interactions import generate_interactions
import json


def main():
    beats = generate_beats(100)
    users = generate_users(50)
    events = generate_interactions(users, beats)

    with open("beats.json", "w") as f:
        json.dump(beats, f)
    with open("users.json", "w") as f:
        json.dump(users, f)
    with open("interactions.json", "w") as f:
        json.dump(events, f)

    print("Synthetic data generated.")


if __name__ == "__main__":
    main()
