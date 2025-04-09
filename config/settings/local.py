from os import getenv
from dotenv import load_dotenv
from pathlib import Path
from .base import *  # noqa
from .base import BASE_DIR

# Load .env.local file from BASE_DIR
env_path = BASE_DIR / ".envs/.env.local"
print(">>> ENV PATH:", env_path)

if env_path.exists():
    print(">>> .env.local FOUND, loading...")
    load_dotenv(dotenv_path=env_path)
else:
    print(">>> .env.local NOT FOUND, skipping environment variable loading.")

SECRET_KEY = getenv("SECRET_KEY")

DEBUG = getenv("DEBUG", "False").lower() == "true"

SITE_NAME = getenv("SITE_NAME")

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]

ADMIN_URL = getenv("ADMIN_URL")

EMAIL_BACKEND = "djcelery_email.backends.Celery.EmailBackend"
EMAIL_HOST = getenv("EMAIL_HOST")
EMAIL_PORT = getenv("EMAIL_PORT")
DEFAULT_FROM_EMAIL = getenv("DEFAULT_FROM_EMAIL")
DOMAIN = getenv("DOMAIN")

MAX_UPLOAD_SIZE = 1 * 1024 * 1024
