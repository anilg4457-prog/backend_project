from fastapi import FastAPI
from app.routes import auth
from common.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Auth Service")
app.include_router(auth.router, prefix="/auth")




# in many.py or main.py of each service
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}
