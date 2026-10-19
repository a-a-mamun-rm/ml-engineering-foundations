# production_python · a small ML service done properly

What "production-quality Python" means for an ML engineer, in about 150 lines:

| File | Practice it shows |
|---|---|
| `risk_service/features.py` | Pure, typed functions; input validation; logging instead of `print`; no mutation of inputs |
| `risk_service/schemas.py` | Pydantic models reject bad requests (wrong category, impossible age) with HTTP 422 |
| `risk_service/api.py` | App factory (`create_app`) so tests can inject a model; config from environment variables; `/health` endpoint |
| `tests/test_service.py` | pytest unit tests for features and API tests with FastAPI's `TestClient` |

## Run

```bash
cd 09-python-sql-coding/production_python
pytest -q                                   # run the tests
# serve the model saved by module 02 (Windows):
set MODEL_PATH=..\..\02-data-preprocessing-feature-engineering\artifacts\heart_model.joblib
uvicorn risk_service.api:app --reload       # then open http://127.0.0.1:8000/docs
```

## ✍️ Your turn
1. Add a test that `predict` returns 503 when no model is loaded.
2. Add a `Dockerfile` (python:3.11-slim, `pip install -r requirements.txt`, `CMD uvicorn ...`).
3. Add a GitHub Actions workflow that runs `pytest` on every push.
