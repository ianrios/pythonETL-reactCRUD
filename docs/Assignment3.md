# Assignment 3 - Working with APIs

- Start via `docker compose up --build -d`

- [x] start the docker container with the provided Postgres database. `docker-compose up db -d`
- [x] database will automatically be populated with a `interview_db.covid_state_stats` table
  - [x] confirm this and connect to the database
  - [x] make sure the table is there and has data.
- [x] install the project's dependencies, then run the flask application:
- [x] create a new api endpoint to serve records from the `covid_state_stats` table.

Success criteria:

- [x] Records from the `covid_state_stats` table are served via the new endpoint.
- [x] Records are served in json format.
- [ ] Datetime fields are in the ISO 8601 format.
- [ ] Results are paginated.

## Tasks

- [x] what is flask
- [ ] get pgadmin or other db viewing tool to work - didnt need to once db connection started working
- [ ] does flask have an orm?
- [ ] does flask have a cli to build boilerplate?
- [x] get dockerfile to work correctly
- [x] connect to db via the covid stats endpoint
- [x] get api connection to use port 5001
- [ ] clean up dockerfile - install packages elsewhere
- [ ] make database connection method
- [ ] research how to make a paginated db call based on path params

## Optimizations to try

- [ ] use orm?

## Notes

- This one was probably the most annoying, but only because I had to edit the docker instance to play nicely with my machine. That took probably a good 8 hours just to configure docker to work with my machine. I ended up scrapping the dev container and splitting the services into an api container, and a ui container alongsize the database container. it made it easier to read the logs from each server for me and also allowed me to spin up just one server at a time
-
