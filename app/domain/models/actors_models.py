from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Actor(Base):
    __tablename__ = "actors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    password = Column(String)
    age = Column(Integer)
    is_active = Column(Boolean, default=True)

    film = relationship('Film', secondary='acting')
