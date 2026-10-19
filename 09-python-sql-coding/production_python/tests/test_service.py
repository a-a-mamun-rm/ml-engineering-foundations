import numpy as np
import pandas as pd
import pytest
from fastapi.testclient import TestClient
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer, OneHotEncoder

from risk_service.api import create_app
from risk_service.features import add_features

PATIENT = {"Age": 61, "Sex": "M", "ChestPainType": "ASY", "RestingBP": 140, "Cholesterol": 0,
           "FastingBS": 1, "RestingECG": "Normal", "MaxHR": 110, "ExerciseAngina": "Y",
           "Oldpeak": 2.0, "ST_Slope": "Flat"}


@pytest.fixture
def frame():
    rng = np.random.default_rng(0)
    rows = [dict(PATIENT, Age=int(a), MaxHR=float(h), Sex=s, Cholesterol=float(c))
            for a, h, s, c in zip(rng.integers(30, 80, 40), rng.integers(90, 190, 40),
                                  rng.choice(["M", "F"], 40), rng.choice([0, 180, 240, 300], 40))]
    df = pd.DataFrame(rows)
    df["HeartDisease"] = (df.Age > 55).astype(int)
    return df


@pytest.fixture
def model(frame):
    prep = ColumnTransformer([
        ("num", SimpleImputer(strategy="median"), ["Age", "MaxHR", "Cholesterol", "HR_reserve"]),
        ("cat", OneHotEncoder(handle_unknown="ignore"), ["Sex", "AgeBand"]),
    ])
    pipe = Pipeline([("features", FunctionTransformer(add_features)), ("prep", prep),
                     ("model", LogisticRegression(max_iter=1000))])
    return pipe.fit(frame.drop(columns="HeartDisease"), frame.HeartDisease)


def test_zero_cholesterol_becomes_missing():
    out = add_features(pd.DataFrame([PATIENT]))
    assert np.isnan(out.loc[0, "Cholesterol"])


def test_engineered_columns():
    out = add_features(pd.DataFrame([PATIENT]))
    assert out.loc[0, "AgeBand"] == "55-69"
    assert out.loc[0, "HR_reserve"] == 220 - 61 - 110


def test_input_is_not_modified():
    df = pd.DataFrame([PATIENT])
    add_features(df)
    assert df.loc[0, "Cholesterol"] == 0


def test_missing_column_raises():
    with pytest.raises(ValueError, match="missing columns"):
        add_features(pd.DataFrame([{"Age": 50}]))


def test_predict_endpoint(model):
    client = TestClient(create_app(model, model_version="test"))
    r = client.post("/predict", json=PATIENT)
    assert r.status_code == 200
    body = r.json()
    assert 0 <= body["risk"] <= 1 and body["model_version"] == "test"


def test_invalid_input_rejected(model):
    client = TestClient(create_app(model))
    r = client.post("/predict", json=dict(PATIENT, Sex="X"))
    assert r.status_code == 422
