import os

# Statement for enabling the development enviroment
DEBUG = True

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# MongoDB settings
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'app'

UPLOAD_FOLDER = '/static/img/'
