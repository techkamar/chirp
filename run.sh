#!/usr/bin/bash
source ../chirpvenv/bin/activate

# All ENV variables needed to run
export DB_NAME="chirp"
export DB_USER="postgres"
export DB_PASS="chirp"
export DB_HOST="localhost"
export DB_PORT="5432"
export JWT_SECRET_KEY="my-secret"


# Start Server
uvicorn app.main.main:app --host 0.0.0.0 --port 8080