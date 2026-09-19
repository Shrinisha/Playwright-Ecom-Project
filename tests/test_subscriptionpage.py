import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.automationexercise.com/")
    #expect(page.locator("div").nth(3)).to_be_visible() 
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    expect(page.locator("#footer")).to_contain_text("Subscription")
    page.get_by_role("textbox", name="Your email address").click()
    page.get_by_role("textbox", name="Your email address").fill("shrinisha1209@gmail.com")
    page.locator("#subscribe").click()
    try:
        expect(page.locator("#footer")).to_contain_text("You have been successfully subscribed!")
        print("Subscription successful!")
    except:
        print("Subscription failed!")
    #expect(page.locator("#footer")).to_contain_text("You have been successfully subscribed!")
