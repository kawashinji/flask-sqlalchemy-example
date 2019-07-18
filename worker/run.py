from dotenv import load_dotenv
load_dotenv(verbose=True)

from flask import Flask
from config.db import init_db
import worker.tasks

app = Flask(__name__)
app.config.from_object('config.define.Config')
init_db(app)
app.app_context().push()

print('========== Start Task ==========')
while worker.tasks.run() is not None:
    pass
print('========== End Task ==========')
