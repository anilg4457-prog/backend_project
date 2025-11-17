# FROM python:3.11-slim

# WORKDIR /app

# COPY ./disaster_ai_service /app
# COPY ./common /app/common

# RUN pip install --no-cache-dir -r /app/requirements.txt

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.11-slim

WORKDIR /app

# Copy all disaster_ai_service contents
COPY ./disaster_ai_service /app
COPY ./common /app/common

RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]