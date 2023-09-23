from abc import abstractmethod
from typing import Type

from config.database import async_session_maker
from location.repository import LocationRepository
from sensors.repository import SensorRepository


class InterfaseContextManager:
    location: Type[LocationRepository]
    sensor: Type[SensorRepository]

    @abstractmethod 
    def __init__(self):
        pass

    @abstractmethod
    async def __aenter__(self):
        pass

    @abstractmethod
    async def __aexit__(self, *args):
        pass

    @abstractmethod
    async def commit(self):
        pass

    @abstractmethod
    async def rollback(self):
        pass


class ContextManager:
    def __init__(self):
        self.session_factory = async_session_maker

    async def __aenter__(self):
        self.session = self.session_factory()

        self.location = LocationRepository(self.session)
        self.sensor = SensorRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
