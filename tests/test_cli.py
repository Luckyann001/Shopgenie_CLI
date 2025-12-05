import pytest
from click.testing import CliRunner
from shopgenie.cli.command import start
from shopgenie.database.config import Base, engine

@pytest.fixture(scope="module", autouse=True)
def setup_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)

def test_cli_register_user(monkeypatch):
    runner = CliRunner()

    # Simulate user input:
    # 1. Register
    # name: John
    # role: developer
    # 5. Exit
    inputs = "1\nJohn\ndeveloper\n5\n"

    result = runner.invoke(start, input=inputs)

    assert "User created!" in result.output

def test_cli_generate_template(monkeypatch):
    runner = CliRunner()

    inputs = "3\nsimple blog layout\n5\n"

    result = runner.invoke(start, input=inputs)

    assert "AI-Generated Layout for: simple blog layout" in result.output
