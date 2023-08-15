from db import db

class PokemonModel(db.Model):
    __tablename__ = "pokemon"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=False)
    species = db.Column(db.String(255), unique=False, nullable=False)
    base_experience = db.Column(db.Integer, unique=False, nullable=False)

    types = db.relationship("TypeModel", back_populates="pokemon", secondary="pokemon_types")
    moves = db.relationship("MoveModel", back_populates="pokemon", secondary="pokemon_moves")