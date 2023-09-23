from base.repository import SQLAlchemyRepository
from location.models import Location


class LocationRepository(SQLAlchemyRepository):
    model = Location
