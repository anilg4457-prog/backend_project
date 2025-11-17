from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi import status
from common.database import SessionLocal
from .. import models, schemas
from ..core import security

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=schemas.UserOut)
def register(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(models.User.email == user_in.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed = security.get_password_hash(user_in.password)
    user = models.User(email=user_in.email, hashed_password=hashed, full_name=user_in.full_name)
    db.add(user); db.commit(); db.refresh(user)
    return user

@router.post("/login", response_model=schemas.Token)
def login(form_data: schemas.UserCreate, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == form_data.email).first()
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Bad credentials")
    token = security.create_access_token({"sub": user.email, "role": user.role, "user_id": user.id})
    return {"access_token": token, "token_type": "bearer"}
