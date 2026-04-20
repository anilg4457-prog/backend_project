# Backend Project (Auth, Courses, Notification, Admin, Disaster AI)

This repository contains a minimal but complete backend skeleton for:
- auth_service
- course_service
- notification_service
- admin_service
- disaster_ai_service

Included:
- Dockerfiles for each service
- docker-compose.yml to run everything locally (includes Postgres)
- common utilities for DB and config
- basic FastAPI apps for each service

Instructions:
1. Copy `.env.example` to `.env` and edit values.
2. Build and run: `docker compose up --build`
3. Services:
   - Auth: http://localhost:8001
   - Course: http://localhost:8002
   - Notification: http://localhost:8003
   - Admin: http://localhost:8004
   - Disaster AI: http://localhost:8005

Train model (optional):
- Provide training CSV at `disaster_ai_service/data/processed/flood_features.csv` and run `python app/models/train.py` inside the disaster_ai_service container or locally.

