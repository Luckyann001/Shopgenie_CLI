from shopgenie.database.config import Base, engine
from shopgenie.models.user import User
from shopgenie.models.category import Category
from shopgenie.models.template import Template


def create_all_tables():
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")

if __name__ == "__main__":
    create_all_tables()
