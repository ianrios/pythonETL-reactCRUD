import os
import psycopg2
import pandas as pd
import pandas.io.sql as sqlio
from flask import Blueprint, jsonify, request
import warnings

warnings.simplefilter(action='ignore', category=UserWarning)

blueprint = Blueprint("covid_stats", __name__, url_prefix="/covid-stats")


def create_connection():
    # create postgres connection
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
        return jsonify({"message": "Database connection successful"})

    except Exception as e:
        return jsonify({"error": str(e)})


@blueprint.route("/all", methods=["GET"])
def get_all_stats():
    """Get all COVID stats"""

    try:
        conn = create_connection()

        query = f"SELECT * FROM covid_state_stats"
        all_data = sqlio.read_sql_query(query, conn)

        conn.close()
        return jsonify({"query": query, "results": all_data.to_json()})

    except Exception as e:
        return jsonify({"error": str(e)})


@blueprint.route("/page", methods=["GET"])
def page_index():
    """Info about pagination"""

    return """Usage: http://localhost:5001/covid-stats/page/4 to return page four of the results - grouped 100 results at a a time, so result ids 400-499"""


@blueprint.route("/page/<int:current_page>", methods=["GET"])
def get_paged_stats(current_page):
    """Get all COVID stats"""

    try:
        conn = create_connection()

        page_size = 100
        offset = page_size * current_page

        query = f"""SELECT *
            FROM covid_state_stats
            ORDER BY date
            LIMIT {page_size}
            OFFSET {offset}
            """
        paged_data = sqlio.read_sql_query(query, conn)

        json_data = paged_data.to_json(orient='records', date_format='iso')

        #

        conn.close()

        return jsonify({"query": query, "results": json_data})

    except Exception as e:
        return jsonify({"error": str(e)})
