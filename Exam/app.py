from flask import Flask, jsonify, request

from logic import ControlledObjectService
from errors import BusinessLogicError, to_error_payload

app = Flask(__name__)
service = ControlledObjectService()


# централізована обробка помилок бізнес-логіки 
@app.errorhandler(BusinessLogicError)
def handle_business_error(err: BusinessLogicError):
    payload, status = to_error_payload(err)
    return jsonify(payload), status


# помилки, які не валять сервер 
@app.errorhandler(Exception)
def handle_unexpected_error(err: Exception):
    return jsonify({"error": "internal_error", "message": "Unexpected server error"}), 500


# необхідні endpoints 
@app.get("/objects")
def list_objects():
    objs = service.list_objects()
    return jsonify([o.to_dict() for o in objs]), 200


@app.post("/objects")
def create_object():
    data = request.get_json(silent=True) or {}
    name = data.get("name")
    value = data.get("value")
    description = data.get("description")

    obj = service.create_object(name=name, value=value, description=description)
    return jsonify(obj.to_dict()), 201


@app.get("/objects/<int:obj_id>")
def get_object(obj_id: int):
    obj = service.get_object(obj_id)
    return jsonify(obj.to_dict()), 200


@app.patch("/objects/<int:obj_id>")
def update_object(obj_id: int):
    data = request.get_json(silent=True) or {}
    name = data.get("name")
    value = data.get("value")
    description = data.get("description")

    obj = service.update_object(obj_id, name=name, value=value, description=description)
    return jsonify(obj.to_dict()), 200


@app.delete("/objects/<int:obj_id>")
def delete_object(obj_id: int):
    service.delete_object(obj_id)
    return jsonify({"status": "deleted", "id": obj_id}), 200


if __name__ == "__main__":
    app.run(debug=True)