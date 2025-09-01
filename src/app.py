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

#####
jackson_family.add_member({
    "first_name": "John",
    "age": 33,
    "lucky_numbers": [7, 13, 22]
})
jackson_family.add_member({
    "first_name": "Jane",
    "age": 35,
    "lucky_numbers": [10, 14, 3]
})
jackson_family.add_member({
    "first_name": "Jimmy",
    "age": 5,
    "lucky_numbers": [1]
})

#####



# Handle/serialize errors like a JSON object

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# 1) GET /members - obtener todos los miembros
@app.route("/members", methods=["GET"])
def get_members():
    try:
        members = jackson_family.get_all_members()
        return jsonify(members), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# 2) GET /members/<int:member_id> - obtener un miembro
@app.route("/members/<int:member_id>", methods=["GET"])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    return jsonify({"error": "Member not found"}), 404


# 3) POST /members - agregar un miembro
@app.route("/members", methods=["POST"])
def add_member():
    try:
        member_data = request.get_json()
        if not member_data:
            return jsonify({"error": "Invalid request"}), 400
        new_member = jackson_family.add_member(member_data)
        return jsonify(new_member), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# 4) DELETE /members/<int:member_id> - eliminar un miembro
@app.route("/members/<int:member_id>", methods=["DELETE"])
def delete_member(member_id):
    deleted = jackson_family.delete_member(member_id)
    if deleted:
        return jsonify({"done": True}), 200
    return jsonify({"error": "Member not found"}), 404


# Solo si corres localmente
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3245, debug=True)

