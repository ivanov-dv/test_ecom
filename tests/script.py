import asyncio

import httpx
from colorama import Fore, Style

from utils.db import collection


async def insert_documents():
    await collection.delete_many({})
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
    print(f'Данные импортированы в коллекцию {collection.name}\n.')


async def send_requests():
    data = (
        (
            {'email': 'bob@example.com', 'phone': '+79009001122'},
            {'form_name': 'Registration'}
        ),
        (
            {
                'first_name': 'bob',
                'birthday': '2000-12-31',
                'city': 'New York'
            },
            {'form_name': 'Profile'}

        ),
        (
            {
                'city': 'New York',
                'birthday': '2000-12-31',
            },
            {'form_name': 'Profile'}

        ),
        (
            {'username': 'bob', 'email': 'bob@example.com'},
            {'form_name': 'Confirmation'}
        ),
        (
            {'email': 'example', 'phone': '+79009001122'},
            {'email': 'text', 'phone': 'phone'}
        ),
        (
            {
                'name': 'bob',
                'birthday': '2000-12-31',
                'city': 'New York'
            },
            {
                'name': 'text',
                'birthday': 'date',
                'city': 'text'
            }
        ),
        (
            {'username': '2024-12-31', 'email': 'bob@example.com'},
            {'username': 'date', 'email': 'email'}
        ),
        (
            {'': ''},
            {'': 'text'}
        )
    )
    async with httpx.AsyncClient() as client:
        for request, expected in data:
            print(f'Отправка запроса {request}')
            response = await client.post(
                'http://localhost:8000/get_form',
                json=request
            )
            response_json = response.json()
            print(f'Получен ответ {response_json}\n'
                  f'Ожидаемый ответ {expected}')
            if response_json == expected:
                print(Fore.GREEN + 'Тест пройден успешно\n' + Style.RESET_ALL)
            else:
                print(Fore.RED + 'Тест не пройден\n' + Style.RESET_ALL)


async def main():
    await insert_documents()
    await send_requests()


asyncio.run(main())
