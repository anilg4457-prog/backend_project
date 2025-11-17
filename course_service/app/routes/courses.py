from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from common.database import SessionLocal
# from app.models import Course   # <-- FIXED
from pydantic import BaseModel
from common.models import Course




router = APIRouter()

class CourseIn(BaseModel):
    title: str
    description: str = ""

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=dict)
def create_course(course: CourseIn, db: Session = Depends(get_db)):
    c = Course(title=course.title, description=course.description)
    db.add(c)
    db.commit()
    db.refresh(c)
    return {"id": c.id, "title": c.title}
