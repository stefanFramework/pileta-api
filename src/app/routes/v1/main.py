import datetime

from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)


@app.route('/version', methods=['GET'])
def version():
    current_date = datetime.datetime.now()
    response = {
        'name': 'pileta-api',
        'version': '1.0.0',
        'date': current_date.strftime("%Y-%m-%d %H:%M")
    }
    return jsonify(response)


# Registers a new measurements
@app.route('/register', methods=['POST'])
def register():
    if request.method != 'POST':
        return ''

    return 'register'


# For variable status pooling
@app.route('/status', methods=['GET'])
def status():
    return 'status'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
