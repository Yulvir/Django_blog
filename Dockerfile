FROM ubuntu:16.04
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN apt-get -y update
#RUN apt-get -y upgrade
RUN apt-get -y install software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install python3
RUN apt-get install -y  python-pip
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
