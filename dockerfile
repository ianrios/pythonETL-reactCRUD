FROM python:3.9

RUN apt update

RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN apt-get install -y postgresql-client

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]