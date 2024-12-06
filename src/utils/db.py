from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_URL, MONGO_DATABASE, MONGO_COLLECTION

client = AsyncIOMotorClient(MONGO_URL)
db = client[MONGO_DATABASE]
collection = db[MONGO_COLLECTION]
