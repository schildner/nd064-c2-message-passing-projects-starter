from app.udaconnect.person_service.schema import PersonSchema
from app.udaconnect.location_service.schema import LocationSchema
from marshmallow import Schema, fields


class ConnectionSchema(Schema):
    location = fields.Nested(LocationSchema)
    person = fields.Nested(PersonSchema)
