import os

DATABASE_PATH = os.path.join(os.getcwd(), "base.db")

PWD_HASH_SALT = b'secret here'
PWD_HASH_ITERATIONS = 100_000
PWD_HASH_NAME = 'sha256'

SECRET_KEY = "s3cR$eT"
ALGO = 'HS256'