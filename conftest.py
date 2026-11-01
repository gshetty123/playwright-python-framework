
"""Shared pytest fixtures and hooks for the framework."""

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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture a screenshot when a test fails during its call phase."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page is None:
            app = item.funcargs.get("app_page")
            page = app if hasattr(app, "screenshot") else None

        if page is not None:
            screenshot_dir = Path(__file__).parent / "reports" / "screenshots"
            screenshot_dir.mkdir(parents=True, exist_ok=True)

            screenshot_path = screenshot_dir / f"{item.name}.png"
            page.screenshot(path=str(screenshot_path), full_page=True)
            print(f"\nFailure screenshot saved: {screenshot_path}")
