# Use an official Python runtime as a parent image
FROM python:3.8-slim
LABEL authors="ouail laamiri"

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["uvicorn", "main:app ", "--workers 4", "--host 0.0.0.0","--port 5000","--reload","--log-level info"]

