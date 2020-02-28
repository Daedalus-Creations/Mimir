from app import crud
from app.db.session import db_session
from app.schemas.bookmark import BookmarkCreate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string


def create_random_bookmark(owner_id: int = None):
    if owner_id is None:
        user = create_random_user()
        owner_id = user.id
    title = random_lower_string()
    description = random_lower_string()
    bookmark_in = BookmarkCreate(title=title, description=description, id=id)
    return crud.bookmark.create_with_owner(
        db_session=db_session, obj_in=bookmark_in, owner_id=owner_id
    )
