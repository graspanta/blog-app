from backend.db.base_class import Base
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(254), nullable=False, unique=True, index=True)
    password = Column(String(60), nullable=False)
    is_superuser = Column(Boolean(), default=False)
    is_active = Column(Boolean(), default=True)
    blogs = relationship("Blog", back_populates="author")