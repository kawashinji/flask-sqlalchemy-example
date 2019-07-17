from dotenv import load_dotenv
load_dotenv(verbose=True)

from flask import Flask
from config.db import init_db
import lib.models
from web.routes import routes

app = Flask(__name__, static_url_path='', static_folder='public')
app.config.from_object('config.define.Config')
app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))

init_db(app)
routes(app)

if __name__ == '__main__':
    app.run()
