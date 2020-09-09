import environ
from pathlib import Path


BASE_DIR = Path(__file__, resolve=True).parent.parent
ENV_FILE = BASE_DIR / ".env"

env = environ.Env(
    # set casting, default value
    HOST=str,
    API_TOKEN=str,
)
# reading .env file
environ.Env.read_env(str(ENV_FILE))

HOST = env("HOST")
API_TOKEN = env("API_TOKEN")
