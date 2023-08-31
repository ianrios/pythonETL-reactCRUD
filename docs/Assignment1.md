### Assignment 1: ETL:

- [x] Unzip the data from crime.csv.gz to "data/crime.csv" (this does not have to be done in Python).
- [x] Update this parse() function to:
  - [x] Read the data from "data/crime.csv"
  - [x] parse all the data rows into the CrimeDataRecord class
  - [x] create outputs directory
  - [x] Convert each CrimeDataRecord to JSON
  - [x] output each json blob to a corresponding text file in the outputs directory
  - [x] Each JSON string should be written to a single line in the corresponding file. The model has a ".to_json()" method to simplify conversion for you.

Example:

```bash
    - outputs/
        - PUBLIC PEACE VIOLATION.txt
        - DECEPTIVE PRACTICE.txt
        - CRIMINAL DAMAGE.txt
        - NARCOTICS.txt
        - etc...
```

- [x] Return a list of CrimeTypeMetric values, sorted from most frequently occurring to least.
  - [x] Occurrences should be calculated based on the number of CrimeTypeData records corresponding to the primary_type.

#### Success Criteria:

- [x] Running this python module executes the parsing logic and test logic successfully without any errors.
- [x] run via `python -m scripts.run_etl`

#### Additional Notes:

- You may use any third party libraries or tools to execute this task but the entrypoint to the ETL process must be executed by Python. You should be able to explain and justify your choices during review. - First focus on getting the right solution and then focus on optimizations, like reducing the number of times the file is read or the number of times the row items are iterated over or the number of records kept in memory. Even if you choose not to make those optimizations, it'll still be good to have a discussion about what could have been done.



##### known sub sort added complexity

['NON-CRIMINAL', 1, 17]
['OTHER NARCOTIC VIOLATION', 15, 3]
['PUBLIC INDECENCY', 18, 0]

all total up to 18 for arrests.

I believe the correct sub sort is alphabetical.

## Tasks

- [x] install linter
- [x] install formatter
- [x] get docker to work on personal laptop
- [x] not sure what i would need a package for, this is simple enough - perhaps packages exist that would out-perform my existing ETL system from conversant...? need to research python etl packages i suppose
- [x] pick a csv parse package - resource: https://pythonspeed.com/articles/pandas-read-csv-fast/
- [x] parse .csv as a python dictionary for a single task costing O(n) - could this runtime be reduced? probably not, even with multithreading we still have to read in each line individually
- [x] test runtimes with python timer for optimization step - 2.5 seconds, barely
- [x] parse data frame from pandas efficiently - resource: https://towardsdatascience.com/efficiently-iterating-over-rows-in-a-pandas-dataframe-7dd5f9992c01
- [x] save all progress in github for review


## Optimizations

- [x] save speed - the CrimeDataRecord is pretty expensive to use instead of pushing the data frame directy to json
    - I added a FAST_SAVE toggle to speed up the process by pushing the output directly from the pandas data frame
- [ ] use parquet instead of CSV https://pypi.org/project/fastparquet/
    - seems like overkill
