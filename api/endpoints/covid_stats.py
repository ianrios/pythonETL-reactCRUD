import os
import psycopg2
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


@blueprint.route("/page/<int:page_num>", methods=["GET"])
def get_paged_stats(page_num):
    """Get all COVID stats"""

    try:
        conn = create_connection()

        query = f"SELECT * FROM covid_state_stats LIMIT 50"
        paged_data = sqlio.read_sql_query(query, conn)

        conn.close()
        return jsonify({"query": query, "results": paged_data.to_json()})

    except Exception as e:
        return jsonify({"error": str(e)})
