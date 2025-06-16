import time
from models.recommender import OptimizedBeatRecommendationModel
from data_gen.generate_beats import generate_beats
from data_gen.generate_users import generate_users
from data_gen.generate_interactions import generate_interactions


def test_latency():
    beats = generate_beats(50)
    users = generate_users(20)
    events = generate_interactions(users, beats, max_per_user=20)

    m = OptimizedBeatRecommendationModel()
    m.beats = beats
    m.users = users
    m.events = events
    m.build_optimized_models()

    start = time.time()
    m.get_fast_recommendations(0, n_recommendations=10)
    latency = time.time() - start
    assert latency < 1.0
