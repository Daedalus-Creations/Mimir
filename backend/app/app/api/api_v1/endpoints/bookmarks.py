from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.api.utils.db import get_db
from app.api.utils.security import get_current_active_user
from app.models.user import User as DBUser
from app.schemas.bookmark import Bookmark, BookmarkCreate, BookmarkUpdate

router = APIRouter()


@router.get("/", response_model=List[Bookmark])
def read_bookmarks(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: DBUser = Depends(get_current_active_user),
):
    """
    Retrieve bookmarks.
    """
    if crud.user.is_superuser(current_user):
        bookmarks = crud.bookmark.get_multi(db, skip=skip, limit=limit)
    else:
        bookmarks = crud.bookmark.get_multi_by_owner(
            db_session=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return bookmarks


@router.post("/", response_model=Bookmark)
def create_bookmark(
    *,
    db: Session = Depends(get_db),
    bookmark_in: BookmarkCreate,
    current_user: DBUser = Depends(get_current_active_user),
):
    """
    Create new bookmark.
    """
    bookmark = crud.bookmark.create_with_owner(
        db_session=db, obj_in=bookmark_in, owner_id=current_user.id
    )
    return bookmark


@router.put("/{id}", response_model=Bookmark)
def update_bookmark(
    *,
    db: Session = Depends(get_db),
    id: int,
    bookmark_in: BookmarkUpdate,
    current_user: DBUser = Depends(get_current_active_user),
):
    """
    Update an bookmark.
    """
    bookmark = crud.bookmark.get(db_session=db, id=id)
    if not bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    if not crud.user.is_superuser(current_user) and (bookmark.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    bookmark = crud.bookmark.update(db_session=db, db_obj=bookmark, obj_in=bookmark_in)
    return bookmark


@router.get("/{id}", response_model=Bookmark)
def read_bookmark(
    *,
    db: Session = Depends(get_db),
    id: int,
    current_user: DBUser = Depends(get_current_active_user),
):
    """
    Get bookmark by ID.
    """
    bookmark = crud.bookmark.get(db_session=db, id=id)
    if not bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    if not crud.user.is_superuser(current_user) and (bookmark.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return bookmark


@router.delete("/{id}", response_model=Bookmark)
def delete_bookmark(
    *,
    db: Session = Depends(get_db),
    id: int,
    current_user: DBUser = Depends(get_current_active_user),
):
    """
    Delete an bookmark.
    """
    bookmark = crud.bookmark.get(db_session=db, id=id)
    if not bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    if not crud.user.is_superuser(current_user) and (bookmark.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    bookmark = crud.bookmark.remove(db_session=db, id=id)
    return bookmark
