from typing import List

from pydantic import BaseModel

from .user import User
from pydantic.color import Color


# Shared properties
class TagBase(BaseModel):
    title: str = None
    public: bool = None
    color: Color = None


# Properties to receive on tag creation
class TagCreate(TagBase):
    title: str
    public: bool = False
    color: Color = "00ffff"
    # color: Color = pickColor() TODO: Randomly assign color


# Properties to receive on tag update
class TagUpdate(TagBase):
    pass


# Properties shared by models stored in DB
class TagInDBBase(TagBase):
    id: int
    title: str
    owner_id: int
    public: bool
    color: Color


    class Config:
        orm_mode = True


# Properties to return to client
class Tag(TagInDBBase):
    pass


# Properties properties stored in DB
class TagInDB(TagInDBBase):
    pass
