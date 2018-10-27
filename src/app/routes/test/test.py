from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/home')
def hello():
    return "Hola"


@app.route('/example', methods=['GET', 'POST'])
def example():
    if request.method == 'POST':
        data = request.get_json()
        return jsonify({'data sent': data.get('name')})

    response = {'title': 'Get Request', 'payload': 'some payload'}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
