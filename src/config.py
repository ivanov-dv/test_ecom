import os

from dotenv import load_dotenv

load_dotenv()

TEST_MODE = os.getenv('TEST_MODE', 'false')

MONGO_URL = os.getenv(
    'MONGO_URL',
    'mongodb://localhost:27017'
)
MONGO_DATABASE = 'test' if TEST_MODE == 'true' else os.getenv('MONGO_DATABASE')
MONGO_COLLECTION = 'test' if TEST_MODE == 'true' else os.getenv('MONGO_COLLECTION')
