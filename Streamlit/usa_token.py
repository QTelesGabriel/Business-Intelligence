import os
from dotenv import load_dotenv

load_dotenv()

class settings:
    kaggle_username = os.getenv("KAGGLE_USERNAME")
    kaggle_key = os.getenv("KAGGLE_KEY")