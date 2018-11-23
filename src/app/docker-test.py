from flask import Flask

app = Flask(__name__)


@app.route('/docker')
def hello():
    return 'Hola Cesar, soy Docker!'

@app.route('/pete')
def pete():
    return 'Soy alto petizo'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
