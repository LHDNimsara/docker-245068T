# API - Docker Containerization Assignment

## Student Information
Name: Sadewna Atukorala
Student ID: 245008L

## Technology
This project uses Docker to containerize a small Python Flask HTTP API.

## Run
From the project directory:
docker compose up --build

## API Endpoints
GET /
http://localhost:5000/
Returns student id, name and a message

GET /health
http://localhost:5000/health
Reutrns the health status of the API

## Stop
Run: 
docker compose down

## Limitations
- The API contains only two GET nedpoints
- No databade is used
- No authentication is implemented
- Data returned by the root endpoint is static


