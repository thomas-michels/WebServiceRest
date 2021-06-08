from datetime import datetime
from pydantic import BaseModel


class Sale(BaseModel):
    id: str
    date: datetime
    active: bool

    class Config:
        orm_mode = True
