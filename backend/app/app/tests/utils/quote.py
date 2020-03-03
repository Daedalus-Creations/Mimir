from app import crud
from app.db.session import db_session
from app.schemas.quote import QuoteCreate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string


def create_random_quote(owner_id: int = None):
    if owner_id is None:
        user = create_random_user()
        owner_id = user.id
    title = random_lower_string()
    description = random_lower_string()
    quote_in = QuoteCreate(title=title, description=description, id=id)
    return crud.quote.create_with_owner(
        db_session=db_session, obj_in=quote_in, owner_id=owner_id
    )
