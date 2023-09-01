import os
import psycopg2
import pandas.io.sql as sqlio
from flask import Blueprint, jsonify, request
import warnings

warnings.simplefilter(action='ignore', category=UserWarning)

blueprint = Blueprint("covid_stats", __name__, url_prefix="/covid-stats")


@blueprint.route("/test-db-connection", methods=["GET"])
def test_db_connection():
    """Establish a connection to Postgres database"""

    host_arg = request.args.get("host")

    try:
        # create postgres connection
        params = {
            'host': host_arg if host_arg else "db",
            'database': os.getenv('POSTGRES_DB'),
            'user': os.getenv('POSTGRES_USER'),
            'password': os.getenv('POSTGRES_PASSWORD'),
            'port': 5432
        }
        connection = psycopg2.connect(**params)
        connection.close()
        return jsonify({"message": "Database connection successful"})

    except Exception as e:
        return jsonify({"error": str(e)})


@blueprint.route("/all", methods=["GET"])
def get_all_stats():
    """Get all COVID stats"""

    host_arg = request.args.get("host")

    try:
        # create postgres connection
        params = {
            'host': host_arg if host_arg else "db",
            'database': os.getenv('POSTGRES_DB'),
            'user': os.getenv('POSTGRES_USER'),
            'password': os.getenv('POSTGRES_PASSWORD'),
            'port': 5432
        }
        connection = psycopg2.connect(**params)

        select_all = f"SELECT * FROM covid_state_stats"
        all_data = sqlio.read_sql_query(select_all, connection)

        connection.close()
        return jsonify({"query": select_all, "results": all_data.to_json(), "status": 200})

    except Exception as e:
        return jsonify({"error": str(e)})
