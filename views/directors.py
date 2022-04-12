from flask import request
from flask_restx import Namespace, Resource

director_ns = Namespace("directors")


@director_ns.route("/")

class DirectorsView(Resource):
    @director_ns.param("uid", "ID Режиссера")
    @director_ns.response(200, description="Возвращает данные режиссера по ID, либо список всех режиссеров")
    @director_ns.response(404, description="Режиссер не найден")
    def get(self):
        uid = request.args.get("uid")
        if uid:
            return uid
        else:
            return "all"
