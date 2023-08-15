from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from schemas import MoveSchema
from models import MoveModel, PokemonModel
from db import db

blp = Blueprint("moves", __name__, description="Operations on moves")

@blp.route("/move")
class MoveList(MethodView):
    @blp.response(200, MoveSchema(many=True))
    def get(self):
        return MoveModel.query.all()

    @blp.arguments(MoveSchema)
    @blp.response(201, MoveSchema)
    def post(self, move_data):
        move = MoveModel(**move_data)

        try:
            db.session.add(move)
            db.session.commit()
        except IntegrityError:
            abort(400, message="The specified move already exists in the database!")
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the move")

        return move

@blp.route("/move/<int:move_id>")
class Move(MethodView):
    @blp.response(200, MoveSchema)
    def get(self, move_id):
        move = MoveModel.query.get_or_404(move_id)
        return move
    
@blp.route("/pokemon/<int:pokemon_id>/move/<int:move_id>")
class LinkMovetoPokemon(MethodView):
    @blp.response(201)
    def post(self, pokemon_id, move_id):
        pokemon = PokemonModel.query.get_or_404(pokemon_id)
        move = MoveModel.query.get_or_404(move_id)

        pokemon.moves.append(move)

        try:
            db.session.add(pokemon)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while linking the move")
        
        return {"message": "Move linked to pokemon"}