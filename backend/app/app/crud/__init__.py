from .crud_user import user
from .crud_bookmark import bookmark

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.bookmark import Bookmark
# from app.schemas.bookmark import BookmarkCreate, BookmarkUpdate

# bookmark = CRUDBase[Bookmark, BookmarkCreate, BookmarkUpdate](Bookmark)
