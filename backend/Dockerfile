FROM python:3.9-slim

MAINTAINER Clanhouse

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && apt-get install -y netcat

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

ADD ./app /app
COPY gh_robber.py /app
COPY config.py /app
COPY .flaskenv /app

CMD python gh_robber.py