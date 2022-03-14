from flask import Blueprint

blueprint = Blueprint("crime_record", __name__, url_prefix="/crime_record")


# a simple page that says hello
@blueprint.route("/hello", methods=["GET"])
def hello():
    return "Hello, World!"
