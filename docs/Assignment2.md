### Assignment 2: data modeling and db scripting:

Must answer the following questions:
- [x] What is the list of all the types of committed crimes (primary_type) in the dataset?
  - [x] select all primary types by name, no need to order by
  - [ ] can be grouped and ordered by later for additional queries
- [ ] For any given year, what type of crime (primary_type) was the most frequently committed?
  - [ ] group by year, sort by amount per primary type
  - [ ] allow hard coding of specific year to just get that years group
- [ ] What percentage of each type of crime (primary_type) ended in arrest (arrest == true)?
  - [ ] divide by total amount
  - [ ] use the same per year alongside the full db grouping
- [ ] What is the frequency of each crime type (primary_type) year over year? Imagine we want to generate datapoints to graph the number of occurrences of each crime type over every year in the dataset.
  - [ ] select data that would show trend
- [ ] For any beat, district, ward or community (only one will be provided at a time), retrieve all the unique keys of each crime incident ordered by date.
  - [ ] select where __ = input str, order by, unique


**Next**, using any preferred tools, 

- [x] script the creation of the proposed data schema
- [ ] import of the data into a Postgres database. 
- [x] start docker via `docker compose up db`
- [x] The credentials can be found in the `.env` file at the root of this project.
- [ ] confirm database available at: `jdbc:postgresql://localhost:5432/interview_db`.

**Finally**, 
- [ ] construct some sample queries that you would use to answer some of the questions listed above. 
- [ ] Consider how you would go about optimizing those queries to be run on a continuous basis by several users on a daily basis. 
- [ ] Consider what database constructs and features you would use to reduce stress on the SQL server and improve query responsiveness, given the nature of the dataset. These sample queries do not have to be exhaustive and are meant to drive the in-person conversation during the review session.

## Tasks

- [x] design database schema for exisitng ETL dataset with db diagram
- [x] identify foreign keys for easy indexing later
  - [x] primary_type
  - [ ] beat - not sure if these are overkill?
  - [ ] district
  - [ ] ward
  - [ ] community
- [ ] come up with queries, indexes, and enums (if applicable)
- [ ] see if pandas has an easy to use csv to sql we could use
- [ ] create new script for pushing data into sql
- [ ] come up with basic sql queries in an sql file


## Optimizations to try

- [ ] use python to perform sql instead of raw sql
- [ ] create example python script with user inputs using invoke with all the different SQL queries tested and described
- [ ] use an orm instead of python sql
