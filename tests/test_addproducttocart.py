import re
from playwright.sync_api import Page, expect
from pages.pages_viewproducts import ViewProductsPage
from pages.pages_addproducttocart import AddProductToCartPage


def test_example(page: Page) -> None:
    view_products_page = ViewProductsPage(page)
    add_to_cart_page = AddProductToCartPage(page)

    view_products_page.navigate_to_products()
    add_to_cart_page.add_product_to_cart(0)
    add_to_cart_page.verify_product_added()
    #expect(page.get_by_role("heading", name="Added!")).to_be_visible()
    #expect(page.get_by_text("Your product has been added")).to_be_visible()
    page.get_by_role("button", name="Continue Shopping").click()
    page.get_by_role("link", name=" Products").click()
    add_to_cart_page.add_product_to_cart(1)
    #page.locator("div:nth-child(6) > .product-image-wrapper > .single-products > .product-overlay > .overlay-content > .btn").click()
    add_to_cart_page.navigate_to_cart()
   # add_to_cart_page.verify_product_in_cart("Blue Top")
