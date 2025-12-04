from shopgenie.database.config import session
from shopgenie.models.category import Category

class CategoryService:

    @staticmethod
    def get_all():
        return session.query(Category).all()
