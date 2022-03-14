import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    _register_blueprints(app)

    return app


def _register_blueprints(app: Flask) -> None:
    from windy_city_crime.endpoints import crime_record

    app.register_blueprint(crime_record.blueprint)
