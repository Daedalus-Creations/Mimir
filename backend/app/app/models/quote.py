from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, LargeBinary
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models import user, quote_tag

class Quote(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    description = Column(String, index=True)
    public = Column(Boolean, nullable=False)
    owner_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    color = Column(String)

    owner = relationship("User", back_populates="quotes")
    # tags = relationship("Quote_Tag", back_populates="tag_owner")
    tags = relationship("Tag", secondary="quote_tag", back_populates="quotes")