import pika

# create the connection, 'localhost' cause our RabbitMQ in our local machine
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#  create a channel in the connection
channel = connection.channel()

# [Optional] create an exchange and specify the bindings, because 
# we are using the default exchange - we ignore this step

# create a queue through the channel
channel.queue_declare(queue="hello") # if  consumer has already created the queue, then this
                                     # particular statement will not have any effect

# message has gone to the queue named hello
# exchange="" means default exchange
# routing key should be exactly the same as the queue name
# in body we need to specify what message we want to send
channel.basic_publish(exchange="", routing_key="hello", body="hello_world 2")
print("[x] Sent Hello World")

# if we close the connection - the channels automatically will also be closed.
connection.close()

# when the publisher sent the message, it was received by one of the consumers,
# if there are two consumers attached to the same queue. Next time - second one
# So these messages are by default distributed among the attached subscribers 
# in a round-robin manner.