from bokeh.document import Document

from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.server.server import Server
from bokeh.palettes import Spectral4
from tornado.ioloop import IOLoop

from . import data_holder


addr = 'localhost'
port = 5006
app_name = 'bkapp'
url = f'http://{addr}:{port}/{app_name}'


def start_server(addr, port):
    allow = [f'localhost:{port}', f'0.0.0.0:{port}', f'{addr}:{port}']
    server = Server({f'/{app_name}': modify_doc}, io_loop=IOLoop(), allow_websocket_origin=allow)
    server.start()
    server.io_loop.start()



def modify_doc(doc: Document):
    plot = figure(x_axis_type='datetime')

    # _source = ColumnDataSource(data=data_holder.get_data())

    def callback():
        d = data_holder.get_data()
        # d = {'a': [(1,123), (2,130), (3, 133)], 'b':[(4,123),(5,130),(6,133)]}

        for k_vtlist, color in zip(d.items(), Spectral4):
            k, vt_list = k_vtlist
            v, t = zip(*vt_list)
            plot.circle(t,v, legend=k, color=color)


    doc.add_next_tick_callback(callback)

    doc.add_root(plot)
