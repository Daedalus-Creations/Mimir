from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.models.quote import Quote
from app.schemas.quote import QuoteCreate, QuoteUpdate
from app.crud.base import CRUDBase
from app.models.tag import Tag
from app.crud.crud_tag import tag as crud_tag
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CRUDQuote(CRUDBase[Quote, QuoteCreate, QuoteUpdate]):
    def create_with_owner(
            self, db_session: Session, *, obj_in: QuoteCreate, owner_id: int
    ) -> Quote:
        tags = [crud_tag.get(db_session, tag.id) for tag in obj_in.tags]
        logger.info(tags)
        db_obj = self.model(title=obj_in.title,
                            description=obj_in.description,
                            public=obj_in.public,
                            owner_id=owner_id,
                            color=jsonable_encoder(obj_in.color),
                            tags=tags)
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

    def get_multi_by_tag_owner(
            self, db_session: Session, *, owner_id: int, tags: List[Tag], skip=0, limit=100
    ) -> List[Quote]:
        quotes = db_session.query(self.model).filter(Quote.owner_id == owner_id).all()
        matching_quotes: List[Quote] = []
        for quote in quotes:
            if not set(quote.tags).isdisjoint(tags): #https://stackoverflow.com/questions/3170055/test-if-lists-share-any-items-in-python
                logger.info("TRUE")
                logger.info(quote)
                matching_quotes.append(quote)
        return matching_quotes
        # return (
        #     db_session.query(self.model)
        #         .filter(Quote.owner_id == owner_id)
        #         .filter(
        #         or_(
        #             *[Quote.tags.any(tag) for tag in tags]
        #         )
        #     )
        #         .offset(skip)
        #         .limit(limit)
        #         .all()
        # )


quote = CRUDQuote(Quote)
