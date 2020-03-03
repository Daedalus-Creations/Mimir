from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.models.quote import Quote
from app.schemas.quote import QuoteCreate, QuoteUpdate
from app.crud.base import CRUDBase


class CRUDQuote(CRUDBase[Quote, QuoteCreate, QuoteUpdate]):
    def create_with_owner(
        self, db_session: Session, *, obj_in: QuoteCreate, owner_id: int
    ) -> Quote:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db_session.add(db_obj)
        db_session.commit()
        db_session.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db_session: Session, *, owner_id: int, skip=0, limit=100
    ) -> List[Quote]:
        return (
            db_session.query(self.model)
            .filter(Quote.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


quote = CRUDQuote(Quote)
