import redis

# connect to local redis server
with redis.Redis() as client:
    while True:
        message = input("Message: ")
        # immediately start publishing messages on the chatroom channel
        # we don't have to create the channels, because Reids will do it
        # for us
        client.publish("chatroom", message=message)
