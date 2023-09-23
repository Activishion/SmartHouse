from abc import ABC, abstractmethod

from fastapi import status
from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError
    
    @abstractmethod
    async def find_one_by_id():
        raise NotImplementedError
    
    @abstractmethod
    async def find_all():
        raise NotImplementedError
    
    @abstractmethod
    async def edit_one():
        raise NotImplementedError
    
    @abstractmethod
    async def delete_by_id():
        raise NotADirectoryError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict) -> int:
        stmt = (
            insert(self.model)
            .values(**data)
            .returning(self.model.id)
        )
        result = await self.session.execute(stmt)
        return result.scalar_one()                      # ??

    async def find_one_by_id(self, id: int):
        query = select(self.model).filter_by(id=id)
        result = await self.session.execute(query)
        result = result.scalar_one_or_none()
        if result is None:
            return result
        return result.to_read_model() # ??
    
    async def find_all(self):
        query = select(self.model)
        result = await self.session.execute(query)
        res = [row[0].to_read_model() for row in result.fetchall()]         # ??
        return res
    
    async def edit_one(self, id: int, data: dict) -> int:
        stmt = (
            update(self.model)
            .values(**data)
            .filter_by(id=id)
            .returning(self.model.id)
        )
        res = await self.session.execute(stmt)
        return res.scalar_one()
    
    async def delete_by_id(self, id: int):
        stmt = delete(self.model).where(self.model.id == id)
        await self.session.execute(stmt)
        return status.HTTP_200_OK
