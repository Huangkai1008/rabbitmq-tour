import pika

# Connect to the local RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# If we send a message to non-existing location, RabbitMQ will just drop the message
# Create the `hello` queue
channel.queue_declare(queue='hello')

# Use the default exchange
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World')
print(" [x] Sent 'Hello World!'")
connection.close()
