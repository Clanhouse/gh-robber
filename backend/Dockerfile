# pull official base image
FROM python:3.8

# set work directory
WORKDIR /gh_robber-app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat

# install dependencies
COPY ./requirements.txt /gh_robber-app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY ./gh_robber-app

# run entrypoint.sh
#ENTRYPOINT ["/gh_robber-app/entrypoint.sh"]

CMD ["python", "./gh_robber.py"]