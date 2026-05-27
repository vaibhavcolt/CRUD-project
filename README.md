# User Management API

A RESTful User Management API built using Django REST Framework and MySQL. This project provides a robust, production-style backend API featuring a scalable service-layer architecture, strict validation, standard response formatting, JWT authentication, and full Docker support.

---

# Tech Stack

- Python
- Django
- Django REST Framework
- MySQL
- JWT Authentication
- Docker

---

# Architecture & Flow

The codebase is organized following a **Service Layer Architecture**:
1. **Views (`views.py`)**: Handle HTTP requests, apply serializers for validation, and manage pagination. They do *not* contain business logic.
2. **Serializers (`serializers.py`)**: Responsible for strict data validation (e.g., email format, required fields).
3. **Services (`services.py`)**: House the core business logic. Views pass validated data to services which interact with models. This separation makes testing and reusability much easier.
4. **Exceptions (`exceptions.py`)**: Intercepts DRF exceptions and formats them into the required `{"success": false, "error": "Message"}` standard.
5. **Utils (`utils.py`)**: Provides helpers for formatting successful JSON responses.

---

# Project Structure

```bash
project/
│
├── users/
│   ├── models/
│   ├── services/
│   ├── serializers/
│   ├── views/
│   ├── urls/
│   └── utils/
│
├── config/
├── manage.py
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
└── README.md
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/vaibhavcolt/CRUD-project.git
cd CRUD-project
```

## 2. Using Docker (Recommended)

The easiest way to run the project is using Docker Compose, which spins up both the Django web server and a MySQL database container.

1. Ensure Docker and Docker Compose are installed.
2. Create a `.env` file (you can copy from `.env.example`):
   ```bash
   cp .env.example .env
   ```
3. Build and start the containers:
   ```bash
   docker-compose up --build
   ```
4. The API will be available at `http://localhost:8000`.

## 3. Local Setup

### Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

**Windows**
```bash
venv\Scripts\activate
```

**Linux/Mac**
```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure MySQL Database

Create MySQL database:

```sql
CREATE DATABASE users;
```

Update database configuration in `.env`:
```env
DB_NAME=users
DB_USER=root
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=3306
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Start Server

```bash
python manage.py runserver
```

Server will run at:
```bash
http://127.0.0.1:8000/
```

---

# Database Schema

## Table: users

| Column | Type | Constraints |
|---|---|---|
| id | Integer | Primary Key |
| name | Varchar(255) | Not Null |
| email | Varchar(255) | Unique, Not Null |
| role | Varchar(100) | Not Null |

---

# API Endpoints

## 1. Get All Users

### Endpoint
```http
GET /users
```

### Query Parameters
- `page` (optional): Page number for pagination
- `limit` (optional): Number of records per page
- `search` (optional): Search term for filtering by name or email

### Response
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "name": "Vaibhav",
      "email": "vaibhav@gmail.com",
      "role": "Developer"
    }
  ]
}
```

---

## 2. Create User

### Endpoint
```http
POST /users
```

### Request Body
```json
{
  "name": "Vaibhav",
  "email": "vaibhav@gmail.com",
  "role": "Developer"
}
```

### Response
```json
{
  "success": true,
  "message": "User created successfully"
}
```

---

## 3. Get User By ID

### Endpoint
```http
GET /users/1
```

### Response
```json
{
  "success": true,
  "data": {
    "id": 1,
    "name": "Vaibhav",
    "email": "vaibhav@gmail.com",
    "role": "Developer"
  }
}
```

---

## 4. Search Users

### Endpoint
```http
GET /users?search=vaibhav
```

### Response
```json
{
  "success": true,
  "data": []
}
```

---

## 5. Pagination

### Endpoint
```http
GET /users?page=1&limit=10
```

### Response
```json
{
  "success": true,
  "page": 1,
  "limit": 10,
  "total": 100,
  "data": []
}
```

---

## 6. Authentication Endpoints

### Endpoint
```http
POST /api/token/
```
Provides access and refresh tokens.

### Endpoint
```http
POST /api/token/refresh/
```
Refreshes the access token.

---

# Validation Rules

- Name is required
- Email is required
- Email must be valid
- Role is required
- Email must be unique

---

# Error Responses

## Duplicate Email
```json
{
  "success": false,
  "error": "Email already exists"
}
```

## User Not Found
```json
{
  "success": false,
  "error": "User not found"
}
```

---

# Assumptions Made

- Email is unique for every user
- Pagination defaults are handled at API level
- Search works on both name and email
- APIs return JSON responses only
- MySQL server is already installed and running
- Authentication is optional unless bonus implementation is enabled

---

# Bonus Features Implemented

- JWT Authentication
- Docker Support
- Service Layer Architecture

---

# AI Usage Declaration

## AI Tools Used
- ChatGPT

## AI-Assisted Areas
- Project structure guidance
- API planning and documentation support
- Validation and architecture suggestions
- Initial project planning and folder structure
- Guidance for Django REST Framework setup

## Manual Work & Modifications
- Implemented models, serializers, views, and services manually
- Added business logic and API integrations
- Handled validations, pagination, and error responses
- Configured MySQL database and environment setup
- Tested and debugged APIs manually
- Refactored code structure and improved implementation where required

## Understanding of Implementation
I fully understand the implementation, architecture, and code written in this project and can explain the functionality and design decisions in detail.

---

# Task 7: Short Answers

## 1. Why did you choose Django?

I chose Django because it provides a robust and scalable framework for building REST APIs quickly with clean architecture. Django REST Framework offers built-in support for serialization, validation, pagination, and class-based views, which helped in developing a modular and maintainable API-first application efficiently.

---

## 2. How would you scale this system?

To scale this system, I would:
- Add database indexing for faster queries
- Use caching tools like Redis
- Deploy multiple application instances behind a load balancer
- Containerize the application using Docker
- Use asynchronous task queues like Celery for background jobs
- Move toward microservices if the application grows significantly
- Use cloud infrastructure and auto-scaling services

---

## 3. What changes would you make for production?

For production deployment, I would:
- Add JWT authentication and role-based authorization
- Use environment variables for sensitive configurations
- Enable HTTPS and security middleware
- Add logging and monitoring
- Implement rate limiting and request throttling
- Write unit and integration tests
- Use Docker and CI/CD pipelines for deployment
- Add centralized error handling and API documentation
- Optimize database queries and improve performance
