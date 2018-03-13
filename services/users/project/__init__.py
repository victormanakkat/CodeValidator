
import os

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


# import sys
# prints to the console, when run a docker-compose...logs command
# print(app.config, file=sys.stderr)

# instantiate the db
db = SQLAlchemy()

# Application Factory pattern:
def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)

    # register blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    # shell context for flask cli
    # This is used to register the app and db to theshell. Now we can work with the application context and
    # the database without having to import them directly into the shell
    app.shell_context_processor({'app': app, 'db': db})

    return app


