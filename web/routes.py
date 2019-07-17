import random, string

from lib import redisClient
from lib import mysqlClient
from lib import sqsClient

def routes(app):
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

    @app.route('/api/sqs')
    def sqs():
        client = sqsClient.Client(app)
        return client.add(''.join(random.choices(string.ascii_letters + string.digits, k=10)))
