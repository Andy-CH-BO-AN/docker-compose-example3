FROM python:3.9

WORKDIR /usr/app/src

COPY test_connect_mysql.py requirements.txt ./

RUN pip install -r requirements.txt