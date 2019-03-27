from threading import Thread
from . import data_renderer, addr, port

Thread(target=data_renderer.start_websocket_server).start()

from .app import app

app.run(host=addr, port=port)
