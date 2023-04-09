FROM python:3.11.0-alpine

ENV PYTHONUNBUFFERED 1

RUN apk --no-cache update \
    && apk add bash \ 
                gcc \
                g++ \
                libc-dev \
                musl-dev \
                libffi-dev \
                git \
                npm \
                python3-dev

WORKDIR /my-celery-worker
COPY poetry.lock pyproject.toml .
RUN pip install --upgrade pip \
    && pip install "poetry==1.2.2" \
    && poetry config virtualenvs.create false \
    && poetry install --no-root
COPY . /my-celery-worker/
