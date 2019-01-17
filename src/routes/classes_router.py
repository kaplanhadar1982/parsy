from flask import request,jsonify
from . import routes



@routes.route("/classes/<class_name>",methods=['GET'])
def handle_find(class_name):
    return jsonify({"class_name": class_name}),200


@routes.route("/classes/<class_name>/<object_id>",methods=['GET'])
def handle_get(class_name,object_id):
    return jsonify({"class_name": class_name,"object_id":object_id}),200


@routes.route("/classes/<class_name>",methods=['POST'])
def handle_post(class_name):
    print(request.json)
    return jsonify({"class_name": class_name}),201


@routes.route("/classes/<class_name>/<object_id>",methods=['PUT'])
def handle_put(class_name,object_id):
    return jsonify({"class_name": class_name,"object_id":object_id}),200


@routes.route("/classes/<class_name>/<object_id>",methods=['DELETE'])
def handle_delete(class_name,object_id):
    return jsonify({"class_name": class_name,"object_id":object_id}),200

