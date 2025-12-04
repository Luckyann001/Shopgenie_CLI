import pytest
from shopgenie.database.config import Base, engine, session
from shopgenie.models.user import User
from shopgenie.models.category import Category
from shopgenie.models.template import Template

@pytest.fixture(scope="module", autouse=True)
def setup_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)

def test_user_model():
    user = User(name="Alice", role="developer")
    session.add(user)
    session.commit()

    saved = session.query(User).filter_by(name="Alice").first()
    assert saved.role == "developer"

def test_category_model():
    cat = Category(name="Portfolio")
    session.add(cat)
    session.commit()

    saved = session.query(Category).filter_by(name="Portfolio").first()
    assert saved.name == "Portfolio"

def test_template_relationship():
    user = User(name="Bob", role="developer")
    cat = Category(name="E-commerce")
    session.add_all([user, cat])
    session.commit()

    template = Template(
        name="Test Template",
        content="<html></html>",
        user_id=user.id,
        category_id=cat.id
    )
    session.add(template)
    session.commit()

    saved = session.query(Template).first()
    assert saved.user.name == "Bob"
    assert saved.category.name == "E-commerce"
