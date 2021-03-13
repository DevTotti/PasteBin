from flask import Flask
from dotenv import load_dotenv
from flask_mongoengine import MongoEngine
import os
from flask_restful import Api
from api.routes import api_routes


from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger

from expiry import deleteDocument



load_dotenv()

default_config = {
    "MONGODB_SETTINGS": {
        'db': os.environ["APP"],
        'host': os.environ["HOST"],
        'port': 0,
    }
}


def initialize():
    print("starting-app")
    app = Flask(__name__)
    app.config.update(default_config)
    mongo = MongoEngine(app)
    scheduler = BlockingScheduler()
    scheduler.start()
    # scheduler.add_job(deleteDocument, "interval", seconds=10, max_instances=2)

    scheduler.add_job(
        func=deleteDocument,
        trigger=IntervalTrigger(seconds=2),
        id='deleting my data',
        replace_existing=True
    )

    atexit.register(lambda: scheduler.shutdown())
    api = Api(app=app)
    api = api_routes(api=api)
    return app



if __name__ == '__main__':
    app = initialize()
    app.run(debug=True)
    
