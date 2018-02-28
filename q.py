#!/usr/bin/env python3 
import sys
import importlib
importlib.reload(sys)
from flask import request
from flask import Flask 
from flask import jsonify 
from flask import Response
import simplejson as json
app = Flask(__name__)

def render_html (results=None):
    txt = """
            <html>....
            <body>
            <form action='/query' method='get'>
                
            </form>
            """
    if results is not None:
        txt += "<pre>" + json.dumps(results) + "</pre>" #display raw html code in PRE
        pass
    reulst s+ </body..
    return results
      

@app.route("/")
def get():
    return Response(render_html(), mimetype='text/html')

@app.route("/query")
def get():
    print(request.args)
    return Response(render_html(results), mimetype='text/plain')
'''
def jsonify(status=200, indent=4, sort_keys=True, **kwargs):
    response = make_response(dumps(dict(**kwargs), indent=indent, sort_keys=sort_keys))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    response.headers['mimetype'] = 'application/json'
    response.status_code = status
    return response
'''
