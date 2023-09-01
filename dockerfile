FROM python:3.9

RUN apt-get -y update

RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs postgresql-client netcat-traditional

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app

COPY . .
