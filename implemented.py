# файл для создания DAO и сервисов чтобы импортировать их везде


from dao.director import DirectorDao
from dao.genre import GenreDao
from dao.movie import MovieDao
from service.director import DirectorService
from service.genre import GenreService
from service.movie import MovieService
from setup_db import db

movie_dao = MovieDao(db.session)
movie_service = MovieService(movie_dao)

director_dao = DirectorDao(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDao(db.session)
genre_service = GenreService(genre_dao)


