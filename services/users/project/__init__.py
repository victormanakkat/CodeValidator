
from flask import Flask, jsonify

# instantiate the app
app = Flask(__name__)

# set configuration - is it relative from the flask cli is (manage.py)?
app.config.from_object('project.config.DevelopmentConfig')

@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong'
    })

