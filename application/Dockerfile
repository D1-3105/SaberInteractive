FROM python:3.10
RUN mkdir /var/log/application
RUN mkdir /Saber
RUN mkdir /builds
COPY core /Saber/core
COPY builds /builds/
COPY requirements.txt /Saber/
COPY .env-docker /Saber/.env
RUN pip install -r /Saber/requirements.txt

WORKDIR /Saber/

