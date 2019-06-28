import redis

class Client:
    def __init__(self, app):
        self.client = redis.Redis.from_url(app.config.get('REDIS_URL'))

    def get(self, key):
        return self.client.get(key)

    def set(self, key, value):
        self.client.set(key, value)
