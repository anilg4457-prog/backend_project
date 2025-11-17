from fastapi import FastAPI
from app.routes import courses
from common.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Course Service")
app.include_router(courses.router, prefix="/courses")




# in many.py or main.py of each service
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "true"}
