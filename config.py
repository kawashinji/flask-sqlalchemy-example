import os

class DevelopmentConfig:
    # Flask
    DEBUG = True
    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/flask?charset=utf8'.format(**{
        'user': os.getenv('DB_USER', 'flask'),
        'password': os.getenv('DB_PASSWORD', 'password'),
        'host': os.getenv('DB_HOST', 'localhost'),
        'port': os.getenv('DB_PORT', 3306),
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    REDIS_URL = 'redis://{host}:{port}/{db}'.format(**{
        'host': os.getenv('REDIS_HOST', 'localhost'),
        'port': os.getenv('REDIS_PORT', 6379),
        'db': os.getenv('REDIS_DB', 0),
    })

Config = DevelopmentConfig
