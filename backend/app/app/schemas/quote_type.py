from enum import Enum
from typing import List

from pydantic import BaseModel

from .user import User
from pydantic.color import Color


class QuoteType(str, Enum):
    book = "Book"
    film = "Film"
    poem = "Poem"
    speech = "Speech"
    web = "Web"
    other = "Other"
    uncategorized = "Uncategorized"

# Shared properties
# class QuoteType(BaseModel):
#     title: str = None
#     public: bool = None
#     color: Color = None
