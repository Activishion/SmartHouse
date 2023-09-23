from fastapi import APIRouter, status

from base.dependencies import ContextManagerDepends
from location.schemas import LocationRead, LocationCreate, LocationUpdate
from location.service import LocationService


router = APIRouter()


@router.get('/')
async def get_list_locations(cmd: ContextManagerDepends) -> list[LocationRead]:
    location_list = await LocationService().get_list_location(context=cmd)


@router.post('/')
async def create_new_location(
    location: LocationCreate,
    cmd: ContextManagerDepends
) -> int:
    new_location_dict = location.model_dump()
    new_location_id = await LocationService().create_new_location(location=new_location_dict, context=cmd)
    return new_location_id


@router.put('/')
async def update_location(
    location: LocationUpdate,
    cmd: ContextManagerDepends
) -> LocationRead:
    location_dict = location.model_dump()


@router.delete('/')
async def delete_location(
    id: int,
    cmd: ContextManagerDepends
):
    """
    Delete location by id
    """
    status_delete = await LocationService().delete_one_location_by_id(id=id, context=cmd)

    return {'status_code': status_delete}
