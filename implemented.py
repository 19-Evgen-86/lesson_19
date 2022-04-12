# файл для создания DAO и сервисов чтобы импортировать их везде
from dao.movie import MovieDao
from service.movie import MovieService
from setup_db import db

movie_dao = MovieDao(db.session)
movie_service = MovieService(movie_dao)
