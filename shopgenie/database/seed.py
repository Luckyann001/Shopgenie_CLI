from shopgenie.database.config import Base, engine, session
from shopgenie.models.category import Category

def seed():
    Base.metadata.create_all(engine)

    categories = [
        "E-Commerce",
        "Portfolio",
        "Landing Page",
        "Blog Website",
        "Restaurant Website"
    ]

    for c in categories:
        exists = session.query(Category).filter_by(name=c).first()
        if not exists:
            session.add(Category(name=c))

    session.commit()
    print("Database seeded!")
