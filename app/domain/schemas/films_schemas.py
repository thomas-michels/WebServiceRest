from typing import List
from pydantic import BaseModel
from app.domain.schemas.actors_schemas import Actor


class FilmBase(BaseModel):
    title: str
    year: int


class FilmCreate(FilmBase):
    pass


class Film(FilmBase):
    id: int
    is_active: bool
    roster: List[Actor]

    class Config:
        orm_mode = True
