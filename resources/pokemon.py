from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from schemas import PokemonSchema
from models import PokemonModel
from db import db

blp = Blueprint("pokemon", __name__, description="Operations on pokemon")

@blp.route("/pokemon")    # Routes requests to the /pokemon endpoint to the decorated class
class PokemonList(MethodView):
    @blp.response(200, PokemonSchema(many=True))   # Defines the main success response, to be detailed in the documentation
    def get(self):
        return PokemonModel.query.all()    # Fetches a list of all pokemon from the database

    @blp.arguments(PokemonSchema)   # Validates passed data, and passes it into the method as an argument
    @blp.response(201, PokemonSchema)
    def post(self, pokemon_data):
        pokemon = PokemonModel(**pokemon_data)    # Creates a new pokemon item using the data passed in the request body

        try:
            db.session.add(pokemon)    # Adds the pokemon item to the database
            db.session.commit()    # Commits the change to the database
        except IntegrityError:
            abort(400, message="The specified pokemon already exists in the database!")
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the pokemon")

        return pokemon
    
@blp.route("/pokemon/<int:pokemon_id>")
class Pokemon(MethodView):
    @blp.response(200, PokemonSchema)
    def get(self, pokemon_id):
        pokemon = PokemonModel.query.get_or_404(pokemon_id)    # Fetches the pokemon from the database by the primary key, and if it cannot find it, automatically aborts with a 404
        return pokemon