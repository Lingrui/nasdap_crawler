#!/usr/bin/env python3 
import sys
import importlib
importlib.reload(sys)
from flask import request
from flask import Flask 
from flask import jsonify 
from flask import Response
import simplejson as json
from query import *
app = Flask(__name__)

@app.route("/")
def get():
    sec = request.args.get('symbol',default = 'goog',type = str)
    info = get_sec(sec) 
    return Response(json.dumps(json.loads(info), indent=4 * ' '), mimetype='text/plain')
'''
def jsonify(status=200, indent=4, sort_keys=True, **kwargs):
    response = make_response(dumps(dict(**kwargs), indent=indent, sort_keys=sort_keys))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['mimetype'] = 'application/json'
    response.status_code = status
    return response
'''
