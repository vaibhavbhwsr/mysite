FROM python:latest

ENV PYTHONUNBUFFERED=1

WORKDIR /webapp

COPY . /webapp/

RUN pip install -r requirements.dev.txt