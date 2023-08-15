from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from schemas import TypeSchema
from models import TypeModel, PokemonModel
from db import db

blp = Blueprint("types", __name__, description="Operations on types")

@blp.route("/type")
class TypeList(MethodView):
    @blp.response(200, TypeSchema(many=True))
    def get(self):
        return TypeModel.query.all()
    
    @blp.arguments(TypeSchema)
    @blp.response(201, TypeSchema)
    def post(self, type_data):
        type = TypeModel(**type_data)

        try:
            db.session.add(type)
            db.session.commit()
        except IntegrityError:
            abort(400, message="The specified type already exists in the database!")
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the type")

        return type

@blp.route("/type/<int:type_id>")
class Type(MethodView):
    @blp.response(200, TypeSchema)
    def get(self,type_id):
        type = TypeModel.query.get_or_404(type_id)
        return type

@blp.route("/pokemon/<int:pokemon_id>/type/<int:type_id>")
class LinkTypetoPokemon(MethodView):
    @blp.response(201, TypeSchema)
    def post(self, pokemon_id, type_id):
        pokemon = PokemonModel.query.get_or_404(pokemon_id)
        type = TypeModel.query.get_or_404(type_id)

        pokemon.types.append(type)

        try:
            db.session.add(pokemon)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while linking the type")
        
        return type