# Web cервис для валидации полей форм.

## Стек технологий

- **FastAPI**
- **Motor (MongoDB)**
- **Pytest**
- **Uvicorn**

## Установка и запуск через Docker Compose.
1. Клонируйте репозиторий:
`git clone git@github.com:ivanov-dv/test_ecom.git`.
2. Перейдите в папку проекта `cd test_ecom`. 
3. Переименуйте файл `.env.example` в `.env`. 
4. Выполните команду `docker compose up --build`.

#### Загрузка тестовых данных и тестирование.
1. После запуска контейнеров в docker выполните команду 
`docker exec -it fastapi_app python3 script.py`.
Данная команда запишет в БД начальные данные и выполнит их тестирование.

ВАЖНО! Данная команда при выполнении очищает данные в БД.

## Установка и запуск без Docker.
#### Для Windows вместо команды `python3` используйте `python`.
1. Клонируйте репозиторий `git clone git@github.com:ivanov-dv/test_ecom.git`.
2. Перейдите в папку проекта `cd test_ecom`.
3. Переименуйте файл `.env.example` в `.env` 
и укажите в нем настройки подключения для MongoDB.
4. Создайте виртуальное окружение `python3 -m venv venv`.
5. Активируйте виртуальное окружение:
* Для Linux/Mac `source venv/bin/activate`;
* Для Windows `venv\Scripts\activate.bat`.
6. Установите зависимости `pip install -r requirements.txt`.
7. Перейдите в папку src `cd src`.
8. Запустите приложение `uvicorn main:app --reload`. 
9. Для загрузки тестовых данных выполните из папки `test_ecom` команду 
`python3 tests/script.py`.
