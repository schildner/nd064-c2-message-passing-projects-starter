from app.udaconnect.location_service.model import Location  # noqa
from app.udaconnect.location_service.schema import LocationSchema  # noqa


def register_routes(api, app, root="api"):
    from app.udaconnect.location_service.controller import api as location_api

    api.add_namespace(location_api, path=f"/{root}")
