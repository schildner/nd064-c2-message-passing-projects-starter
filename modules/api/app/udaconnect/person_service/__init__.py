from app.udaconnect.person_service.model import Person  # noqa
from app.udaconnect.person_service.schema import PersonSchema  # noqa


def register_routes(api, app, root="api"):
    from app.udaconnect.person_service.controller import api as person_api

    api.add_namespace(person_api, path=f"/{root}")
