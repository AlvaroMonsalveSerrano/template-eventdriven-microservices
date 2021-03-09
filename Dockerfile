FROM python:3.8-alpine

RUN apk add --no-cache --virtual .build-deps gcc musl-dev python3-dev
RUN apk add libpq

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

RUN apk del --no-cache .build-deps

RUN mkdir -p /app
COPY . /app/

RUN pip install -e /app

WORKDIR /app
