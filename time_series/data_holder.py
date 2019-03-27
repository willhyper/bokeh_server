from collections import defaultdict, deque
from functools import partial

from math import sin

_data = defaultdict(partial(deque, maxlen=30))


def data_gen():
    cnt = 0
    while True:
        t = cnt / 10
        yield (t, sin(t))
        cnt += 1


dg = data_gen()


def update_next():
    t, b = next(dg)
    _data['t'].append(t)
    _data['busy'].append(b)


update_next() # so that _data is non-empty


def get_data():
    return _data
