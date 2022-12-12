from kafka3 import KafkaConsumer

# consumer constructor takes one or more topics that it might be
# interested in
consumer = KafkaConsumer("datascience")
for record in consumer:
    message = record.value.decode("utf-8")
    print(f"Got message: {message}")