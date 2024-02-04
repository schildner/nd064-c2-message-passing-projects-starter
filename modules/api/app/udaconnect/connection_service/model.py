from dataclasses import dataclass

from app.udaconnect.person_service.model import Person
from app.udaconnect.location_service.model import Location

@dataclass
class Connection:
    location: Location
    person: Person
