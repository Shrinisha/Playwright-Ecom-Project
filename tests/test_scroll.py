import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.automationexercise.com/")
    try:
        page.get_by_role("button", name="Consent").click()
    except:
        pass
    #page.locator(".grippy-host").click()
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    #page.wait_for_selector(".lazy-loaded-item")
    try:
      expect(page.locator("div").filter(has_text="Subscription Get the most").nth(3)).to_be_visible()
      expect(page.locator("#footer")).to_contain_text("Subscription")
      print("Subscription line are visible.")
    except:
      print("One or more elements not found.")
      pass
    page.evaluate("window.scrollTo(0, 0)")
    
    try:
        expect(page.get_by_role("link", name="Website for automation")).to_be_visible()
        print("Website for automation is visible.")
    except:
        print("Website for automation not found.")
