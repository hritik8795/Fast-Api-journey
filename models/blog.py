from sqlalchemy import Column, Integer, String,Text,Boolean,ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    is_published = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="Blogs")