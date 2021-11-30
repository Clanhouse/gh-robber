# pull official base image
FROM python:3.9-slim

MAINTAINER Clanhouse

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat

# install dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# copy project
ADD ./app /app/app
COPY gh_robber.py /app
COPY config.py /app
COPY .flaskenv /app


COPY entrypoint.sh /app
#CMD ["python", "gh_robber.py"]

CMD ["/app/entrypoint.sh"]
