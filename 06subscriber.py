import pika
import random
import time


subId = random.randint(1, 100)
print("Subscriber Id = ", subId)


connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))

channel = connection.channel()

# Solution of problem №2 - durable=True - it retains exchange config, bindings, etc
channel.exchange_declare(exchange='logs_exchange', exchange_type='direct', durable=True)

queue_name = "task_queue"
# Solution of problem №3 - durable=True - queue will start persisting the messages
# Only the messages which are requested by the publisher to be persisted
result = channel.queue_declare(queue=queue_name,
                               #exclusive=True, # Problem №4 solution 
                               durable=True)

severity = ["Error", "Warning", "Info", "Other"]

for s in severity: # subscriber is receiving all the severity messages
    channel.queue_bind(exchange='logs_exchange', queue=queue_name, routing_key=s)

print('[*] waiting for the messages')

def callback(ch, method, properties, body):
    print('[x] Received message:::: %r' %body)
    #randomSleep = random.randint(1, 5)
    randomSleep = 5 # to simulate workload time of subscriber 
    print("Working for ", randomSleep, "seconds")
    while randomSleep > 0:
        print(".", end="")
        time.sleep(1)
        randomSleep -= 1
    print("!")
    ch.basic_ack(delivery_tag=method.delivery_tag) # Problem №4 solution

# Solution of problem №5 - prefetch_count=1 - will not send more than one message 
# to a particular subscriber before receiving the acknowledgement from it.
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=queue_name,
                      on_message_callback=callback
                      #auto_ack=True
                      )

channel.start_consuming()

