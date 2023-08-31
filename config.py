from dotenv import dotenv_values

env = dotenv_values(".env")


class Config:
    SECRET_KEY = env.get("SECRET_KEY")
    SQL = env.get("SQL")
    SQLALCHEMY_DATABASE_URI = env.get("SQL")
    DEBUG = True
    DEFAULT_URL_PATH = env.get("DEFAULT_URL_PATH")
