from websocket_server import WebsocketServer
import logging
import json
from datetime import datetime
from setting import Setting

from database import Database


class Websocket_Server():

    def __init__(self, host, port, label, db):
        self.server = WebsocketServer(
            host=host, port=port, loglevel=logging.DEBUG)
        self.db = Database(db)
        self.label = label
        self.s = Setting()

    def new_client(self, client, server):
        print("new client connected and was given id {}".format(client['id']))

    def client_left(self, client, server):
        print("client{} disconnected".format(client['id']))

    def message_received(self, client, server, message):
        message = json.loads(message)
        timestamp = datetime.today().strftime("%Y-%m-%d/%H-%M-%S-%f")
        message["timestamp"] = timestamp
        print(
            f"Response from client:{message['timestamp']}, {client['id']}, address:{client['address']}. label:{self.s.LABEL}.")
        if(len(message) == 18):
            self.db.insert_current_data(message, self.label)

    def run(self):
        self.server.set_fn_new_client(self.new_client)
        self.server.set_fn_client_left(self.client_left)
        self.server.set_fn_message_received(self.message_received)
        self.server.run_forever()

    



