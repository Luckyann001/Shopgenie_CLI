import pytest
from shopgenie.services.user_service import UserService
from shopgenie.services.category_service import CategoryService
from shopgenie.services.template_service import TemplateService
from shopgenie.database.config import Base, engine, session
from shopgenie.models.category import Category

@pytest.fixture(scope="module", autouse=True)
def setup_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    # Seed categories
    session.add(Category(name="Portfolio"))
    session.add(Category(name="Landing Page"))
    session.commit()

    yield
    Base.metadata.drop_all(engine)

def test_create_user_service():
    user = UserService.create_user("Diana", "developer")
    assert user.name == "Diana"
    assert user.role == "developer"

def test_list_users_service():
    users = UserService.list_users()
    assert len(users) >= 1

def test_generate_ai_template():
    content = TemplateService.generate_from_prompt("ecommerce site")
    assert "ecommerce site" in content

def test_create_template_service():
    user = UserService.create_user("Elvis", "developer")
    cat = session.query(Category).filter_by(name="Portfolio").first()

    template = TemplateService.create_template(
        name="Portfolio A",
        content="<html></html>",
        category_id=cat.id,
        user_id=user.id
    )

    assert template.category.name == "Portfolio"
    assert template.user.name == "Elvis"
