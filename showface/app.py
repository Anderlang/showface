# -*- coding: utf-8 -*-
"""
    主程序.
    :copyright: © 2018 by Ander.
    :license: MIT, see LICENSE for more details.
"""
import time
from flask import Flask,request,render_template
from gevent import monkey
from gevent.pywsgi import WSGIServer

monkey.patch_all()

app=Flask(__name__)

@app.route('/')
def helloworld():
    time.sleep(10)
    return render_template('index.html')

@app.route('/home')
def hellohome():
    return '异步立刻出现'

if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', 8000), app)
    http_server.serve_forever()


        



