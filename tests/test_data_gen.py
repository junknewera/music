from data_gen.generate_beats import generate_beats
from data_gen.generate_users import generate_users
from data_gen.generate_interactions import generate_interactions


def test_generation():
    beats = generate_beats(10)
    users = generate_users(5)
    events = generate_interactions(users, beats, max_per_user=5)

    assert len(beats) == 10
    assert len(users) == 5
    assert len(events) > 0
