from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    id: str
    name: str
    email: str
    password: str
    created_date: datetime
    updated_date: datetime
    active: bool

    class Config:
        orm_mode = True
