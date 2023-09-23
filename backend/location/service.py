from fastapi import status

from base.utils import InterfaseContextManager
from location.schemas import LocationRead, LocationCreate, LocationUpdate


class LocationService:
    async def get_list_location(
        self,
        context: InterfaseContextManager
    ) -> list[LocationRead]:
        async with context:
            location_list = await context.location.find_all()
            return
        
    async def get_location_by_id(
        self,
        id: int,
        context: InterfaseContextManager
    ) -> LocationRead:
        async with context:
            location_id = await context.location.find_one_by_id(id=id)
            return
        
    async def create_new_location(
        self,
        location: LocationCreate,
        context: InterfaseContextManager
    ):
        async with context:
            new_location = await context.location.add_one(location)
            return
        
    async def update_location(
        self,
        location: LocationUpdate,
        context: InterfaseContextManager
    ) -> LocationRead:
        async with context:
            location_dict = location.model_dump()
            location_id = location_dict['id']
            updated_location = await context.location.edit_one()

    async def delete_one_location_by_id(
        self,
        id: int,
        context: InterfaseContextManager
    ):
        async with context:
            location_id = await context.location.find_one_by_id(id=id)
            if not location_id:
                return None
            response = await context.location.delete_by_id(id=id)
            return response
