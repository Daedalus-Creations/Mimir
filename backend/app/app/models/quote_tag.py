from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models import quote, tag

# class Quote_Tag(Base):
#     quote_id = Column(Integer, ForeignKey("quote.id"), nullable=False, primary_key=True)
#     tag_id = Column(Integer, ForeignKey("tag.id"), nullable=False, primary_key=True)
#
#     tag_owner = relationship("Quote", back_populates="tags")
#     tag = relationship("Tag", back_populates="quotes_with_tag")

quote_tag = Table('quote_tag', Base.metadata,
                  Column('quote_id', ForeignKey('quote.id'), primary_key=True),
                  Column('tag_id', ForeignKey('tag.id'), primary_key=True)
                  )
