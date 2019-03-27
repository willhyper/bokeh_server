from bokeh.document import Document

from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.server.server import Server

from tornado.ioloop import IOLoop

from . import data_holder

_source = ColumnDataSource(data=data_holder.get_data())


def start_websocket_server():
    server = Server({'/bkapp': modify_doc}, io_loop=IOLoop(), allow_websocket_origin=["localhost:8000"])
    server.start()
    server.io_loop.start()


def callback():
    data_holder.update_next()
    _source.data = ColumnDataSource(data=data_holder.get_data()).data


def modify_doc(doc: Document):
    plot = figure()
    plot.circle('t', 'busy', source=_source)

    doc.add_periodic_callback(callback, 200)
    doc.add_root(plot)
