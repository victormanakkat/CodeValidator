
import os
# import sys
from flask import Flask, jsonify

# instantiate the app
app = Flask(__name__)

# set configuration - is it relative from the flask cli is (manage.py)?
# app.config.from_object('project.config.DevelopmentConfig')

# set config from the environment variable define in the docker-compose yml file
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# prints to the console, when run a docker-compose...logs command
# print(app.config, file=sys.stderr)

@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong'
    })

