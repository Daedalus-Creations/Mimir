from app import crud
from app.schemas.quote import QuoteCreate, QuoteUpdate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string
from app.db.session import db_session


def test_create_quote():
    title = random_lower_string()
    description = random_lower_string()
    quote_in = QuoteCreate(title=title, description=description)
    user = create_random_user()
    quote = crud.quote.create_with_owner(
        db_session=db_session, obj_in=quote_in, owner_id=user.id
    )
    assert quote.title == title
    assert quote.description == description
    assert quote.owner_id == user.id


def test_get_quote():
    title = random_lower_string()
    description = random_lower_string()
    quote_in = QuoteCreate(title=title, description=description)
    user = create_random_user()
    quote = crud.quote.create_with_owner(
        db_session=db_session, obj_in=quote_in, owner_id=user.id
    )
    stored_quote = crud.quote.get(db_session=db_session, id=quote.id)
    assert quote.id == stored_quote.id
    assert quote.title == stored_quote.title
    assert quote.description == stored_quote.description
    assert quote.owner_id == stored_quote.owner_id


def test_update_quote():
    title = random_lower_string()
    description = random_lower_string()
    quote_in = QuoteCreate(title=title, description=description)
    user = create_random_user()
    quote = crud.quote.create_with_owner(
        db_session=db_session, obj_in=quote_in, owner_id=user.id
    )
    description2 = random_lower_string()
    quote_update = QuoteUpdate(description=description2)
    quote2 = crud.quote.update(db_session=db_session, db_obj=quote, obj_in=quote_update)
    assert quote.id == quote2.id
    assert quote.title == quote2.title
    assert quote2.description == description2
    assert quote.owner_id == quote2.owner_id


def test_delete_quote():
    title = random_lower_string()
    description = random_lower_string()
    quote_in = QuoteCreate(title=title, description=description)
    user = create_random_user()
    quote = crud.quote.create_with_owner(db_session=db_session, obj_in=quote_in, owner_id=user.id)
    quote2 = crud.quote.remove(db_session=db_session, id=quote.id)
    quote3 = crud.quote.get(db_session=db_session, id=quote.id)
    assert quote3 is None
    assert quote2.id == quote.id
    assert quote2.title == title
    assert quote2.description == description
    assert quote2.owner_id == user.id
