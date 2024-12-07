# Используем базовый образ Python
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY /src /app
COPY /tests/script.py /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]