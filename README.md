# django-bankMS

Foundation of a banking API built with Django and Django REST Framework. Learning project built while following a Django course. Work in progress: the user and authentication layer is in place, banking features (accounts, transactions) are not implemented yet.

## What is in the code
- Custom `User` model with account status, failed login attempts, and account lockout
- One-time-password (OTP) with expiry time, plus OTP and account-locked email templates
- User profile app
- API schema and docs with drf-spectacular (Swagger UI at `/api/v1/schema/swagger-ui/`, ReDoc at `/api/v1/schema/redoc/`)
- Split settings (`base`, `local`, `production`)
- Docker setup: Django, PostgreSQL, Redis, RabbitMQ, Celery worker / beat / Flower, nginx, Mailpit

## Tech stack
Python, Django, Django REST Framework, PostgreSQL, Celery, Redis, RabbitMQ, Docker, nginx, Argon2 password hashing

## Run locally
Create the env file the compose file expects at `.envs/.env.local`, then:
```bash
make build
make up
make migrate
make superuser
```
See `Makefile` and `local.yml` for the other commands (`down`, `collectstatic`, `makemigrations`, `flush`) and services.
