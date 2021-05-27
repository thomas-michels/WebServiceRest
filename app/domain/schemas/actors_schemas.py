from typing import List
from pydantic import BaseModel
from app.domain.schemas.films_schemas import Film


class ActorBase(BaseModel):
    name: str
    age: int


class ActorCreate(ActorBase):
    password: str


class Actor(ActorBase):
    id: int
    is_active: bool
    films: List[Film] = []

    class Config:
        orm_mode = True
