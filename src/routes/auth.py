from re import split
from flask import Blueprint, request, jsonify
from .function_jwt import write_token, validate_token


routes_auth = Blueprint("routes_auth", __name__)


@routes_auth.route("/login", methods=["POST"])
def login():
    data = request.json["username"]
    if data == "Daniel Salinas":
        return write_token(data=request.json)
    else:
        print(data)
        print(type(data))
        response = jsonify({"Mensaje": "Usuario no existe"})
        response.status_code = 404
        return response

@routes_auth.route("/verify/token")
def verify():
    token = request.headers['Authorization'].split(" ")[1]
    return validate_token(token, output=True)