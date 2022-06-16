import pika
import sys

# Create a connection, say CN
# Create a channel in CN, say CH
# Create an Exchange
# Publish the message
# Close the connection
# Automatically closes the channel


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.exchange_declare(exchange = 'br_exchange', exchange_type='fanout')

# we don't create any queue in the publisher because it's a broadcast exchange
# and queue will be created exclusively for subscriber
for i in range(4):
    message = "Hello" + str(i)
    channel.basic_publish(exchange='br_exchange', routing_key='', body = message)
    print("[x] sent %r" %message)

# if_unused=False - delete exchange even some queues are associated with the exchange.
channel.exchange_delete(exchange='br_exchange', if_unused=False)

connection.close()

"""
The only thing is if a subscriber is already running by the time publisher 
sends the message, they will be received by the subscriber.
But if a subscriber is not there at the time of publishing the message, they 
will be dropped
"""
