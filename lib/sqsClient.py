import boto3
from config.define import Config

class Client:
    def __init__(self):
        self.sqs = boto3.resource('sqs',
            aws_access_key_id = Config.AWS['ACCESS_KEY'],
            aws_secret_access_key = Config.AWS['SECRET_KEY'],
            region_name = Config.AWS['REGION'])
        self.name = Config.SQS_NAME

    def add(self, value):
        try:
            queue = self.sqs.get_queue_by_name(QueueName = self.name)
        except:
            queue = self.sqs.create_queue(QueueName = self.name)

        return str(queue.send_message(MessageBody = value))

    def get(self):
        queue = self.sqs.get_queue_by_name(QueueName = self.name)
        messages = queue.receive_messages(MaxNumberOfMessages=1)
        return messages[0] if len(messages) > 0 else None

    def delete(self, id, receiptHandle):
        entries = [{ "Id": id, "ReceiptHandle": receiptHandle }]
        queue = self.sqs.get_queue_by_name(QueueName = self.name)
        return queue.delete_messages(Entries = entries)
