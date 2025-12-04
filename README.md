# ShopGenie CLI – MVP

ShopGenie CLI is a lightweight command-line tool for generating and managing website templates for developers. It includes user registration, categories, templates, and a simple AI prompt-based generation system.

This MVP demonstrates:
- Python fundamentals
- OOP
- SQLAlchemy ORM
- 3 related tables (User, Category, Template)
- CLI using Click
- Lists & dicts
- Clean project structure

## Features
- Register & manage users
- Create categories (e.g., eCommerce, Portfolio)
- Add templates linked to categories
- Browse generated templates
- AI-style "prompt → template" generator (simple logic)
- Fully interactive CLI menu

## Run the App
pipenv install
pipenv shell
python -m shopgenie.cli.main

markdown
Copy code

## Database
SQLite database using SQLAlchemy ORM.

Tables:
- users
- categories
- templates

## Future Expansion
This CLI will evolve into the developer backend for ShopGenie SaaS.
