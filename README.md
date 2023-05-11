# Stomp over websocket

simple python client for stomp over websocket.

## Usage

The usage is simple if you have experience using Stomp js, assuming you have built a websocket server with [SpringBoot](https://spring.io/guides/gs/messaging-stomp-websocket/), below is the way to connect:

```python
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)


client = Client("ws://127.0.0.1:8080/gs-guide-websocket")

# connect to the endpoint
client.connect()

# subscribe channel
client.subscribe("/topic/1", callback=print_frame)

# send msg to channel
client.send("/topic/1", body=json.dumps({'name': 'tom'}))

time.sleep(3)

client.disconnect()
```

## API

### .connect(login, passcode, headers, connectCallback, errorCallback, timeout)

Attempts to connect to the server, the `timeout` default to 0 means that will block until a successful connection. You can also set login and passcode if the server requires auth.

### .disconnect(disconnectCallback, headers)

Disconnect from STOMP server, the callback will be called if `disconnectCallback` is not None.

### .subscribe(dest, callback)

Subscribes to a destination on the STOMP server to receive messages that are published on it. This method will return a tuple `(subscribe_id, unsubscribe)`:

```python
sub_id, unsubscribe = client.subscribe("/topic/1", some_func)
unsubscribe() # This will unsubscribe topic '/topic/1'
```

The `callback` must be a function that accepts a frame argument:

```python
def some_func(frame):
    print(frame.command) # get commend
    print(frame.headers) # get headers
    print(frame.body)    # get body
```

### .unsubscribe(dest)

Unsubscribe from a topic.

### .send(dest, headers=None, body=None)

Sends message to destination on the server. The format of message could be json or others, depends on the STOMP server.

## TODO

- [ ] : Heart beat
- [ ] : Transaction