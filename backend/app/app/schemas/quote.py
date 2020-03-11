from typing import List

from pydantic import BaseModel

from .tag import Tag
from .user import User
from pydantic.color import Color


# Shared properties
class QuoteBase(BaseModel):
    title: str = None
    text: str = None
    type: str = None
    description: str = None
    public: bool = None
    color: Color = None
    tags: List[Tag] = []


# Properties to receive on quote creation
class QuoteCreate(QuoteBase):
    text: str
    type: str = "Uncategorized"
    public: bool = False

# Properties to receive on quote update
class QuoteUpdate(QuoteBase):
    pass

# Properties to search for in quotes
class QuoteSearch(BaseModel):
    any: str = None
    title: str = None
    text: str = None
    type: str = None
    description: str = None
    public: bool = None
    color: Color = None
    tags: List[Tag] = []

# Properties shared by models stored in DB
class QuoteInDBBase(QuoteBase):
    id: int
    text: str
    type: str
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Quote(QuoteInDBBase):
    pass


# Properties properties stored in DB
class QuoteInDB(QuoteInDBBase):
    pass
