ShopGenie CLI

A Python-based command-line interface (CLI) that allows developers to manage users, categories, and AI-generated templates for an automated website-building platform.

This project demonstrates OOP, SQLAlchemy ORM, database relationships, modular architecture, and clean CLI design — fulfilling all Phase 3 requirements.

 Table of Contents

Overview

Problem Statement

Solution

Features

Tech Stack

Project Structure

Database Schema

Installation

How to Run the CLI

Demo Workflow

Tests

Future Improvements

Author

Overview

ShopGenie CLI is the developer tool for a larger system called ShopGenie, an AI-powered platform that generates website templates for entrepreneurs.

This CLI simulates how developers interact with the backend to:

Register users

Assign categories

Generate AI templates

View stored templates

It is built using clean modular architecture and persistent storage through SQLAlchemy with SQLite.

 Problem Statement

Developers need a lightweight backend management system where they can:

Register clients

Organize template categories

Generate templates

Store them securely

Retrieve them easily

Entrepreneurs often struggle building websites manually — they need reliable tools that work even behind the scenes.

 Solution

ShopGenie CLI provides a simple but scalable backend workflow:

A developer-friendly CLI to manage the system

A relational database with three important models

Auto-generated templates using placeholder AI logic

Services that handle business logic

Clear separation of concerns (CLI → Services → Models → DB)

This simulates the real workflow that future ShopGenie developers will use.

 Features
 User Management

Register new users

List registered users

 Category Management

Auto-creates categories when generating templates

 Template Management

Generate “AI-powered” templates

Store template metadata in the database

List all templates

 SQLite Database

Stores all users, categories, and templates

Managed through SQLAlchemy ORM

 Clean Architecture

models

services

database

cli

utils

 Tech Stack
Component	Technology
Language	Python 3
Database	SQLite
ORM	SQLAlchemy
CLI	Native Python + input()
Testing	pytest
Environment	pipenv
 Project Structure
shopgenie/
│── Pipfile
│── README.md
│── shopgenie/
│   ├── cli/
│   │   ├── main.py
│   │   └── commands.py
│   ├── database/
│   │   ├── config.py
│   │   ├── create_tables.py
│   │   └── seed.py
│   ├── models/
│   │   ├── user.py
│   │   ├── category.py
│   │   └── template.py
│   ├── services/
│   │   ├── user_service.py
│   │   ├── category_service.py
│   │   └── template_service.py
│   └── utils/
│       └── formatters.py
│── tests/
│   ├── test_models.py
│   ├── test_services.py
│   └── test_cli.py

Database Schema
Users Table
Column	Type	Notes
id	Integer	Primary Key
username	String	Unique
Categories Table
Column	Type
id	Integer
name	String
Templates Table
Column	Type	Notes
id	Integer	Primary Key
name	String	
user_id	Integer	ForeignKey → users.id
category_id	Integer	ForeignKey → categories.id
 Installation
1. Clone the repository
git clone <your-repo-url>
cd Shopgenie_CLI

2. Install dependencies
pipenv install
pipenv shell

3. Create the database tables
python3 -m shopgenie.database.create_tables

▶ How to Run the CLI
python3 -m shopgenie.cli.main


You will see:

ShopGenie CLI
---------------------------------------------
1. Register User
2. List Users
3. Generate Template (AI)
4. List Templates
5. Exit

Tests

Run tests using pytest:

pytest


Tests include:

Model tests

Service tests

CLI tests

 Demo Workflow

Start the CLI

Register a user

Generate a template for that user

List templates

Exit

 Future Improvements

Real AI template generation

JSON export of templates

API version (Python Flask/FastAPI)

Authentication for developers

Entrepreneur web dashboard

Author

 Name: Luckyann Kagendo
Phase 3 Python Student
ShopGenie Founder