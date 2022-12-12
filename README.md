# Distributed-Message-Queues, msg brokers

- Integrating Python With Distributed Message Queues
- Message brokers takes the burden of resilient message delivery betn the producer and consumer services which requires its own infrastructure, that can be both an advantage and a disadvantage
- other benefits this provides are:

1. **Loose Coupling**: modify or replace one component with another without affecting the rest of your system
2. **Flexibility**: ability to alter system's business rules by changing the broker configuration and message delivery rules without writing code.
3. **Scalability**: dynamically add more components of a given kind to handle increased workload in a specific functional area
4. **Reliability**: Consumers may need to acknowledge a message b4 the broker removes its from a queue to ensure safe delivery.
   - Running the broker in the cluster may provide additional fault tolerance
5. **Persistence**: The broker may keep some messages in the queue while the consumers are offline due to a failure.
6. **Performance**: Using a dedicated infrastructure for the msg broker offloads our application

## RabbitMQ: pika

- `docker run -it --rm --name rabbitmq -p 5672:5672 rabbitmq`

## Redis (Remote Dictionary Server)

- in-memory key-value data store that usually works as an ultra-fast cache betn a traditional SQL database and a server
- it can also serve as a persistent NoSQL database and also a message broker in the publish-subscribe model
- `docker run -it --rm --name redis -p 6379:6379 redis`
- connect to a running container using redis command-line interface
  - `docker exec -it redis redis-cli`
  - [List of commands](https://redis.io/commands/)

- if we have multiple active subscribers listening on a channel, then all of them will receive the same message.
- By default messages aren't persisted
- [How to Use Redis with Python](https://realpython.com/python-redis/)

## Apache Kafka: kafka-python3

- Kafka is the most advanced and complicated of the 3 message brokers that we saw till now.
- It's a distributed streaming platform used in real-time event-driven applications.
- Its main selling point is the ability to handle large volumes of data with almost no performance lag.

### Running Kafka

- to run kafka, we'll need to set up a distributed cluster.
- we can use Docker-compose to start a multi-container Docker application
