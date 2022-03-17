import os
import subprocess

from flask import Blueprint, request

blueprint = Blueprint("covid_stats", __name__, url_prefix="/covid-stats")


@blueprint.route("/test-db-connection", methods=["GET"])
def test_db_connection():
    """Establish a connection to Postgres database"""

    host_arg = request.args.get("host")

    db_host = host_arg if host_arg else "localhost"
    db_port = 5432

    result = subprocess.run(
        f"nc -vw 0 {db_host} {db_port}",
        shell=True,
        capture_output=True,
    )

    return {
        "stdout": result.stdout.decode(),
        "stderr": result.stderr.decode(),
    }
