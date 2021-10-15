import os

from dotenv import load_dotenv

load_dotenv(".env")


HOST = os.environ["HOST"]
API_TOKEN = os.environ["API_TOKEN"]
