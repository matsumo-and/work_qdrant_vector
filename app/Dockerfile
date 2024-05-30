FROM python:3.8

RUN apt-get update && apt-get install -y \
    && pip install --upgrade pip \
    && pip install qdrant-client[fastembed] pandas

RUN pip install fastembed

WORKDIR /app

COPY . /app