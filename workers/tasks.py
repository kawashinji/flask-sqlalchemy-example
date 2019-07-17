from dotenv import load_dotenv
load_dotenv(verbose=True)

import time
from celery import Celery

from . import path
from config.define import Config
from lib import sqsClient


app = Celery('tasks', backend=Config.BROKER_URL, broker=Config.BROKER_URL)

@app.task
def run():
    time.sleep(1)
    client = sqsClient.Client()
    key = client.get()
    print(key)
    return key
