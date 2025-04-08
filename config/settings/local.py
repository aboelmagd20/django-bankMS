from os import path, getenv
from dotenv import load_dotenv
from .base import * #noqa
from .base import BASE_DIR

# Load environment variables from .env file
local_env_path = path.join(BASE_DIR, ".env", ".env.local")

if path.isfile(local_env_path):
    load_dotenv(local_env_path)

SECRET_KEY = getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getenv("DEBUG") 

SITE_NAME = getenv("SITE_NAME")

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]

ADMIN_URL = getenv("ADMIN_URL")

EMAIL_BACKEND = "djcelery_email.backends.Celery.EmailBackend"
EMAIL_HOST = getenv("EMAIL_HOST")
EMAIL_PORT = getenv("EMAIL_PORT")
DEFAULT_FROM_EMAIL = getenv("DEFAULT_FROM_EMAIL")
DOMAIN = getenv("DOMAIN")

MAX_UPLOAD_SIZE = 1 * 1024 * 1024