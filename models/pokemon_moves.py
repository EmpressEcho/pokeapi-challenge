from db import db

class PokemonMoves(db.Model):
    __tablename__ = "pokemon_moves"

    id = db.Column(db.Integer, primary_key=True)
    pokemon_id = db.Column(db.Integer, db.ForeignKey("pokemon.id"))
    move_id = db.Column(db.Integer, db.ForeignKey("moves.id"))