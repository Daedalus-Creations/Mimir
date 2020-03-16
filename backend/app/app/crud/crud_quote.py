from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy import or_
from sqlalchemy.orm import Session, Query

from app.models.quote import Quote
from app.schemas.quote import QuoteCreate, QuoteUpdate, QuoteSearch
from app.crud.base import CRUDBase
from app.models.tag import Tag
from app.crud.crud_tag import tag as crud_tag
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_multi_by_tag(quotes: List[Quote], tags: List[Tag]):
    matching_quotes: List[Quote] = []
    for quote in quotes:
        if not set(quote.tags).isdisjoint(
                tags):  # https://stackoverflow.com/questions/3170055/test-if-lists-share-any-items-in-python
            logger.info("TRUE")
            logger.info(quote)
            matching_quotes.append(quote)
    return matching_quotes

def search_query(quotes: Query, search: QuoteSearch, skip=0, limit=100):
    anywhere = search.anywhere
    title = search.title
    text = search.text
    quote_type = search.quote_type
    description = search.description
    author = search.author
    # public = search.public
    color = search.color
    tags = search.tags

    if title:
        quotes = quotes.filter(Quote.title.ilike(title))
    if text:
        quotes = quotes.filter(Quote.text.ilike(text))
    if quote_type:
        quotes = quotes.filter(Quote.type == quote_type)
    if description:
        quotes = quotes.filter(Quote.description.ilike(description))
    if author:
        quotes = quotes.filter(Quote.author.ilike(author))
    if color:
        quotes = quotes.filter(Quote.color == color.as_hex())

    if anywhere:
        logger.info("ANYWHERE called")
        quotes = quotes.filter(
            or_(Quote.title.ilike(anywhere),
                Quote.text.ilike(anywhere),
                Quote.description.ilike(anywhere),
                Quote.author.ilike(author))
        )
    quotes = quotes.offset(skip).limit(limit).all()

    if tags:
        return get_multi_by_tag(quotes, tags)
    else:
        return quotes

class CRUDQuote(CRUDBase[Quote, QuoteCreate, QuoteUpdate]):
    def create_with_owner(
            self, db_session: Session, *, obj_in: QuoteCreate, owner_id: int
    ) -> Quote:
        tags = [crud_tag.get(db_session, tag.id) for tag in obj_in.tags]
        logger.info(tags)
        color = obj_in.color.as_hex() if obj_in.color else None
        db_obj = self.model(title=obj_in.title,
                            text=obj_in.text,
                            type=obj_in.type,
                            author=obj_in.author,
                            description=obj_in.description,
                            public=obj_in.public,
                            owner_id=owner_id,
                            color=color,
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
        return get_multi_by_tag(quotes, tags)
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
    def get_multi_by_search_owner(
            self, db_session: Session, *, owner_id: int, search: QuoteSearch, skip=0, limit=100
    ):

        quotes = db_session.query(self.model).filter(Quote.owner_id == owner_id)

        return search_query(quotes, search, skip, limit)

    def get_multi_by_search(
            self, db_session: Session, *, search: QuoteSearch, skip=0, limit=100
    ):
        logger.info("GET MULTI BY SEARCH")
        quotes = db_session.query(self.model)


        return search_query(quotes, search, skip, limit)

    def update(
        self, db_session: Session, *, db_obj: Quote, obj_in: QuoteUpdate
    ) -> Quote:
        obj_data = jsonable_encoder(db_obj)
        update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                if field == "color":
                    setattr(db_obj, field, update_data[field].as_hex())
                else:
                    setattr(db_obj, field, update_data[field])


        db_session.add(db_obj)
        db_session.commit()
        db_session.refresh(db_obj)

        # tags = [crud_tag.get(db_session, tag.id) for tag in obj_in.tags]
        # logger.info(tags)
        # color = obj_in.color.as_hex() if obj_in.color else None
        # db_obj = self.model(title=obj_in.title,
        #                     text=obj_in.text,
        #                     type=obj_in.type,
        #                     description=obj_in.description,
        #                     public=obj_in.public,
        #                     owner_id=owner_id,
        #                     color=color,
        #                     tags=tags)
        # db_session.add(db_obj)
        # db_session.commit()
        # db_session.refresh(db_obj)

        return db_obj

quote = CRUDQuote(Quote)
