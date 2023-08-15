from db import db

class PokemonTypes(db.Model):
    __tablename__ = "pokemon_types"

    id = db.Column(db.Integer, primary_key=True)
    pokemon_id = db.Column(db.Integer, db.ForeignKey("pokemon.id"))
    type_id = db.Column(db.Integer, db.ForeignKey("types.id"))