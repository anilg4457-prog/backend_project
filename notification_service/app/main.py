from fastapi import FastAPI
from .routes import notify
from common.database import Base, engine
Base.metadata.create_all(bind=engine)
app = FastAPI(title="Notification Service")
app.include_router(notify.router, prefix="/notify")




# in many.py or main.py of each service
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}
