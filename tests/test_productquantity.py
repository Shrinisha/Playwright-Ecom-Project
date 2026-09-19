import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.automationexercise.com/")
    page.get_by_role("link", name=" Products").click()
    expect(page.get_by_role("heading", name="All Products")).to_be_visible()
    page.get_by_role("link", name=" View Product").first.click()
    expect(page.get_by_text("Blue Top Category: Women >")).to_be_visible()
    expect(page.locator("section")).to_contain_text("Blue Top")
    page.locator("#quantity").fill("4")
    page.get_by_role("button", name=" Add to cart").click()
    page.get_by_role("link", name="View Cart").click()
    cart_row = page.locator("#product-1")
    expect(cart_row.locator(".cart_quantity")).to_have_text("4")
    #expect(page.locator("#product-1")).to_contain_text("4")
    #expect(page.get_by_role("cell", name="4")).to_be_visible()
    print(cart_row.locator(".cart_quantity").text_content())
