from pathlib import Path

from konfik import Konfik

BASE_DIR = Path(__file__, resolve=True).parent.parent
ENV_FILE = BASE_DIR / ".env"

konfik = Konfik(config_path=ENV_FILE)
config = konfik.config

HOST = config.HOST
API_TOKEN = config.API_TOKEN
