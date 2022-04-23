from dao.director import DirectorDao
from dao.model.directors import DirectorSchema
from utils import handling_exceptions

director_schemas = DirectorSchema(many=True)
director_schema = DirectorSchema()


class DirectorService:
    def __init__(self, director_dao: DirectorDao):
        self.director_dao = director_dao

    @handling_exceptions
    def get_director_all(self):
        result = self.director_dao.get_all()
        if result:
            return director_schemas.dump(result)
        else:
            return {"message": "Genres into database not found"}

    @handling_exceptions
    def get_director(self, did):
        result = self.director_dao.get_one(did)
        if result:
            return director_schema.dump(result)
        else:
            return {"message": f"Genre with ID: '{did}' not found"}
