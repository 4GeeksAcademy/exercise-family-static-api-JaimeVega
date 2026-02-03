"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
# from models import Person


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the jackson family object
jackson_family = FamilyStructure("Jackson")


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/members', methods=['GET'])
def get_all():
    # This is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {"family": members}
    return jsonify(response_body), 200

@app.route('/member/<int:position>', methods=['GET'])
def get_one(position):
    # This is how you can use the Family datastructure by calling its methods
    if type(position) != int:
        message = 'numero malo' 
        return jsonify(message), 400
    member = jackson_family.get_member(position)
    response_body = {"member": member}
    return jsonify(response_body), 200

@app.route('/member', methods=['POST'])
def add_member():
    # This is how you can use the Family datastructure by calling its methods
    request_body = request.json
    if len(request_body) != 3:
        message = 'faltan datos' 
        return jsonify(message), 400
    elif jackson_family.repeat_member(request_body):
        return jsonify('Ya existe'), 400
    new_member = jackson_family.add_member(request_body)
    return jsonify(new_member), 201

@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    # This is how you can use the Family datastructure by calling its methods
    new_member = jackson_family.delete_member(id)
    return jsonify(new_member), 200

# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
