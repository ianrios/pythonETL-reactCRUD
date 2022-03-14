# Windy City Crime

## Getting Started
Decompress given dataset
```sh
gunzip -c data/crime.csv.gz > data/crime.csv
```

Install the project's dependencies, then run the flask application
```sh
export FLASK_APP=windy_city_crime
export FLASK_ENV=development
flask run
```
