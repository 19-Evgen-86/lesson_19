from flask import request
from flask_restx import Namespace, Resource

from implemented import auth_service
from utils import get_token_from_headers

auth_ns = Namespace("auth")


@auth_ns.route("/")
class AuthView(Resource):
    def post(self):
        return auth_service.login(request.json)

    def put(self):
        data = get_token_from_headers(request.json["refresh_token"])
        return auth_service.get_new_tokens(data)
