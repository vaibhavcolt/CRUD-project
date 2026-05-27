# Django REST Framework Backend Assignment

This project provides a robust, production-style backend API built with Django and Django REST Framework. It features a scalable service-layer architecture, strict validation, standard response formatting, JWT authentication, and full Docker support.

## Architecture & Flow

The codebase is organized following a **Service Layer Architecture**:
1. **Views (`views.py`)**: Handle HTTP requests, apply serializers for validation, and manage pagination. They do *not* contain business logic.
2. **Serializers (`serializers.py`)**: Responsible for strict data validation (e.g., email format, required fields).
3. **Services (`services.py`)**: House the core business logic. Views pass validated data to services which interact with models. This separation makes testing and reusability much easier.
4. **Exceptions (`exceptions.py`)**: Intercepts DRF exceptions and formats them into the required `{"success": false, "error": "Message"}` standard.
5. **Utils (`utils.py`)**: Provides helpers for formatting successful JSON responses.

## Setup Instructions (Docker)

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

## Setup Instructions (Local)

1. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the `.env` file. (By default, if DB variables aren't provided or MySQL isn't running locally, SQLite fallback is enabled for quick testing).
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Run the server:
   ```bash
   python manage.py runserver
   ```

## Endpoints Overview

- `GET /users` - Fetch all users with pagination and search (`/users?page=1&limit=10&search=john`).
- `POST /users` - Create a new user (Validations: Email format, duplicate email check).
- `GET /users/<id>` - Retrieve a specific user (Handles "User not found" gracefully).
- `POST /api/token/` - Obtain JWT tokens.
- `POST /api/token/refresh/` - Refresh JWT tokens.

## Response Formatting

**Success:**
```json
{
  "success": true,
  "message": "User fetched successfully",
  "data": { ... }
}
```

**Error:**
```json
{
  "success": false,
  "error": "Duplicate email"
}
```
# CRUD-project
# CRUD-project
