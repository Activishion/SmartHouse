from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base


class Base(DeclarativeBase):
    __abstract__ = True
    __tablename__ = None

    id: Mapped[int] = mapped_column(primary_key=True)


base = declarative_base()
