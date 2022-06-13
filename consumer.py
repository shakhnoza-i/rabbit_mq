import pika, sys, os


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host = "localhost"))
    channel = connection.channel()
    channel.queue_declare(queue="hello")


# whenever a message is posted in the queue, the corresponding callback function is executed
# %body - receive msg in the binary format so % bring to real format
    def callback(ch, method, properties, body):
        print("[x] received %r" %body)

# basic_consume - to associate this callback function with the queue
# auto_ack - acknowledging this back to the message queue. So that queue can delete 
# this msq from itself. And msg will keep on lingering in the msg queue - consume memory
    channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack = True)

    print(" [*] waiting for the messages. To exit press Ctrl-C")

    channel.start_consuming()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
