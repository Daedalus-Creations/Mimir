from typing import List

from fastapi import APIRouter, Depends, HTTPException
from pydantic.color import Color
from sqlalchemy.orm import Session

from app import crud
from app.api.utils.db import get_db
from app.api.utils.security import get_current_active_user
from app.models.user import User as DBUser
from app.schemas.quote import Quote, QuoteCreate, QuoteUpdate, QuoteSearch
from app.schemas.tag import Tag

router = APIRouter()


@router.get("/", response_model=List[Quote])
def read_quotes(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    anywhere: str = None,
    title: str = None,
    author: str = None,
    text: str = None,
    quote_type: str = None,
    description: str = None,
    color: Color = None,
    tag_ids: List[int] = None,
    current_user: DBUser = Depends(get_current_active_user),
):
    """
    Retrieve quotes.
    """

    tags = []
    if tag_ids:
        for each_tag in tag_ids:
            tag = crud.tag.get(db_session=db, id=each_tag)
            if not tag:
                raise HTTPException(status_code=404, detail="Tag not found")
            tags.append(tag)

    search: QuoteSearch = QuoteSearch(
        anywhere=anywhere,
        title=title,
        author=author,
        text=text,
        quote_type=quote_type,
        description=description,
        color=color.as_hex() if color else None,
        tags=tags
    )

    if crud.user.is_superuser(current_user):
        quotes = crud.quote.get_multi_by_search(
            db, search=search, skip=skip, limit=limit
        )
    else:
        quotes = crud.quote.get_multi_by_search_owner(
            db_session=db, owner_id=current_user.id, search=search, skip=skip, limit=limit
        )


    return quotes


@router.post("/", response_model=Quote)
def create_quote(
    *,
    db: Session = Depends(get_db),
    quote_in: QuoteCreate,
    current_user: DBUser = Depends(get_current_active_user),
):
    """
    Create new quote.
    """
    quote = crud.quote.create_with_owner(
        db_session=db, obj_in=quote_in, owner_id=current_user.id
    )
    return quote


@router.put("/{id}", response_model=Quote)
def update_quote(
    *,
    db: Session = Depends(get_db),
    id: int,
    quote_in: QuoteUpdate,
    current_user: DBUser = Depends(get_current_active_user),
):
    """
    Update an quote.
    """
    quote = crud.quote.get(db_session=db, id=id)
    if not quote:
        raise HTTPException(status_code=404, detail="Quote not found")
    if not crud.user.is_superuser(current_user) and (quote.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    quote = crud.quote.update(db_session=db, db_obj=quote, obj_in=quote_in)
    return quote


@router.get("/{id}", response_model=Quote)
def read_quote(
    *,
    db: Session = Depends(get_db),
    id: int,
    current_user: DBUser = Depends(get_current_active_user),
):
    """
    Get quote by ID.
    """
    quote = crud.quote.get(db_session=db, id=id)
    if not quote:
        raise HTTPException(status_code=404, detail="Quote not found")
    if not crud.user.is_superuser(current_user) and (quote.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return quote


@router.delete("/{id}", response_model=Quote)
def delete_quote(
    *,
    db: Session = Depends(get_db),
    id: int,
    current_user: DBUser = Depends(get_current_active_user),
):
    """
    Delete an quote.
    """
    quote = crud.quote.get(db_session=db, id=id)
    if not quote:
        raise HTTPException(status_code=404, detail="Quote not found")
    if not crud.user.is_superuser(current_user) and (quote.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    quote = crud.quote.remove(db_session=db, id=id)
    return quote
