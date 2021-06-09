from pydantic import BaseModel


class Token(BaseModel):
    access_token: str

    class Config:
        orm_mode = True
