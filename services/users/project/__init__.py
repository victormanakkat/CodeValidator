
import os
# import sys
import datetime
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# instantiate the app
app = Flask(__name__)

# set configuration - is it relative from the flask cli is (manage.py)?
# app.config.from_object('project.config.DevelopmentConfig')

# set config from the environment variable define in the docker-compose yml file
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# prints to the console, when run a docker-compose...logs command
# print(app.config, file=sys.stderr)

# instantiate the db
db = SQLAlchemy(app)

# model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'this is a success message',
        'message': 'pong'
    })

