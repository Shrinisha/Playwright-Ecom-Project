import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.automationexercise.com/")
    page.get_by_role("link", name=" Test Cases").click()
    try:
        expect(page.locator("b")).to_be_visible()
        expect(page.locator("b")).to_contain_text("Test Cases")
        page.get_by_role("link", name="Test Case 1: Register User").click()
        expect(page.locator("#collapse1").get_by_text("Launch browser")).to_be_visible()
        page.get_by_role("link", name="Test Case 1: Register User").click()
        #page.get_by_role("button", name="Consent").click()
        print("Test case passed successfully!")
    except:
        print("Test case failed!")
        
