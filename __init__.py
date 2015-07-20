# Load config and environments
import config

from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()