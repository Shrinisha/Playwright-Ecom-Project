from playwright.sync_api import Page, expect

class ViewProductsPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_products(self):
        self.page.goto("https://www.automationexercise.com/")
        try:
            self.page.get_by_role("button", name="Consent").click()
        except:
            pass
        self.page.get_by_role("link", name=" Products").click()

    def view_product_details(self, product_index: int):
        expect(self.page.get_by_role("heading", name="All Products")).to_be_visible()
        self.page.get_by_role("link", name=" View Product").nth(product_index).click()

    def verify_product_details(self):
        #expect(self.page.get_by_role("heading")).to_be_visible()
        expect(self.page.get_by_text("Category:")).to_be_visible()
        expect(self.page.get_by_text("Rs.")).to_be_visible()
        expect(self.page.get_by_text("Condition:")).to_be_visible()
        expect(self.page.get_by_text("Brand:")).to_be_visible()
        expect(self.page.get_by_text("Quantity:")).to_be_visible()
        category_locator = self.page.get_by_text("Category:")
        text_value = category_locator.text_content()
        print(f"\nCategory Text: {text_value}")