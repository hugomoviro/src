from dotenv import load_dotenv
import os

load_dotenv()

FLASK_DEBUG = os.getenv("FLASK_DEBUG")
SECRET_KEY = os.getenv("SECRET_KEY")