from fastapi import APIRouter, BackgroundTasks, Depends
from sqlalchemy.orm import Session
from common.database import SessionLocal
from ..models import Notification
from pydantic import BaseModel
import smtplib, os

router = APIRouter()

class NotifyIn(BaseModel):
    recipient: str
    subject: str
    body: str
    meta: dict = {}

def get_db():
    db = SessionLocal(); 
    try: yield db
    finally: db.close()

def send_email_sync(recipient, subject, body):
    SMTP_HOST = os.getenv("SMTP_HOST")
    SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
    SMTP_USER = os.getenv("SMTP_USER")
    SMTP_PASS = os.getenv("SMTP_PASS")
    message = f"Subject: {subject}\n\n{body}"
    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as smtp:
            smtp.starttls()
            smtp.login(SMTP_USER, SMTP_PASS)
            smtp.sendmail(SMTP_USER, recipient, message)
    except Exception as e:
        print("Email error:", e)

@router.post("/send")
def send_notify(payload: NotifyIn, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    n = Notification(recipient=payload.recipient, subject=payload.subject, body=payload.body, meta=payload.meta)
    db.add(n); db.commit(); db.refresh(n)
    background_tasks.add_task(send_email_sync, payload.recipient, payload.subject, payload.body)
    return {"status": "queued", "id": n.id}
