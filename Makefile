.PHONY: data train test serve

data:
python -m data_gen

train:
python - <<'PY'
from models.recommender import OptimizedBeatRecommendationModel
m = OptimizedBeatRecommendationModel()
m.load_data('beats.json','users.json','interactions.json')
m.build_optimized_models()
m.save_model('model.json')
print('Model trained.')
PY

test:
pytest -q

serve:
python -m api.app
