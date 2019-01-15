from flask import jsonify
from . import routes

@routes.route('/health')
def health():
    return jsonify({"health": "ok"}),200