import threading
from functools import partial
from random import random

from bokeh.io import curdoc

import time

from bokeh.models import ColumnDataSource
from bokeh.plotting import figure

doc = curdoc()

src = ColumnDataSource(data=dict(x=[0], y=[0]))

def coro(x, y):
    src.stream(dict(x=[x], y=[y]))

def block_call():
    while True:

        time.sleep(0.1)
        x, y = random(), random()

        doc.add_next_tick_callback(partial(coro, x, y))

p, q = figure(), figure()

p.circle(x='x', y='y', source=src)
q.scatter(x='x', y='y', source=src)

doc.add_root(p)
doc.add_root(q)

t = threading.Thread(target=block_call, daemon=True)
t.start()