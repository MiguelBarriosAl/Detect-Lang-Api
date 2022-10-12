from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.openapi.models import Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.model.model import predict_pipeline

app = FastAPI()

__version__ = "0.1.0"


class PrectionOut(BaseModel):
    text: str


class TextIn(BaseModel):
    text: str


@app.get("/")
def home():
    response = {
        "HealthCheck": "Ok",
        "Version": __version__

    }
    return JSONResponse(content=response, media_type="application/json")


@app.post("/predict", response_model=BaseModel)
async def predict(payload: TextIn):
    lang = predict_pipeline(payload)
    response = {
        "language": lang
    }
    return JSONResponse(content=response, media_type="application/json")
