FROM python:3.6

ENV PYTHONUNBUFFERED 1

COPY . /code/
WORKDIR /code/

RUN pip install pipenv
RUN pipenv install
RUN pipenv install psycopg2

EXPOSE 8000