import time
from collections import defaultdict, deque
from functools import partial

_data = defaultdict(partial(deque, maxlen=10000))


def get_data():
    return _data


def get_keys():
    return _data.keys()


def post(**kwargs):

    t_ms = time.time() * 1000

    for k, v in kwargs.items():
        _data[k].append((v, t_ms))


