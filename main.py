from webSocketServer import Websocket_Server
from setting import Setting


if(__name__ == "__main__"):
    s = Setting()
    ws_server = Websocket_Server("0.0.0.0", s.PORT, s.LABEL, s.USE_DATABASE)
    ws_server.run()
