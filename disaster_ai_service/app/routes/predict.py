from fastapi import APIRouter

router = APIRouter(prefix="/api/v1", tags=["predict"])

@router.post("/predict")
async def predict_disaster():
    return {"message": "Prediction endpoint", "prediction": "safe"}

@router.get("/predict/models")
async def get_models():
    return {"models": ["model_v1", "model_v2"]}