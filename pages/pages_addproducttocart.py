from playwright.sync_api import Page, expect

class AddProductToCartPage:
    def __init__(self, page: Page):
        self.page = page
        

    def add_product_to_cart(self, product_index: int):
        expect(self.page.get_by_role("heading", name="All Products")).to_be_visible()
        self.page.get_by_role("link", name=" View Product").nth(product_index).click()
        self.page.get_by_role("button", name=" Add to cart").click()

    def verify_product_added(self):
        expect(self.page.get_by_role("heading", name="Added!")).to_be_visible()
        expect(self.page.get_by_text("Your product has been added")).to_be_visible()
    
    def navigate_to_cart(self):
        self.page.get_by_role("link", name="View Cart").click()
        expect(self.page.get_by_text("Home Shopping Cart")).to_be_visible()
        expect(self.page.locator("#product-1").get_by_role("cell", name="Product Image")).to_be_visible()
        expect(self.page.locator("#product-2").get_by_role("cell", name="Product Image")).to_be_visible()
        expect(self.page.get_by_role("cell", name="Total")).to_be_visible()
        expect(self.page.get_by_role("cell", name="Quantity")).to_be_visible()
        expect(self.page.get_by_role("cell", name="Price")).to_be_visible()
        expect(self.page.get_by_role("cell", name="Description")).to_be_visible()
        expect(self.page.get_by_role("cell", name="Item")).to_be_visible()
    
    def verify_product_in_cart(self, product_name: str):
        self.page.goto("https://www.automationexercise.com/view_cart")
        value_page_cart_name=self.page.get_by_role("link", name=product_name).inner_text()
       # value_page_cart_price=self.page.get_by_role("cell", name="Rs").inner_text()
        #value_page_cart_quantity=self.page.get_by_role("cell", name="1").inner_text()
        print(value_page_cart_name)
        #print(value_page_cart_price)
        #print(value_page_cart_quantity)
        self.page.goto("https://www.automationexercise.com/product_details/1")
        value_page_product_name = self.page.get_by_role("heading").inner_text()
        #value_page_product_price = self.page.get_by_role("heading", name="Price").inner_text()
        #value_page_product_quantity = self.page.locator("#quantity").inner_text()
        print(value_page_product_name)
       # print(value_page_product_price)
        #print(value_page_product_quantity)
        assert value_page_cart_name == value_page_product_name
        #assert value_page_cart_price == value_page_product_price
        #assert value_page_cart_quantity == value_page_product_quantity
    