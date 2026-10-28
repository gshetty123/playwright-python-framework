"""Shared pytest fixtures for the framework."""

import json
from pathlib import Path

import pytest

from fixtures.browser_fixtures import app_page


@pytest.fixture
def test_users() -> dict:
    """Load sample users from JSON so tests do not hard-code credentials."""
    users_file = Path(__file__).parent / "test_data" / "users.json"
    try:
        with users_file.open(encoding="utf-8") as file:
            return json.load(file)
    except (OSError, json.JSONDecodeError) as error:
        pytest.fail(f"Could not load test users from {users_file}: {error}")
