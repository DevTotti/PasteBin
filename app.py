from flask import Flask
from dotenv import load_dotenv
from flask_mongoengine import MongoEngine
import os
from flask_restful import Api
from api.routes import api_routes


load_dotenv()

default_config = {
    "MONGODB_SETTINGS": {
        'db': os.environ["APP"],
        'host': os.environ["HOST"],
        'port': 0,
    }
}


def initialize():
    app = Flask(__name__)
    app.config.update(default_config)
    mongo = MongoEngine(app)
    api = Api(app=app)
    api = api_routes(api=api)
    return app



if __name__ == '__main__':
    app = initialize()
    app.run(debug=True)
    