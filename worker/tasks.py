import time

from config.define import Config
from lib import sqsClient
from lib import mysqlClient

def run():
    time.sleep(1)
    message = read()

    if message is not None:
        write(message.body)
        remove(message.message_id, message.receipt_handle)
        return message.body
    else:
        return None

def read():
    client = sqsClient.Client()
    return client.get()

def write(name):
    client = mysqlClient.Client()
    client.add(name)

def remove(id, receiptHandle):
    client = sqsClient.Client()
    return client.delete(id, receiptHandle)
