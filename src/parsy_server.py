from flask import Flask,request,jsonify
from flask_cors import CORS
from routes import *

app = Flask(__name__)
CORS(app)
app.register_blueprint(routes)


@app.route("/",methods=['GET'])
def get_ui():
    return 'this is the zerver speeking'


if __name__ == '__main__':
    app.run('0.0.0.0',3333)
