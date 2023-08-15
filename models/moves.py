from db import db

class MoveModel(db.Model):
    __tablename__ = "moves"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

    pokemon = db.relationship("PokemonModel", back_populates="moves", secondary="pokemon_moves")