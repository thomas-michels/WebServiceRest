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
    user_type_id: int

    class Config:
        orm_mode = True
