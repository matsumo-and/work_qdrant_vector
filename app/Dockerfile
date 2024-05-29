FROM python:3.8

RUN apt-get update && apt-get install -y \
    && pip install --upgrade pip \
    && pip install openai qdrant-client pandas python-dotenv

WORKDIR /app

COPY . /app