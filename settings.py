
import os
from dotenv import load_dotenv

_dotenv_name = '.env.'
_dotenv_file = os.path.join(os.path.dirname(__file__), _dotenv_name + 'development')

load_dotenv(dotenv_path=_dotenv_file, verbose=True)


SQLALCHEMY_DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URI')
PROJECT_NAME = "Web Service Rest"
HOST = 'localhost'
PORT = 5000
RELOAD = True
BACKEND_CORS_ORIGINS = []
CLIENT = 'client'
SALESMAN = 'salesman'
ADMIN = 'admin'
