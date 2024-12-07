import asyncio

import pytest
from httpx import AsyncClient, ASGITransport
from motor.motor_asyncio import AsyncIOMotorClient

import config
from main import app


@pytest.fixture(scope="session")
def event_loop():
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='session')
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope='function')
async def collection():
    client = AsyncIOMotorClient(config.MONGO_URL)
    db = client[config.MONGO_DATABASE]
    collection = db[config.MONGO_COLLECTION]
    await collection.delete_many({})
    yield collection
    await collection.delete_many({})


@pytest.fixture
async def forms(collection):
    forms = (
        {'form_name': 'Registration', 'email': 'email', 'phone': 'phone'},
        {
            'form_name': 'Profile',
            'first_name': 'text',
            'birthday': 'date',
            'city': 'text'
        },
        {'form_name': 'Confirmation', 'username': 'text', 'email': 'email'}
    )
    await collection.insert_many(forms)


@pytest.fixture
async def client():
    async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url='http://test'
    ) as client:
        yield client


@pytest.fixture
def valid_form_data(forms):
    form_data = (
        (
            {'email': 'bob@example.com', 'phone': '+79009001122'},
            'Registration'
        ),
        (
            {
                'first_name': 'bob',
                'birthday': '2000-12-31',
                'city': 'New York'
            },
            'Profile'
        ),
        (
            {'username': 'bob', 'email': 'bob@example.com'},
            'Confirmation'
        )
    )
    return form_data

@pytest.fixture
def invalid_form_data(forms):
    form_data = (
        (
            {'email': 'example', 'phone': '+79009001122'},
            {'email': 'text', 'phone': 'phone'}
        ),
        (
            {
                'name': 'bob',
                'birthday': '2000-12-31',
                'city': 'New York',
                'phone': '+79009001122',
                'email': 'bob@example.com'
            },
            {
                'name': 'text',
                'birthday': 'date',
                'city': 'text',
                'phone': 'phone',
                'email': 'email'
            }
        ),
        (
            {'username': '2024-12-31', 'email': 'bob@example.com'},
            {'username': 'date', 'email': 'email'}
        ),
        (
            {'': ''},
            {'': 'text'}
        ),
        (
            {'email': 123},
            {'email': 'unknown'}
        ),
        (
            {'phone': True},
            {'phone': 'unknown'}
        )
    )
    return form_data
