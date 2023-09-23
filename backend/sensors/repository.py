from base.repository import SQLAlchemyRepository
from sensors.models import Sensor


class SensorRepository(SQLAlchemyRepository):
    model = Sensor
