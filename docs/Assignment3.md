# Assignment 3 - Working with APIs

## Steps for running Assignment 3 code

- Start via `docker compose up --build -d`
- navigate to `http://localhost:5001/columns`
- navigate to `http://localhost:5001/all`
- navigate to `http://localhost:5001/page`
- page around via `http://localhost:5001/page/34`

## process from readme

- [x] start the docker container with the provided Postgres database. `docker-compose up db -d`
- [x] database will automatically be populated with a `interview_db.covid_state_stats` table
  - [x] confirm this and connect to the database
  - [x] make sure the table is there and has data.
- [x] install the project's dependencies, then run the flask application:
- [x] create a new api endpoint to serve records from the `covid_state_stats` table.

Success criteria:

- [x] Records from the `covid_state_stats` table are served via the new endpoint.
- [x] Records are served in json format.
- [x] Datetime fields are in the ISO 8601 format.
- [x] Results are paginated.
  - I decided to paginate these at 100 at a time for a faster query result

## Tasks

- [x] what is flask
- [ ] get pgadmin or other db viewing tool to work - didnt need to once db connection started working
- [ ] does flask have an orm?
- [ ] does flask have a cli to build boilerplate?
- [x] get dockerfile to work correctly
- [x] connect to db via the covid stats endpoint
- [x] get api connection to use port 5001
- [x] clean up dockerfile - install packages elsewhere
- [x] make database connection method
- [x] research how to make a paginated db call based on path params

## Optimizations to try

- [ ] use orm?
- [ ] add index in seed_database.sh....
- [ ] if the url wildcard is beyond the bounds of the available records in the database, redirect url to last possible wildcard option
- [ ] if the url wildcard is not a valid type (string, negative number, etc), redirect to first page for possible wildcard
- [ ] install swagger

## Notes

- This one was probably the most annoying, but only because I had to edit the docker instance to play nicely with my machine. That took probably a good 8 hours just to configure docker to work with my machine. I ended up scrapping the dev container and splitting the services into an api container, and a ui container alongsize the database container. it made it easier to read the logs from each server for me and also allowed me to spin up just one server at a time
- it feels really good when docker works correctly
- the actual work required here was pretty minimal, so it was not too bad
