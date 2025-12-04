from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from shopgenie.database.config import Base

class Template(Base):
    __tablename__ = "templates"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    content = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    category = relationship("Category")
    user = relationship("User")

    def __repr__(self):
        return f"<Template(name={self.name}, category={self.category.name})>"
