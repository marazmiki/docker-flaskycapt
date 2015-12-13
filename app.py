#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals
from __future__ import absolute_import
from flask import Flask, request, jsonify
import threading
import requests as rqlib
import subprocess
import tempfile
import os
import six


def async(func):
    """
    Decorator makes wrapped function to run asynchronously
    """
    def wrapper(*args, **kwargs):
        thr = threading.Thread(target=func, args=args, kwargs=kwargs)
        thr.start()
    return wrapper


@async
def cutycapt(url, callback_url, min_width=1680, min_height=1280, delay=0):
    """
    Runs cutycapt and send resulted snapshot into callback
    url with HTTP POST method.
    """
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as fp:
        out = fp.name
        subprocess.check_output(map(six.text_type, [
            'cutycapt',
            '--url={}'.format(url),
            '--out={}'.format(url),
            '--min-width={}'.format(min_width),
            '--min-height={}'.format(min_height),
            '--delay={}'.format(delay),
        ]),
        env={
            'DISPLAY': DISPLAY,
        })
        fp.seek(0)
        requests.post(callback_url,
                      files={'file': fp},
                      verify=False)
    if os.path.exists(out):
        os.remove(out)


app = Flask(__name__)
requests = rqlib.Session()
DISPLAY = ':99'


@app.route('/thumbnail', methods=['POST'])
def thumbnail():
    data = request.get_json()
    cutycapt(url=data['url'],
             callback_url=data['callback'])
    return jsonify(**data)


if __name__ == '__main__':
    app.run(debug=True)
