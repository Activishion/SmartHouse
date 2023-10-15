from datetime import datetime

from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from base.model import Base


class Location(Base):
    __tablename__ = 'location'

    name: Mapped[str] = mapped_column(String(100))
    sensors: Mapped[int] = mapped_column(ForeignKey('sensors.id'))
    date_create: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())

    def __repr__(self) -> str:
        return self.name
