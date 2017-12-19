import socket
from flask import Flask
from decouple import config

app = Flask(__name__)

VERSION = config('VERSION', 'dev', cast=str)

@app.route("/")
def index():
    return socket.gethostname() + " - " + VERSION

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
