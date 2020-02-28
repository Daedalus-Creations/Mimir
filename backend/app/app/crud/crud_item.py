from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.models.bookmark import Bookmark
from app.schemas.bookmark import BookmarkCreate, BookmarkUpdate
from app.crud.base import CRUDBase


class CRUDBookmark(CRUDBase[Bookmark, BookmarkCreate, BookmarkUpdate]):
    def create_with_owner(
        self, db_session: Session, *, obj_in: BookmarkCreate, owner_id: int
    ) -> Bookmark:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db_session.add(db_obj)
        db_session.commit()
        db_session.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db_session: Session, *, owner_id: int, skip=0, limit=100
    ) -> List[Bookmark]:
        return (
            db_session.query(self.model)
            .filter(Bookmark.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


bookmark = CRUDBookmark(Bookmark)
