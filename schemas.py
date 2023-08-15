from marshmallow import Schema, fields

class PlainTypeSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class PlainMoveSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class PlainPokemonSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class PokemonSchema(PlainPokemonSchema):
    description = fields.Str(required=True)
    species = fields.Str(required=True)
    base_experience = fields.Int(required=True)
    types = fields.List(fields.Nested(PlainTypeSchema()), dump_only=True)
    moves = fields.List(fields.Nested(PlainMoveSchema()), dump_only=True)

class MoveSchema(PlainMoveSchema):
    pokemon = fields.List(fields.Nested(PlainPokemonSchema()), dump_only=True)

class TypeSchema(PlainTypeSchema):
    pokemon = fields.List(fields.Nested(PlainPokemonSchema()), dump_only=True)