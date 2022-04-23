from flask_restx import Resource, Namespace

user_ns = Namespace('users')


class UserView(Resource):
    def get(self):
        ...

    def post(self):
        ...

    def put(self):
        ...
