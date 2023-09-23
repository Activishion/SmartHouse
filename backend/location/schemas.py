from datetime import datetime

from pydantic import BaseModel


class LocationBase(BaseModel):
    name: str
    date_create: datetime


class LocationRead(LocationBase):
    id: int


class LocationCreate(LocationBase):
    pass


class LocationUpdate(LocationBase):
    id: int