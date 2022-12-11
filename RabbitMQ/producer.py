import pika


QUEUE_NAME = "mailbox"


with pika.BlockingConnection() as connection:
    # channel is a lightweight abstraction on top of a TCP connection
    # we can have multiple independent channels for separate 
    # transmissions
    channel = connection.channel()
    # making sure the queue exist in the broker
    channel.queue_declare(queue=QUEUE_NAME)
    while True:
        message = input("Message: ")
        channel.basic_publish(
            exchange="",
            routing_key=QUEUE_NAME,
            body=message.encode("utf-8")
        )