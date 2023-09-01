# Assignment 3 - Working with APIs

- [x] start the docker container with the provided Postgres database. `docker-compose up db -d`
- [ ] database will automatically be populated with a `interview_db.covid_state_stats` table
  - [x] confirm this and connect to the database
  - [ ] make sure the table is there and has data.
- [x] install the project's dependencies, then run the flask application:
- [x] create a new api endpoint to serve records from the `covid_state_stats` table.

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
- [x] get dockerfile to work correctly
- [x] connect to db via the covid stats endpoint
- [x] get api connection to use port 5001

## Optimizations to try

- [ ] use orm?
