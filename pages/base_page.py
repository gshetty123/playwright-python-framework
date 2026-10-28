"""Shared page actions used by page objects."""

from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def open(self, url: str) -> None:
        """Navigate to a URL and wait for the document to be ready."""
        self.page.goto(url, wait_until="domcontentloaded")
