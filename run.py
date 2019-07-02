from dotenv import load_dotenv
load_dotenv(verbose=True)

import random, string
from flask import Flask
from functools import reduce

from app import redisClient
from app import mysqlClient
from db import init_db
import app.models

app = Flask(__name__, static_url_path='', static_folder='public')
app.config.from_object('config.Config')
app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))

init_db(app)

@app.route('/api')
def top():
    return 'Hello World!'

@app.route('/api/redis')
def redis():
    client = redisClient.Client(app)
    client.set('hoge', 'fuga')
    return client.get('hoge')

@app.route('/api/mysql')
def mysql():
    client = mysqlClient.Client()
    client.add(''.join(random.choices(string.ascii_letters + string.digits, k=10)))
    users = client.all()
    return ''.join(map(lambda user: str(user.id) + ":" + user.name + "<br>", users))

if __name__ == '__main__':
    app.run()
