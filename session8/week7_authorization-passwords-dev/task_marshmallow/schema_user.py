from marshmallow import Schema, fields

from utils import hash_password

class UserSchema(Schema):
    class Meta:
        ordered = True

    id = fields.Int(dump_only=True)
    username = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.Method(required=True, deserialize='load_password')

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    def load_password(self, value):
        return hash_password(value)

user_schema = UserSchema()
user_public_schema = UserSchema(exclude=('email', ))


# TODO 
# -- try to understand what the code does 

# -- What functions has the serialization saved us ?

# -- how to validate input ?

# -- what do these do?
# --    dump_only ?
# --    deserialize ?

# -- can we interact with SQLAlchemy ?

# -- what other extension have we used previously for data input validation?
