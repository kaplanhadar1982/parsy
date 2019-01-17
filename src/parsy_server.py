from flask import Flask,request,jsonify
from flask_cors import CORS
from config import Config
from routes import *

class ParseServer(object):

    def __init__(self):
        self._app = Flask(__name__)
        CORS(self._app)
        self._app.register_blueprint(routes)

    
    def start(self):
        self._app.run('0.0.0.0',3333)

    

ps = ParseServer()
ps.start()