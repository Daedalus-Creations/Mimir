from app import crud
from app.schemas.bookmark import BookmarkCreate, BookmarkUpdate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string
from app.db.session import db_session


def test_create_bookmark():
    title = random_lower_string()
    description = random_lower_string()
    bookmark_in = BookmarkCreate(title=title, description=description)
    user = create_random_user()
    bookmark = crud.bookmark.create_with_owner(
        db_session=db_session, obj_in=bookmark_in, owner_id=user.id
    )
    assert bookmark.title == title
    assert bookmark.description == description
    assert bookmark.owner_id == user.id


def test_get_bookmark():
    title = random_lower_string()
    description = random_lower_string()
    bookmark_in = BookmarkCreate(title=title, description=description)
    user = create_random_user()
    bookmark = crud.bookmark.create_with_owner(
        db_session=db_session, obj_in=bookmark_in, owner_id=user.id
    )
    stored_bookmark = crud.bookmark.get(db_session=db_session, id=bookmark.id)
    assert bookmark.id == stored_bookmark.id
    assert bookmark.title == stored_bookmark.title
    assert bookmark.description == stored_bookmark.description
    assert bookmark.owner_id == stored_bookmark.owner_id


def test_update_bookmark():
    title = random_lower_string()
    description = random_lower_string()
    bookmark_in = BookmarkCreate(title=title, description=description)
    user = create_random_user()
    bookmark = crud.bookmark.create_with_owner(
        db_session=db_session, obj_in=bookmark_in, owner_id=user.id
    )
    description2 = random_lower_string()
    bookmark_update = BookmarkUpdate(description=description2)
    bookmark2 = crud.bookmark.update(db_session=db_session, db_obj=bookmark, obj_in=bookmark_update)
    assert bookmark.id == bookmark2.id
    assert bookmark.title == bookmark2.title
    assert bookmark2.description == description2
    assert bookmark.owner_id == bookmark2.owner_id


def test_delete_bookmark():
    title = random_lower_string()
    description = random_lower_string()
    bookmark_in = BookmarkCreate(title=title, description=description)
    user = create_random_user()
    bookmark = crud.bookmark.create_with_owner(db_session=db_session, obj_in=bookmark_in, owner_id=user.id)
    bookmark2 = crud.bookmark.remove(db_session=db_session, id=bookmark.id)
    bookmark3 = crud.bookmark.get(db_session=db_session, id=bookmark.id)
    assert bookmark3 is None
    assert bookmark2.id == bookmark.id
    assert bookmark2.title == title
    assert bookmark2.description == description
    assert bookmark2.owner_id == user.id
