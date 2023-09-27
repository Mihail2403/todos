FROM python:3.11-alpine

WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFERRED=1
COPY . .

RUN pip install --no-cache-dir -r requirements.txt