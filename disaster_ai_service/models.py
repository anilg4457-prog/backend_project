from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Add your database models here later
# Example:
# class DisasterPrediction(Base):
#     __tablename__ = "predictions"
#     id = Column(Integer, primary_key=True, index=True)
#     prediction = Column(String)
#     confidence = Column(Float)