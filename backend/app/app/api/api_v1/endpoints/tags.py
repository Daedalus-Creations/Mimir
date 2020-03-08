from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.api.utils.db import get_db
from app.api.utils.security import get_current_active_user
from app.models.user import User as DBUser
from app.schemas.tag import Tag, TagCreate, TagUpdate

router = APIRouter()


@router.get("/", response_model=List[Tag])
def read_tags(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: DBUser = Depends(get_current_active_user),
):
    """
    Retrieve tags.
    """
    if crud.user.is_superuser(current_user):
        tags = crud.tag.get_multi(db, skip=skip, limit=limit)
    else:
        tags = crud.tag.get_multi_by_owner(
            db_session=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return tags


@router.post("/", response_model=Tag)
def create_tag(
    *,
    db: Session = Depends(get_db),
    tag_in: TagCreate,
    current_user: DBUser = Depends(get_current_active_user),
):
    """
    Create new tag.
    """
    tag = crud.tag.create_with_owner(
        db_session=db, obj_in=tag_in, owner_id=current_user.id
    )
    return tag


@router.put("/{id}", response_model=Tag)
def update_tag(
    *,
    db: Session = Depends(get_db),
    id: int,
    tag_in: TagUpdate,
    current_user: DBUser = Depends(get_current_active_user),
):
    """
    Update an tag.
    """
    tag = crud.tag.get(db_session=db, id=id)
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    if not crud.user.is_superuser(current_user) and (tag.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    tag = crud.tag.update(db_session=db, db_obj=tag, obj_in=tag_in)
    return tag


@router.get("/{id}", response_model=Tag)
def read_tag(
    *,
    db: Session = Depends(get_db),
    id: int,
    current_user: DBUser = Depends(get_current_active_user),
):
    """
    Get tag by ID.
    """
    tag = crud.tag.get(db_session=db, id=id)
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    if not crud.user.is_superuser(current_user) and (tag.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return tag


@router.delete("/{id}", response_model=Tag)
def delete_tag(
    *,
    db: Session = Depends(get_db),
    id: int,
    current_user: DBUser = Depends(get_current_active_user),
):
    """
    Delete an tag.
    """
    tag = crud.tag.get(db_session=db, id=id)
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    if not crud.user.is_superuser(current_user) and (tag.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    tag = crud.tag.remove(db_session=db, id=id)
    return tag
