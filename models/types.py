from db import db

class TypeModel(db.Model):
    __tablename__ = "types"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

    pokemon = db.relationship("PokemonModel", back_populates="types", secondary="pokemon_types")