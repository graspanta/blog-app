from datetime import datetime

from sqlalchemy import ForeignKey  # noqa: E501
from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text
from sqlalchemy.orm import relationship

from backend.db.base_class import Base


class Blog(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String(60), nullable=False)
    content = Column(Text, nullable=True)
    author_id = Column(Integer, ForeignKey("user.id"))
    author = relationship("User", back_populates="blogs")
    created_at = Column(DateTime(timezone=True), default=datetime.now)
    is_active = Column(Boolean, default=False)
