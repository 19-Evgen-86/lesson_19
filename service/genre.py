from dao.genre import GenreDao
from dao.model.genres import GenreSchema
from utils import handling_exceptions

genre_schemas = GenreSchema(many=True)
genre_schema = GenreSchema()


class GenreService:
    def __init__(self, genre_dao: GenreDao):
        self.genre_dao = genre_dao

    @handling_exceptions
    def get_genres_all(self):
        result = self.genre_dao.get_all()
        if result:
            return genre_schemas.dump(result)
        else:
            return {"message": "Genres into database not found"}

    @handling_exceptions
    def get_genre(self, gid):
        result = self.genre_dao.get_one(gid)
        if result:
            return genre_schema.dump(result)
        else:
            return {"message": f"Genre with ID: '{gid}' not found"}
