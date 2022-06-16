import pika

# Create a connection say CN
# Create a channel in CN, say CH
# Create the exchange (if publisher will not started yet)
# Create the temporary queue, if it does not exist already and associate it with the channel CH exclusively
# Bind the queue with the exchange
# Associate a call-back function with the message queue
# Start consuming the messages


# after creating the queue, it will use RabbitMQ Api or Pika to get queue_name.
# And using that name, it will bind the queue with the exchange.
connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))

channel = connection.channel()

# creating exchange, exchange_name=any,  exchange_type='fanout'
channel.exchange_declare(exchange='br_exchange', exchange_type='fanout')

# we don't specify any queue name, RabbitMQ choose the queue name
result = channel.queue_declare(queue='', exclusive=True)

# fetch the name of the queue
queue_name = result.method.queue

print("Subscriber queue_name =", queue_name)

# bind particular queue with the exchange
channel.queue_bind(exchange='br_exchange', queue=queue_name)

print('[*] waiting for the messages')

def callback(ch, method, properties, body):
    print('[x] %r' %body)

# basic_consume - to associate this callback function with the queue
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()

