# Continuous Control Monitoring

## Overview
A real-world AI-powered compliance control monitoring system built with Spring Boot, MySQL, Redis, and Docker.

## Tech Stack
- Java 17 + Spring Boot 3.2.5
- MySQL 8.0
- Redis 7
- Flyway (DB migrations)
- Spring Security + JWT
- Docker + Docker Compose

## Setup Instructions
1. Clone the repo
2. Copy `.env.example` to `.env` and fill in values
3. Run `docker-compose up --build`
4. Access API at `http://localhost:8080`
5. Access Swagger UI at `http://localhost:8080/swagger-ui.html`

## Default Login
- Username: `admin`
- Password: `Admin@1234`

## API Endpoints
- POST `/api/auth/login` - Login
- POST `/api/auth/register` - Register
- GET `/api/controls` - Get all controls
- POST `/api/controls` - Create control
- PUT `/api/controls/{id}` - Update control
- DELETE `/api/controls/{id}` - Delete control
- GET `/api/controls/stats` - Dashboard stats
- GET `/api/controls/search` - Search controls
- GET `/api/controls/export` - Export CSV

## Known Issues (P3)
- Swagger UI authorization has a browser CORS limitation in development mode
    - Workaround: Use terminal commands with Bearer token
- Redis must be running for caching to work