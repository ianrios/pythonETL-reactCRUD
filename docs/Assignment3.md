# Assignment 3 - Working with APIs


- [x] start the docker container with the provided Postgres database. `docker-compose up db -d`
- [ ] database will automatically be populated with a `interview_db.covid_state_stats` table - confirm this and connect to the database to make sure the table is there and has data. 
- [x] install the project's dependencies, then run the flask application:
```sh
$ python -m api

# Use provided endpoint to verify that flask is able to establish a tcp connection with the database.
$ curl http://localhost:5001/covid-stats/test-db-connection

# If debugging the api in docker, add the host=host.docker.internal to the url.
$ curl http://localhost:5001/covid-stats/test-db-connection?host=host.docker.internal
```

- [x] create a new api endpoint to serve records from the `covid_state_stats` table.

The database credentials can be found by looking up the environment variables that were injected into flask from `.env`.

```python
# use host.docker.internal instead of localhost if debugging the api in docker
# host = "host.docker.internal"
host = localhost
port = 5432
user = os.environ["POSTGRES_USER"]
password = os.environ["POSTGRES_PASSWORD"]
db = os.environ["POSTGRES_DB"]
```

Success criteria:

- [ ] Records from the `covid_state_stats` table are served via the new endpoint.
- [ ] Records are served in json format.
- [ ] Datetime fields are in the ISO 8601 format.
- [ ] Results are paginated.


## Tasks

- [x] what is flask
- [ ] get pgadmin or other db viewing tool to work
- [ ] does flask have an orm?
- [ ] does flask have a cli to build boilerplate?
- [ ] get dockerfile to work correctly
- [ ] connect to db via the covid stats endpoint
- [ ] get connection to use correct 5001 port, instead of default 5000 port



## Optimizations to try

- [ ] use orm?