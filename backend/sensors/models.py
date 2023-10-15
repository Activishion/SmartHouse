from datetime import datetime

from sqlalchemy import String, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from base.model import Base


class Sensor(Base):
    __tablename__ = 'sensors'

    name: Mapped[str] = mapped_column(String(100))
    # единица измерения
    status: Mapped[bool] = mapped_column(Boolean, default=False)
    date_create: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())

    def __repr__(self) -> str:
        return self.name
