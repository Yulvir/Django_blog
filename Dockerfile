FROM python:3.6
ENV PYTHONUNBUFFERED 1
COPY . /code/
WORKDIR /code/
RUN pip install -r requirements.txt
EXPOSE 8000


# correr las migraciones: sudo docker-compose run web python3 manage.py migrate
# levantar el contenedor: sudo docker-compose up
# construir la imagen: sudo docker-compose up