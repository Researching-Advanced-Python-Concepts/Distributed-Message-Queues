import redis


with redis.Redis() as client:
    # subscribing to a channel requires one extra step i.e creating the
    # PubSub object to call the subscribe() method on
    pubsub = client.pubsub()
    pubsub.subscribe("chatroom")
    for message in pubsub.listen():
        # messages received by a subscriber are python dictionaries with
        # some metadata which lets us decide how to deal with them
        print()
        print(message)
        print()
        if message["type"] == "message":
            # {'type': 'message', 'pattern': None, 'channel': b'chatroom',
            # 'data': b'pikachu'}
            body = message["data"].decode("utf-8")
            print(f"Got message: {body}")
