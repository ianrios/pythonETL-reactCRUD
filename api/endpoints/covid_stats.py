import os
import psycopg2
import pandas as pd
import pandas.io.sql as sqlio
from flask import Blueprint, jsonify, request, redirect, url_for, Response
import warnings

warnings.simplefilter(action='ignore', category=UserWarning)

blueprint = Blueprint("covid_stats", __name__, url_prefix="/covid-stats")

# For Assignment 3


def create_connection():
    """create postgres connection"""
    host_arg = request.args.get("host")

    params = {
        'host': host_arg if host_arg else "db",
        'database': os.getenv('POSTGRES_DB'),
        'user': os.getenv('POSTGRES_USER'),
        'password': os.getenv('POSTGRES_PASSWORD'),
        'port': 5432
    }

    return psycopg2.connect(**params)


@blueprint.route("/test-db-connection", methods=["GET"])
def test_db_connection():
    """Establish a connection to Postgres database"""

    try:
        create_connection().close()
        return jsonify({'message': "Database connection successful"})

    except Exception as e:
        return jsonify({'error': str(e)})


def format_col(col):
    # return if value is numeric for nicer table later on
    return {'id': col, 'label': col.replace("_", " ").title()}


@blueprint.route("/columns", methods=["GET"])
def get_columns():
    """Get columns formatted for react table"""

    try:
        conn = create_connection()

        query = f"""SELECT *
            FROM covid_state_stats
            LIMIT 1
            """
        single_row_data = sqlio.read_sql_query(query, conn)

        conn.close()

        # should match [{ id: "string", label: "String (units)"},...]

        columns = [format_col(col) for col in single_row_data.columns]

        return jsonify(columns)

    except Exception as e:
        return jsonify({'error': str(e)})


@blueprint.route("/all", methods=["GET"])
def get_all_stats():
    """Get all COVID stats"""

    try:
        conn = create_connection()

        query = f"SELECT * FROM covid_state_stats"
        all_data = sqlio.read_sql_query(query, conn)

        conn.close()

        return jsonify({'query': query, 'results': all_data.to_json()})

    except Exception as e:
        return jsonify({'error': str(e)})


@blueprint.route("/page", methods=["GET"])
def page_index():
    """Info about pagination"""

    return """Usage: http://localhost:5001/covid-stats/page/4 to return page four of the results - grouped 100 results at a a time, so result ids 400-499"""


@blueprint.route("/page/<int:current_page>", methods=["GET"])
def get_paged_stats(current_page):
    """Get all COVID stats"""

    page_size = 100

    try:
        conn = create_connection()

        offset = page_size * current_page

        query = f"""SELECT *
            FROM covid_state_stats
            ORDER BY date
            LIMIT {page_size}
            OFFSET {offset}
            """
        paged_data = sqlio.read_sql_query(query, conn)

        conn.close()

        json_data = paged_data.to_json(orient='records', date_format='iso')

        # TODO: calculate the URL for the last previous available page and redirect if no data

        return jsonify({'query': query,  'row_count': len(json_data), 'results': json_data})

    except Exception as e:
        return jsonify({'error': str(e)})


# For Assignment 4


@blueprint.route("/pages/<int:page_size>", methods=["GET"])
def get_num_pages(page_size):
    """Get number of pages and count of all rows in table based on page size"""

    try:
        conn = create_connection()

        query = f"""SELECT COUNT(*) as row_count FROM covid_state_stats"""
        data = sqlio.read_sql_query(query, conn)

        conn.close()

        row_count = int(data.iloc[0]['row_count'])
        max_pages = (row_count - 1) // page_size

        return jsonify({'row_count': row_count, 'max_pages': max_pages})

    except Exception as e:
        return jsonify({'error': str(e)})


@blueprint.route("/exact-page/<int:current_page>/limit/<int:page_limit>/offset/<int:row_offset>", methods=["GET"])
def get_exact_page(current_page, page_limit, row_offset):
    """Get a certain page of COVID stats starting at a specific offset"""

    try:
        conn = create_connection()

        offset = page_limit * current_page + row_offset

        # page_limit will only ever 25, 50, or 100
        # row_offset will only ever be 0, 25, 50, or 75

        query = f"""SELECT *
            FROM covid_state_stats
            ORDER BY date
            LIMIT {page_limit}
            OFFSET {offset}
            """
        paged_data = sqlio.read_sql_query(query, conn)

        conn.close()

        json_data = paged_data.to_json(orient='records', date_format='iso')

        return jsonify({'query': query,  'row_count': len(json_data), 'offset': offset, 'results': json_data})

    except Exception as e:
        return jsonify({'error': str(e)})
