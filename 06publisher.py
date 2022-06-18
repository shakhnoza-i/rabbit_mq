import pika
import sys
import random

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

# Solution of problem №1
channel.confirm_delivery() # confirmation is sent from broker to publisher

# Solution of problem №2 - durable=True - it retains exchange config, bindings, etc
channel.exchange_declare(exchange = 'logs_exchange', exchange_type='direct', durable=True)

severity = ["Error", "Warning", "Info", "Other"]
messages = ["EMsg", "WMsg", "IMsg", "OMsg"]

for i in range(10):
    randomNum = random.randint(0, len(severity)-1)
    message = messages[randomNum]
    rk = severity[randomNum]
    try:
        channel.basic_publish(exchange='logs_exchange',
                              routing_key=rk,
                              body=message,
                              properties=pika.BasicProperties(
                                  delivery_mode=2 # Make Message Persistent - Problem №3
                                  )
                              )
        print("[x] sent %r" %message)
    except pika.exceptions.ChannelClosed:
        print("Channel Closed")
    except pika.exceptions.ConnectionClosed:
        print("Connection Closed")


channel.exchange_delete(exchange='logs_exchange', if_unused=False)

connection.close()





