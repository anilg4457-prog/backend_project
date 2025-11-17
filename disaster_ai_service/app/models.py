from sqlalchemy import Column, Integer, String, DateTime, JSON, Float, Boolean
from common.database import Base
import datetime

class Observation(Base):
    __tablename__ = "observations"
    id = Column(Integer, primary_key=True, index=True)
    region_id = Column(Integer)
    timestamp = Column(DateTime)
    data = Column(JSON)

class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True, index=True)
    region_id = Column(Integer)
    run_ts = Column(DateTime, default=datetime.datetime.utcnow)
    model_version = Column(String)
    predicted_value = Column(Float)
    alert_sent = Column(Boolean, default=False)
