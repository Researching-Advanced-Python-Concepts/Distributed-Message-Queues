from kafka3 import KafkaProducer

producer = KafkaProducer(bootstrap_servers="localhost:9092")
while True:
    message = input("Message: ")
    # the send method is asynchronous becuz it returns a future object
    # that we can await by calling its blocking .get() method
    producer.send(
        topic="datascience",
        value=message.encode("utf-8"),
    )