# Beat Recommendation Project

This project demonstrates a simple recommendation system built entirely with
standard Python. The dataset is synthetic and generated on the fly. The model is
inspired by the description in the report and combines content-based and
collaborative signals.

## Usage

```
make data   # generate synthetic dataset
make train  # train model and save to model.json
make serve  # run simple HTTP server on port 8000
```

Recommendations are available at `http://localhost:8000/recommend?user_id=0&n=10`.

Run tests with `make test`.
