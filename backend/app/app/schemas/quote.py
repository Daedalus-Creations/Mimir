from pydantic import BaseModel

from .user import User
from pydantic.color import Color


# Shared properties
class QuoteBase(BaseModel):
    title: str = None
    description: str = None
    public: bool = None
    color: Color = None


# Properties to receive on quote creation
class QuoteCreate(QuoteBase):
    title: str
    public: bool = False

# Properties to receive on quote update
class QuoteUpdate(QuoteBase):
    pass


# Properties shared by models stored in DB
class QuoteInDBBase(QuoteBase):
    id: int
    title: str
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Quote(QuoteInDBBase):
    pass


# Properties properties stored in DB
class QuoteInDB(QuoteInDBBase):
    pass
