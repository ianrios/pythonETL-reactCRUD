FROM python:3.9

RUN apt-get -y update

RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs postgresql-client netcat-traditional

RUN pip install flask

COPY entrypoint.sh /entrypoint.sh
EXPOSE 5000
EXPOSE 5001
EXPOSE 3000
ENTRYPOINT ["/entrypoint.sh"]

