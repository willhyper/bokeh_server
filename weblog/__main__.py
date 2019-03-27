from threading import Thread
from . import data_renderer
from . import flask_app

t_bokeh = Thread(target=data_renderer.start_server,
       args=(flask_app.addr, flask_app.port))
t_bokeh.daemon =True
t_bokeh.start()

t_flask=Thread(target=flask_app.app.run,
       args=(flask_app.addr, flask_app.port))
t_flask.daemon= True
t_flask.start()

from .logger import log

