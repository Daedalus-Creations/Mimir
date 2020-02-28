from pydantic import BaseModel

from .user import User

# Shared properties
class BookmarkBase(BaseModel):
    title: str = None
    description: str = None


# Properties to receive on bookmark creation
class BookmarkCreate(BookmarkBase):
    title: str


# Properties to receive on bookmark update
class BookmarkUpdate(BookmarkBase):
    pass


# Properties shared by models stored in DB
class BookmarkInDBBase(BookmarkBase):
    id: int
    title: str
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Bookmark(BookmarkInDBBase):
    pass


# Properties properties stored in DB
class BookmarkInDB(BookmarkInDBBase):
    pass
