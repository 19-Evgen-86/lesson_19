from flask import request
from flask_restx import Namespace, Resource

from implemented import director_service
from utils import auth_required

director_ns = Namespace("directors")


@director_ns.route("/")
class DirectorsView(Resource):
    @director_ns.response(200, description="Возвращает список всех режиссеров")
    @auth_required
    def get(self):
        result = director_service.get_director_all()
        return result, 200

    @director_ns.response(200, description="Режиссер добавлен")
    def post(self):
        data = request.json
        result = director_service.add_director(data)
        return result, 200


@director_ns.route("/<int:uid>")
class DirectorView(Resource):
    @director_ns.param("uid", "ID Режиссера")
    @director_ns.response(200, description="Возвращает данные режиссера по ID")
    @auth_required
    def get(self, uid):
        result = director_service.get_director(uid)
        return result, 200

    @director_ns.doc(params={"did": "ID Режиссера", "data": "Данные для обновления"})
    @director_ns.response(201, description="Режиссер обновлен")
    def put(self, did):
        data = request.json
        result = director_service.update_movie(data, did)
        return result, 201

    @director_ns.param("did", "ID Режиссер")
    @director_ns.response(204, description="Режиссер удален")
    def delete(self, did):
        result = director_service.delete_movie(did)
        return result, 204
