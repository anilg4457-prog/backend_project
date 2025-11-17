from fastapi import FastAPI
from .routes import admin
from common.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Admin Service")
app.include_router(admin.router, prefix="/admin")




# in many.py or main.py of each service
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}
