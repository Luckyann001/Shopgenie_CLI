from shopgenie.database.config import session
from shopgenie.models.user import User
from shopgenie.models.category import Category
from shopgenie.models.template import Template

# Add users
u1 = User(name="Lucky", email="lucky@example.com")
u2 = User(name="Dev A", email="dev@example.com")

# Add categories
c1 = Category(name="E-commerce")
c2 = Category(name="Portfolio")
c3 = Category(name="Blog")

# Add templates
t1 = Template(name="Modern Shop", category_id=1, developer_id=2, description="Clean e-commerce")
t2 = Template(name="Personal Portfolio", category_id=2, developer_id=2, description="Simple personal brand")

session.add_all([u1, u2, c1, c2, c3, t1, t2])
session.commit()

print("Seeding completed successfully!")
