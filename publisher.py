import pika
from config import setting

credentials = pika.PlainCredentials(username=setting.user, password=setting.password, erase_on_connect=True)
parameters = pika.ConnectionParameters(host=setting.host, port=setting.port)

connection = pika.BlockingConnection(parameters)
# A channel provides a wrapper for interacting with RabbitMQ
channel = connection.channel()

# Check for a queue and create it, if necessary
channel.queue_declare(queue='hello')
# For the sake of simplicity, we are not declaring an exchange, so the subsequent publish call will be sent to a Default exchange that is predeclared by the broker
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")

# Safely disconnect from RabbitMQ
connection.close()


