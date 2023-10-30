from datetime import datetime

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from base.model import BaseModel
from config.database import get_async_session


class User(SQLAlchemyBaseUserTable[int], BaseModel):
    __tablename__ = 'user'

    email: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)

    role_id: Mapped[int] = mapped_column(ForeignKey('role.id'))
 
    registered_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(default=False, nullable=False)

    def __repr__(self) -> str:
        return f"{self.username} - {self.email}"


class Role(BaseModel):
    __tablename__ = 'role'

    role: Mapped[str] = mapped_column()
    permission: Mapped[str] = mapped_column(ForeignKey('permission.id'))

    def __repr__(self) -> str:
        return self.role
    

class Permission(BaseModel):
    __tablename__ = 'permission'

    permission: Mapped[str] = mapped_column()

    def __repr__(self) -> str:
        return self.permission


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
