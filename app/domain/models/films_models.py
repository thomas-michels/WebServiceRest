from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Film(Base):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    year = Column(Integer)
    roster = Column(Integer, ForeignKey('actors.id'), use_list=True)
    is_active = Column(Boolean, default=True)

    actor = relationship('Actor', secondary='acting')
