from sqlalchemy import Column, Integer, String
from shopgenie.database.config import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    role = Column(String)  # developer or entrepreneur

    def __repr__(self):
        return f"<User(name={self.name}, role={self.role})>"
