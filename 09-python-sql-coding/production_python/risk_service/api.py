"""FastAPI service around a saved scikit-learn pipeline.

Run (after saving a model in module 02):
    set MODEL_PATH=..\\..\\02-data-preprocessing-feature-engineering\\artifacts\\heart_model.joblib
    uvicorn risk_service.api:app --reload
"""
from __future__ import annotations

import logging
import os

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException

from .schemas import Patient, Prediction

logger = logging.getLogger(__name__)


def create_app(model=None, model_version: str = "dev") -> FastAPI:
    """App factory: tests pass a model in; production loads it from MODEL_PATH."""
    app = FastAPI(title="Heart risk service")
    state = {"model": model, "version": model_version}

    @app.on_event("startup")
    def load_model() -> None:
        if state["model"] is None:
            path = os.environ.get("MODEL_PATH")
            if not path:
                raise RuntimeError("set MODEL_PATH to a saved .joblib pipeline")
            state["model"] = joblib.load(path)
            state["version"] = os.path.basename(path)
            logger.info("loaded model from %s", path)

    @app.get("/health")
    def health() -> dict:
        return {"status": "ok", "model_loaded": state["model"] is not None}

    @app.post("/predict", response_model=Prediction)
    def predict(patient: Patient) -> Prediction:
        if state["model"] is None:
            raise HTTPException(503, "model not loaded")
        row = pd.DataFrame([patient.model_dump()])
        risk = float(state["model"].predict_proba(row)[0, 1])
        return Prediction(risk=risk, model_version=state["version"])

    return app


app = create_app()
