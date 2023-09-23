from fastapi import APIRouter

from base.dependencies import ContextManagerDepends
from sensors.schemas import SensorRead


router = APIRouter()


@router.post('/')
async def get_sensors_by_location(
    location: str,
    cmd: ContextManagerDepends
) -> list[SensorRead]:
    pass


@router.post('/')
async def create_new_sensor() -> SensorRead:
    pass
