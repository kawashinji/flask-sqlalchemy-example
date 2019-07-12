import boto3

class Client:
    def __init__(self, app):
        self.sqs = boto3.resource('sqs',
            aws_access_key_id = app.config.get('AWS')['ACCESS_KEY'],
            aws_secret_access_key = app.config.get('AWS')['SECRET_KEY'],
            region_name = app.config.get('AWS')['REGION'])
        self.name = app.config.get('SQS_NAME')

    def add(self, value):
        try:
            queue = self.sqs.get_queue_by_name(QueueName=self.name)
        except:
            queue = self.sqs.create_queue(QueueName=self.name)

        return str(queue.send_message(MessageBody=value))
