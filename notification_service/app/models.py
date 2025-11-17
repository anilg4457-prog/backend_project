from sqlalchemy import Column, Integer, String, DateTime, JSON
from common.database import Base
import datetime

class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, index=True)
    recipient = Column(String, nullable=False)
    subject = Column(String)
    body = Column(String)
    meta = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
