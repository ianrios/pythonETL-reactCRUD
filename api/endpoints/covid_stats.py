import os
import psycopg2
from flask import Blueprint, jsonify, request

blueprint = Blueprint("covid_stats", __name__, url_prefix="/covid-stats")


@blueprint.route("/test-db-connection", methods=["GET"])
def test_db_connection():
    """Establish a connection to Postgres database"""

    host_arg = request.args.get("host")

    db_host = host_arg if host_arg else "db"
    db_port = 5432

    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=db_host,
            port=db_port,
        )
        conn.close()
        return jsonify({"message": "Database connection successful"})

    except Exception as e:
        return jsonify({"error": str(e)})
