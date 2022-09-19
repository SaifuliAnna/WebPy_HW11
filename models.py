
from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table, MetaData
from sqlalchemy.sql.sqltypes import DateTime

from db import Base, engine, db_session


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    nickname = Column(String(50), nullable=False)
    name = Column(String(50), nullable=True)
    surname = Column(String(50), nullable=True)
    phone = Column(String(150), nullable=False, unique=True)
    email = Column(String(125), nullable=True, unique=True)
    birthday = Column(String(25), nullable=True)
    address = Column(String(25), nullable=True)
    created = Column(DateTime, default=datetime.now())

    def __repr__(self) -> str:
        return f"{self.nickname}, {self.name}, {self.surname}, {self.phone}, {self.email}, {self.birthday}," \
               f" {self.address}"


if __name__ == "__main__":
    Base.metadata.create_all(engine)