from flask_migrate import Migrate

import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    app_settings = config.Config
    app.config.from_object(app_settings)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_AS_ASCII"] = False
    app.config["JSON_SORT_KEYS"] = False

    # Register Blueprints

    from API.posts.views import posts_api
    from API.users.views import users_api

    app.register_blueprint(posts_api)
    app.register_blueprint(users_api)

    from API.posts.models import Posts
    from API.users.models import Users

    db.init_app(app)
    migrate.init_app(app, db)

    return app
