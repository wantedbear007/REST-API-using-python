from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')  # Basically it means we are accessing our home page eg: https://www.google.com/
def homepage():
    return 'Hello world !'


if '__main__' == __name__:
    app.run(debug=True)  # Here you can specify the port by passing port=4000
