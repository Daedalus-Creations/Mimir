from sqlalchemy import Column, ForeignKey, Integer, String, LargeBinary
from sqlalchemy.orm import relationship, backref

from app.db.base_class import Base
from app.models import quote_tag

class Tag(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    color = Column(LargeBinary)

    parent_id = Column(Integer, ForeignKey('tag.id'))
    children = relationship("Tag",
                            backref=backref('parent', remote_side=[id])
                            )

    quotes_with_tag = relationship("Quote_Tag", back_populates="tag")
