from flask import Flask, request, jsonify
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = ''
#db.

@app.route('/home')
def hello():
    return "Hola wacho forro"


@app.route('/example', methods=['GET', 'POST'])
def example():
    if request.method == 'POST':
        data = request.get_json()
        return jsonify({'data sent': data.get('name')})

    response = {'title': 'Get Request', 'payload': 'some payload'}
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
