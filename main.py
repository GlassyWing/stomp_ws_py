import json
import time

from stomp_ws.client import Client
import logging


def print_frame(frame):
    print(json.loads(frame.body))


if __name__ == '__main__':
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)

    # open transport
    client = Client("ws://127.0.0.1:8080/gs-guide-websocket")

    # connect to the endpoint
    client.connect(login="name",
                   passcode="45C82C421EBA87C8131E220F878E4145",
                   timeout=0)

    # subscribe channel
    client.subscribe("/topic/1", callback=print_frame)

    # send msg to channel
    client.send("/topic/1", body=json.dumps({'name': 'tom'}))

    time.sleep(3)

    client.disconnect()
