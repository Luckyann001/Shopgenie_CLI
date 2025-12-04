from shopgenie.database.config import session
from shopgenie.models.user import User

class UserService:

    @staticmethod
    def create_user(name, role):
        user = User(name=name, role=role)
        session.add(user)
        session.commit()
        return user

    @staticmethod
    def list_users():
        return session.query(User).all()
