from models.recommender import OptimizedBeatRecommendationModel
from data_gen.generate_beats import generate_beats
from data_gen.generate_users import generate_users
from data_gen.generate_interactions import generate_interactions


def test_recommendations():
    beats = generate_beats(30)
    users = generate_users(10)
    events = generate_interactions(users, beats, max_per_user=10)

    m = OptimizedBeatRecommendationModel()
    m.beats = beats
    m.users = users
    m.events = events
    m.build_optimized_models()

    recs = m.get_fast_recommendations(0, n_recommendations=5)
    assert len(recs) == 5
    assert all("beat_id" in r for r in recs)
