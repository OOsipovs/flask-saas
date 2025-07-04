from flask import Flask

from snakeeyes.blueprints.page import page
from snakeeyes.extensions import debug_toolbar


def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object("config.settings")
    app.config.from_pyfile("settings.py", silent=True)

    if settings_override:
        app.config.update(settings_override)

    app.register_blueprint(page)
    extensions(app)

    # @app.route("/")
    # def index():
    #     """
    #     Render a Hello World response.

    #     :return: Flask response
    #     """
    #     return app.config["HELLO"]

    return app


def extensions(app):
    """
    REgister 0 or more extensions
    :param app: Flask app
    :return: None
    """

    debug_toolbar.init_app(app)
    return None
