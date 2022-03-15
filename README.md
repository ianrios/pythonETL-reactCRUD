# Windy City Crime

This repository houses the coding assignments used by NYGC SWENG to evaluate interview candidates on their
technical engineering skills. Each assignment touches on specific topics to allow candidates to demonstrate
proficiencies in the various technologies we use at NYGC. As a candidate, you may be asked to execute on one
or more of these assignments, varying based on the position being applied for.

In general, you should tackle these exercises as you would any problem you encounter in your normal day to day.
That means you should feel free to search for and use any online references you can find to assist you in creating
the best solution you can in the time you have. You will not be evaluated on just the correctness of your
solutions. We also highly value your ability to explain your thought process and justify the choices you made to
arrive that those solutions.

Good luck!

## Prerequisites

**First**, we will be using a Google Cloud Platform provided dataset to drive the work in these assignments.
For convenience, we have included a compressed CSV file of the dataset for you to work against and you should
unzip this file locally.

```sh
gunzip -c data/crime.csv.gz > data/crime.csv
```

**Next**, if you do not have a Python development environment readily available, we have provided the docker 
compose file and configuration files to support remote container development in Visual Studio Code. For more details,
check out the [documentation](https://code.visualstudio.com/docs/remote/containers#_getting-started). Once you have 
installed the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
extension, you can run the `Remote-Containers: Open Folder in Container` command in VSCode and target the root of this
repository to launch into a remote container session in the Python docker container we have provided for you.

Alternatively, you can go ahead and do all the Python development work in a development environment on your host machine,
if you are set up to do so.


# Assignment 1 - ETL in Python

This assignment will review your basic proficiency in Python by having you perform an ETL operation on a 
fixed CSV dataset. The ETL process should be run with the following command:

```bash
$ python -m scripts.run_etl
```

Success criteria:
- Running the python script should successfully execute the parsing logic and export the data
    from the CSV into the requested format.
- All the test assertions pass on the resulting dataset.


Be prepared to:
- Walk us through the details of your solution and point out any specific optimizations made.
- Discuss any further optimizations that could be made, given more time and thought.

View the assignment details [here](./scripts/run_etl.py).


# Assignment 2 - ETL to SQL Database

This assignment gives you an opportunity to demonstrate your proficiency with data modeling and database scripting.

**First**, using the same dataset as [Assignment 1](#assignment-1---etl-in-python), design a database schema to best 
represent the data in the [CSV file](./data/crime.csv) in order to support queries to answer the following questions. 
Assume that we will want to build a reporting application that will run queries for these answers on a frequent basis:

- What is the list of all the types of committed crimes (primary_type) in the dataset?
- For any given year, what type of crime (primary_type) was the most frequently committed?
- What percentage of each type of crime (primary_type) ended in arrest (arrest == true)?
- What is the frequency of each crime type (primary_type) year over year? Imagine we want to generate datapoints
    to graph the number of occurrences of each crime type over every year in the dataset.
- For any beat, district, ward or community (only one will be provided at a time), retrieve all the unique keys
    of each crime incident ordered by date.

**Next**, using any preferred tools, script the creation of the proposed data schema and the import of the data into a
Postgres database. For convenience, we have provided a docker-compose file for a simple Postgres database that can
be started as follows:

```bash
$ docker compose up db
```

The credentials are as follows:
- Username: `nygc-user`
- Password: `nygc-sweng-rocks!`

Once started, you should have an empty database available at: `jdbc:postgresql://localhost:5432/interview_db`. We are using
a docker volume so the data should persist between container and host restarts. Feel free to create the schema and import
the data using any database frameworks and tools you are familiar with.

**Finally**, construct some sample queries that you would use to answer some of the questions listed above. Just tackle the
ones you feel comfortable on and feel free to adjust the data model as you work through the problem. Consider how you would go
about optimizing those queries to be run on a continuous basis by several users on a daily basis. Consider what database 
constructs and features you would use to reduce stress on the SQL server and improve query responsiveness, given the nature 
of the dataset. These sample queries do not have to be exhaustive and are meant to drive the in-person conversation during
the review session.


# Assignment 3 - Working with APIs (:construction: Work In Progress :construction:)

 > This section is currently under construction so please ignore it.

 This assignment is intended to test your familiarity with Python's FlaskAPI by having you implement additional API 
 functionality. You will be exposing the data set that was imported in [Assignment 1](#assignment-1---etl-the-data) 
 through new APIs.


Install the project's dependencies, then run the flask application:

```sh
export FLASK_APP=windy_city_crime
export FLASK_ENV=development
flask run
```


# Assignment 4 - Working with React (:construction: Work In Progress :construction:)

> This section is currently under construction so please ignore it.

This assignment is intended to test your proficiency in implementing changes in React based applications.

