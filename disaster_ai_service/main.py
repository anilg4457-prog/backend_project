# from fastapi import FastAPI
# from routes import ingest, predict
# from models import Base
# from common.database import engine

# Base.metadata.create_all(bind=engine)

# app = FastAPI(title="Disaster AI Service")
# app.include_router(ingest.router, prefix="/ingest")
# app.include_router(predict.router, prefix="/predict")



from fastapi import FastAPI

app = FastAPI(title="Disaster AI Service")

@app.get("/")
async def root():
    return {"message": "Disaster AI Service is running"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.post("/ingest")
async def ingest_data():
    return {"message": "Data ingestion endpoint"}

@app.post("/predict")
async def predict_disaster():
    return {"message": "Prediction endpoint", "prediction": "safe"}





# in many.py or main.py of each service
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}
