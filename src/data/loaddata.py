import asyncio

from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_URL, MONGO_DATABASE, MONGO_COLLECTION

client = AsyncIOMotorClient(MONGO_URL)
db = client[MONGO_DATABASE]
collection = db[MONGO_COLLECTION]

async def insert_documents():
    await collection.delete_many({})
    forms = (
        {'name': 'Registration', 'email': 'email', 'phone': 'phone'},
        {
            'name': 'Profile',
            'first_name': 'text',
            'birthday': 'date',
            'city': 'text'
        },
        {'name': 'Confirmation', 'username': 'text', 'email': 'email'}
    )
    await collection.insert_many(forms)
    print(f'Данные импортированы в коллекцию {collection.name}.')


asyncio.run(insert_documents())
