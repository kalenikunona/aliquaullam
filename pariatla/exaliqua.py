import pika

# Establish a connection to the RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue to send and receive messages
channel.queue_declare(queue='hello')

# Send a message to the queue
channel.basic_publish(exchange='', routing_key='hello', body='Hello, RabbitMQ!')

# Close the connection
connection.close()
