"""Thin aliases around pytest-playwright's built-in page fixture."""

import pytest
from playwright.sync_api import Page


@pytest.fixture
def app_page(page: Page) -> Page:
    """Use pytest-playwright's managed page without duplicating browser setup."""
    return page
