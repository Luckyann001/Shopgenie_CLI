from sqlalchemy import Column, Integer, String
from shopgenie.database.config import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    def __repr__(self):
        return f"<Category(name={self.name})>"
