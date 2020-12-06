FROM python:3.8-alpine

MAINTAINER Srinaveen Desu

#EXPOSE 5050

COPY ./requirements.txt /requirements.txt

WORKDIR ./

RUN apk add --update \
  && apk add gcc libc-dev make git libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev \
  libjpeg-turbo-dev jpeg-dev \
  && pip install --upgrade pip  \
  && pip install -r requirements.txt \
  && rm -rf /var/cache/apk/*

COPY ./flaskblog /flaskblog
COPy ./run.py /

CMD python run.py