from sqlalchemy import Column, ForeignKey, Integer, String, LargeBinary, Boolean
from sqlalchemy.orm import relationship, backref

from app.db.base_class import Base
from app.models import quote_tag, user

class Tag(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    color = Column(String)
    public = Column(Boolean, nullable=False)
    owner_id = Column(Integer, ForeignKey('user.id'))

    parent_id = Column(Integer, ForeignKey('tag.id'))
    children = relationship("Tag",
                            backref=backref('parent', remote_side=[id])
                            )

    # quotes_with_tag = relationship("Quote_Tag", back_populates="tag")
    owner = relationship("User", back_populates="tags")
    quotes = relationship("Quote", secondary="quote_tag", back_populates="tags")
