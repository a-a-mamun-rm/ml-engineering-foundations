"""Request/response schemas: invalid input is rejected before it reaches the model."""
from typing import Literal

from pydantic import BaseModel, Field


class Patient(BaseModel):
    Age: int = Field(ge=1, le=120)
    Sex: Literal["M", "F"]
    ChestPainType: Literal["ASY", "NAP", "ATA", "TA"]
    RestingBP: float = Field(ge=0, le=300, description="0 = not measured")
    Cholesterol: float = Field(ge=0, le=1000, description="0 = not measured")
    FastingBS: Literal[0, 1]
    RestingECG: Literal["Normal", "LVH", "ST"]
    MaxHR: float = Field(ge=40, le=250)
    ExerciseAngina: Literal["N", "Y"]
    Oldpeak: float = Field(ge=-5, le=10)
    ST_Slope: Literal["Up", "Flat", "Down"]


class Prediction(BaseModel):
    risk: float = Field(ge=0, le=1)
    model_version: str
