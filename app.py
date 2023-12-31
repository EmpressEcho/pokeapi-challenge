import os
from typing import Optional
from flask import Flask
from flask_smorest import Api
from db import db
import models
from resources import PokemonBlueprint, MoveBlueprint, TypeBlueprint, UpdateBlueprint

def create_app(db_url:Optional[str]=None):
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "PokeAPI Challenge"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    db.init_app(app)

    api = Api(app)
    api.register_blueprint(PokemonBlueprint)
    api.register_blueprint(MoveBlueprint)
    api.register_blueprint(TypeBlueprint)
    api.register_blueprint(UpdateBlueprint)

    with app.app_context():
        db.create_all()

    return app