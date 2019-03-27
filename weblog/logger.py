from concurrent.futures import ThreadPoolExecutor

import requests


from .flask_app import addr, port
from functools import partial

url = f'http://{addr}:{port}'
_post = partial(requests.post, url)


_executor = ThreadPoolExecutor(max_workers=20)


def _log(**kwargs):
    return _post(json=kwargs)


def log(**kwargs):
    _executor.submit(_log, **kwargs)

