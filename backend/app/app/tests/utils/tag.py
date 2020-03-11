from app import crud
from app.db.session import db_session
from app.schemas.tag import TagCreate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string


def create_random_tag(owner_id: int = None):
    if owner_id is None:
        user = create_random_user()
        owner_id = user.id
    title = random_lower_string()
    description = random_lower_string()
    text = random_lower_string()
    tag_in = TagCreate(title=title, description=description, text=text, id=id)
    return crud.tag.create_with_owner(
        db_session=db_session, obj_in=tag_in, owner_id=owner_id
    )
