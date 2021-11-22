# pull official base image
FROM python:3.8-alpine

MAINTAINER Clanhouse

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat

# install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY ./app /app

# run entrypoint.sh
#ENTRYPOINT ["/gh_robber-app/entrypoint.sh"]

CMD ["python", "./gh_robber.py"]