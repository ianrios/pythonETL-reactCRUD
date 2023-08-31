import logging
import argparse
import sys
from time import perf_counter
import os
from dotenv import load_dotenv
from datetime import timedelta
from pathlib import Path
import pandas as pd
import pandas.io.sql as sqlio
import psycopg2
import psycopg2.extras

parser = argparse.ArgumentParser()

parser.add_argument('--init', action='store_true', help="Run Init Method")
parser.add_argument('--query', action='store_true', help="Run Queries")


logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel("INFO")

input_csv = Path("data/crime.csv")


CRIMES_TABLE_NAME = 'crimes'
PRIMARY_TYPES_TABLE_NAME = 'primary_types'


def connect(params):
    """establish and return a connection to the PostgreSQL database and the db cursor"""
    connection = psycopg2.connect(**params)
    return [connection.cursor(), connection]


def clear_table(cursor, connection, table_name, reset_sequence=False):
    """delete all rows from a table"""
    cursor.execute(f"DELETE FROM {table_name}")

    # for primary_types table
    if reset_sequence:
        cursor.execute(f"ALTER SEQUENCE {table_name}_id_seq RESTART WITH 1")

    connection.commit()


def migrate_db(cursor, connection):
    """drop tables and recreate tables (if needed) for fresh database"""

    # drop tables if exists - new db version
    # TODO: consider wrapping this in a migrate new version method
    cursor.execute(f"DROP TABLE IF EXISTS {CRIMES_TABLE_NAME}")
    cursor.execute(f"DROP TABLE IF EXISTS {PRIMARY_TYPES_TABLE_NAME}")

    # create new tables
    cursor.execute(f"""
                   CREATE TABLE IF NOT EXISTS {PRIMARY_TYPES_TABLE_NAME} (
                    id serial PRIMARY KEY NOT NULL,
                    primary_type text NOT NULL
                   );
                """)

    cursor.execute(f"""
                    CREATE TABLE IF NOT EXISTS {CRIMES_TABLE_NAME} (
                    unique_key bigint NOT NULL,
                    case_number text,
                    date timestamp with time zone,
                    block text,
                    iucr text,
                    primary_type_id int REFERENCES primary_types(id),
                    description text,
                    location_description text,
                    arrest boolean,
                    domestic boolean,
                    beat int,
                    district text,
                    ward text,
                    community_area text,
                    fbi_code text,
                    x_coordinate numeric,
                    y_coordinate numeric,
                    year integer,
                    updated_on timestamp with time zone,
                    latitude numeric,
                    longitude numeric,
                    location text
                   );
                """)
    # TODO: location could be point, but not enough time

    # create an index on the primary_type_id column
    cursor.execute(
        f"CREATE INDEX idx_{CRIMES_TABLE_NAME}_primary_type_id ON {CRIMES_TABLE_NAME} (primary_type_id)")

    connection.commit()


def seed_db(cursor, connection):
    """Parse CSV and inject data into SQL DB"""

    # read data from csv and store as data frame for future use
    data_frame = pd.read_csv(input_csv, engine="pyarrow")

    # insert primary types into db and save foreign keys in dict for future use
    primary_type_mapping = {}
    for primary_type in data_frame['primary_type'].unique():
        cursor.execute(
            f"""INSERT INTO {PRIMARY_TYPES_TABLE_NAME} (primary_type)
            VALUES (%s) RETURNING id""", (primary_type,)
        )
        primary_type_id = cursor.fetchone()[0]
        primary_type_mapping[primary_type] = primary_type_id
    connection.commit()

    # group data by primary_type
    grouped_data = data_frame.groupby('primary_type')

    # insert grouped data into crime table
    for primary_type, group in grouped_data:
        # convert data frame to dict insertion
        rows = group.to_dict('records')

        # get primary_type_id
        primary_type_id = primary_type_mapping[primary_type]

        # transform rows to include primary_type_id and exclude primary_type
        for row in rows:
            row['primary_type_id'] = primary_type_id
            row.pop('primary_type')

        # columns for insert
        columns = [col for col in data_frame.columns if col != 'primary_type']
        columns.insert(0, 'primary_type_id')

        # convert to tuples for insertion
        tuples = [tuple(row[col] for col in columns) for row in rows]

        # insert
        psycopg2.extras.execute_values(
            cursor, f"INSERT INTO {CRIMES_TABLE_NAME} ({', '.join(columns)}) VALUES %s",
            tuples, template=None, page_size=100
        )

        connection.commit()


def query_db(cursor, connection):
    # create many queries to check if data exists and was parsed and inserted correctly

    select_primary_types = f"SELECT * FROM {PRIMARY_TYPES_TABLE_NAME}"
    primary_types = sqlio.read_sql_query(select_primary_types, connection)
    print(primary_types)

    select_distinct_years = f"SELECT DISTINCT year FROM {CRIMES_TABLE_NAME}"
    distinct_years = sqlio.read_sql_query(select_distinct_years, connection)
    print(distinct_years)

    select_distinct_years = f"SELECT year, COUNT(year) AS total_crimes_in_year FROM {CRIMES_TABLE_NAME} GROUP BY year"
    distinct_years = sqlio.read_sql_query(select_distinct_years, connection)
    print(distinct_years)

    return


if __name__ == "__main__":

    args = parser.parse_args()
    print(args)

    if not args.init and not args.query:
        parser.print_help()

    # load .env
    load_dotenv()

    # create postgres connection
    db_params = {
        'host': 'db',
        'database': os.getenv('POSTGRES_DB'),
        'user': os.getenv('POSTGRES_USER'),
        'password': os.getenv('POSTGRES_PASSWORD'),
        'port': 5432
    }
    [cur, conn] = connect(db_params)

    if args.init:
        logger.info("Initializing DB")
        t1 = perf_counter()

        # migrate db (create tables)
        migrate_db(cur, conn)

        # clear tables if previously seeded
        clear_table(cur, conn, CRIMES_TABLE_NAME)
        clear_table(cur, conn, PRIMARY_TYPES_TABLE_NAME, reset_sequence=True)

        # migrate db (create tables)
        seed_db(cur, conn)

        t2 = perf_counter()
        time_delta = timedelta(seconds=t2-t1)
        logger.info(f"Completed database initialization in {time_delta}.")

    if args.query:
        logger.info("Running Queries")
        t1 = perf_counter()

        # query db
        query_db(cur, conn)

        t2 = perf_counter()
        time_delta = timedelta(seconds=t2-t1)
        logger.info(f"Completed queries in {time_delta}.")

    # close connection and cursor
    cur.close()
    conn.close()
