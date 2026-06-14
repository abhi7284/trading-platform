# Trading Platform

A production-grade algorithmic trading platform built using FastAPI, PostgreSQL, Redis, and Docker.

---

## Documentation

Project Tracking & Design Notes:

https://app.notion.com/p/37f9ae5781f28085a40ac5aac2d9f4cd?v=37f9ae5781f2804db1a0000c71927714&source=copy_link

---

## Project Vision

The goal of this project is to build a scalable trading platform capable of:

* User Authentication & Authorization
* Broker Integration (Upstox, Zerodha, etc.)
* Market Data Streaming
* Order Management
* Portfolio Tracking
* Position Management
* Risk Management
* Strategy Execution
* Real-Time Monitoring

---

## Technology Stack

### Backend

* Python 3.12+
* FastAPI
* SQLAlchemy
* Alembic

### Database

* PostgreSQL

### Cache & Messaging

* Redis

### Infrastructure

* Docker
* Docker Compose

### Security

* JWT Authentication
* Password Hashing (bcrypt)

---

## Architecture

```text
Client
   │
   ▼
FastAPI
   │
   ├── Controllers
   │
   ├── Services
   │
   ├── Repositories
   │
   ▼
PostgreSQL

Redis
```

---

## Project Structure

```text
trading-platform/

├── api/
│   ├── controllers/
│   └── schemas/
│
├── services/
├── repositories/
├── models/
│
├── database/
│
├── migrations/
│
├── config/
│
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── main.py
```

---

## Features Completed

### Infrastructure

* Dockerized environment
* PostgreSQL integration
* Redis integration
* Environment-based configuration

### Database

* SQLAlchemy ORM setup
* Alembic migration setup
* User table creation

### Authentication

* User Registration
* User Login
* Password Hashing
* JWT Token Generation
* JWT Token Validation
* Protected Endpoints

---

## Local Development Setup

### Clone Repository

```bash
git clone <repository-url>
cd trading-platform
```

### Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
APP_NAME=Trading Platform

DATABASE_URL=postgresql://postgres:postgres@localhost:5432/trading

JWT_SECRET=change-me
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=60
```

---

## Start Infrastructure

```bash
docker-compose up -d
```

Verify:

```bash
docker ps
```

Expected containers:

```text
trading-postgres
trading-redis
trading-api
```

---

## Database Migration

Generate Migration:

```bash
alembic revision --autogenerate -m "migration name"
```

Apply Migration:

```bash
alembic upgrade head
```

Check Current Version:

```bash
alembic current
```

Migration History:

```bash
alembic history
```

---

## Running Application

Local:

```bash
uvicorn main:app --reload
```

Docker:

```bash
docker-compose up
```

Application:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

---

## API Endpoints

### Register User

```http
POST /auth/register
```

Request:

```json
{
  "name": "Abhishek",
  "email": "abhishek@gmail.com",
  "password": "secret123"
}
```

---

### Login

```http
POST /auth/login
```

Request:

```json
{
  "email": "abhishek@gmail.com",
  "password": "secret123"
}
```

Response:

```json
{
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}
```

---

### Current User

```http
GET /auth/me
```

Headers:

```text
Authorization: Bearer <JWT_TOKEN>
```

---

## Example cURL Commands

### Register

```bash
curl -X POST http://localhost:8000/auth/register \
-H "Content-Type: application/json" \
-d '{
"name":"Abhishek",
"email":"abhishek@gmail.com",
"password":"secret123"
}'
```

### Login

```bash
curl -X POST http://localhost:8000/auth/login \
-H "Content-Type: application/json" \
-d '{
"email":"abhishek@gmail.com",
"password":"secret123"
}'
```

### Current User

```bash
curl -X GET http://localhost:8000/auth/me \
-H "Authorization: Bearer <TOKEN>"
```

---

## Development Roadmap

### Phase 1 — Foundation ✅

* User Management
* Authentication
* JWT Security
* PostgreSQL
* Redis
* Docker

### Phase 2 — Broker Integration

* Upstox OAuth
* Broker Account Linking
* Token Management
* Holdings API
* Positions API

### Phase 3 — Trading Core

* Order Placement
* Order Modification
* Order Cancellation
* Order History

### Phase 4 — Market Data

* WebSocket Integration
* Live Tick Processing
* Redis Caching

### Phase 5 — Strategy Engine

* Strategy Framework
* Signal Generation
* Automated Trading

### Phase 6 — Risk Management

* Position Limits
* Daily Loss Limits
* Exposure Controls

---

## Current Status

Version: 0.1.0

Status:

✅ Infrastructure Ready

✅ Authentication Ready

✅ Database Ready

🚧 Broker Integration Next

🚧 Trading Engine Pending

🚧 Strategy Engine Pending
