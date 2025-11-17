from fastapi import APIRouter, UploadFile, File
from typing import List

router = APIRouter(prefix="/api/v1", tags=["ingest"])

@router.post("/ingest")
async def ingest_data(file: UploadFile = File(...)):
    return {"message": "Data ingestion endpoint", "filename": file.filename}

@router.get("/ingest/status")
async def get_ingestion_status():
    return {"status": "ingestion service ready"}