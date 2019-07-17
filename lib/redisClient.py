import redis
from config.define import Config

class Client:
    def __init__(self):
        self.client = redis.Redis.from_url(Config.REDIS_URL)

    def get(self, key):
        return self.client.get(key)

    def set(self, key, value):
        self.client.set(key, value)
