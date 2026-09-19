import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.automationexercise.com/")
    try:
        page.get_by_role("button", name="Consent").click()
    except:
        pass
    page.get_by_role("link", name=" Products").click()
    #page.locator("iframe[name=\"aswift_3\"]").content_frame.get_by_role("button", name="Close ad").click()
    page.get_by_role("link", name=" View Product").first.click()
    page.get_by_role("button", name=" Add to cart").click()
    page.get_by_role("button", name="Continue Shopping").click()
    page.get_by_role("link", name=" Products").click()
    page.get_by_role("link", name=" View Product").nth(1).click()
    page.get_by_role("button", name=" Add to cart").click()
    page.get_by_role("button", name="Continue Shopping").click()
    page.get_by_role("link", name=" Cart").click()
    expect(page.get_by_role("heading", name="Blue Top")).to_be_visible()
    expect(page.get_by_role("cell", name="Rs.").nth(1)).to_be_visible()
    page.locator(".cart_quantity_delete").first.click()
    expect(page.get_by_role("heading", name="Blue Top")).not_to_be_visible()
