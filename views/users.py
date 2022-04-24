from flask import request
from flask_restx import Resource, Namespace

from implemented import user_service
from utils import auth_required

user_ns = Namespace('users')


@user_ns.route("/")
@user_ns.route("/<int:uid>")
class UserView(Resource):
    @auth_required
    def get(self):
        result = user_service.get()
        return result, 200

    def post(self):
        data = request.json
        result = user_service.create(data)
        return result, 200

    def put(self, uid):
        data = request.json
        result = user_service.update(data, uid)
        return result, 201
