"""Page object for the inventory page shown after login."""

from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class HomePage(BasePage):
    page_title = "[data-test='title']"
    inventory_list = "[data-test='inventory-list']"
    inventory_items = "[data-test='inventory-item']"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def expect_loaded(self) -> None:
        expect(self.page.locator(self.page_title)).to_have_text("Products")
        expect(self.page.locator(self.inventory_list)).to_be_visible()

    def expect_page_title(self, title: str) -> None:
        expect(self.page.locator(self.page_title)).to_have_text(title)

    def expect_products_visible(self) -> None:
        expect(self.page.locator(self.inventory_items).first).to_be_visible()
