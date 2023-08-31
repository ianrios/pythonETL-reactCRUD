import logging
import sys
import os
from dotenv import load_dotenv
from pathlib import Path
import pandas as pd
import psycopg2


logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel("INFO")

input_csv = Path("data/crime.csv")


TABLE_NAME = 'crime'


def connect(params):
    """establish and return a connection to the PostgreSQL database and the db cursor"""
    connection = psycopg2.connect(**params)
    return [connection.cursor(), connection]


def migrate_db(cursor, connection):
    """create tables needed for fresh database"""
    cursor.execute(f"""
                   CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                    unique_key int,
                    case_number text,
                    date date,
                    block text,
                    iucr int,
                    primary_type text,
                    description text,
                    location_description text,
                    arrest boolean,
                    domestic boolean,
                    beat_id int,
                    district_id int,
                    ward_id int,
                    community_area_id int,
                    fbi_code_id int,
                    x_coordinate numeric,
                    y_coordinate numeric,
                    year integer,
                    updated_on timestamp,
                    latitude numeric,
                    longitude numeric,
                    location point
                    );""")

    connection.commit()


def seed_db(cursor, connection):
    """Parse CSV and inject data into SQL DB"""

    # read data from csv and store as dataframe for future use
    data_frame = pd.read_csv(input_csv, engine="pyarrow")

    # group data by primary_type
    grouped_data = data_frame.groupby('primary_type')

    # group sizes
    group_sizes = grouped_data.size()

    # sort data by data frame size and primary_type alphabetically
    sorted_groups = group_sizes.reset_index(name='size').sort_values(
        by=['size', 'primary_type'], ascending=[False, True])

    # sort grouped data by data frame size and iterate over each group to generate output list
    for primary_type in sorted_groups['primary_type']:
        # grab group
        group = grouped_data.get_group(primary_type)

        # find foreign key for primary_type or create

        # convert DataFrame to list of tuples for insertion
        values = [tuple(row) for row in group.values]
        # insert
        psycopg2.extras.execute_values(
            cursor, f"INSERT INTO {TABLE_NAME} VALUES %s", values, template=None, page_size=100)

        connection.commit()


if __name__ == "__main__":

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

    # migrate db (create tables)
    migrate_db(cur, conn)

    # migrate db (create tables)
    # seed_db(cur, conn)

    # close connection and cursor
    cur.close()
    conn.close()
