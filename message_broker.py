"""
like tcp - rabbitmq
udp - redis

Manage the data of all devices. Just send all your data of these devices towards
your Message Broker, and it will take care of processing them.

Registration with the third party services
"""

"""
Exchange recieves messages from the publisher
Exchange has rules defined - which decides which in particular message 
queue this message should be forwarded
Publisher recognizes the subscriber entity by its identifier, say its name.
The actual subscriber address is not known to the publisher.
AMQP - advanced message queuing protocol
Publisher is not aware of the subscriber physical address. The routing of the 
message to the physical address of the subscriber is taken care of by the message
broker.
"""