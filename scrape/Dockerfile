FROM python:3.8

RUN apt-get update && apt-get install -y \
    && pip install --upgrade pip \
    && pip install requests bs4 chromedriver-binary==125.0.6422.78 selenium

WORKDIR /scrape

COPY . /scrape