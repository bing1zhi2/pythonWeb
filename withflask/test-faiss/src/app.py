# coding=utf-8
from flask import Flask
from faissindex.blueprint import blueprint as FaissIndexBlueprint
import uwsgi_signal as sf


app = Flask(__name__)
app.debug = True

app.config.from_object('config')
# app.config.from_envvar('FAISS_WEB_SERVICE_CONFIG')

app.register_blueprint(FaissIndexBlueprint)

@app.route('/')
def hello_world():
    return 'Hello world'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
