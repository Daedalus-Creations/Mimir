from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.models.tag import Tag
from app.schemas.tag import TagCreate, TagUpdate
from app.crud.base import CRUDBase

class CRUDTag(CRUDBase[Tag, TagCreate, TagUpdate]):
    def create_with_owner(
            self, db_session: Session, *, obj_in: TagCreate, owner_id: int
    ) -> Tag:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db_session.add(db_obj)
        db_session.commit()
        db_session.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
            self, db_session: Session, *, owner_id: int, skip=0, limit=100
    ) -> List[Tag]:
        return (
            db_session.query(self.model)
                .filter(Tag.owner_id == owner_id)
                .offset(skip)
                .limit(limit)
                .all()
        )

    def get_multi_by_tag_owner(
            self, db_session: Session, *, owner_id: int, tag_ids: List[int], skip=0, limit=100
    ) -> List[Tag]:
        return (
            db_session.query(self.model)
                .filter(Tag.owner_id == owner_id)
                .filter(
                or_(
                    *[Tag.tags_for_tag.any(tag) for tag in tag_ids]
                )
            )
                .offset(skip)
                .limit(limit)
                .all()
        )


tag = CRUDTag(Tag)
