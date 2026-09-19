import re
from pathlib import Path
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.automationexercise.com/")
    try:
        page.get_by_role("button", name="Consent").click()
    except:
        pass
    #page.get_by_role("button", name="Consent").click()
    page.get_by_role("link", name=" Contact us").click()
    page.get_by_role("textbox", name="Name").click()
    page.get_by_role("textbox", name="Name").fill("shrinisha")
    page.get_by_role("textbox", name="Email", exact=True).click()
    page.get_by_role("textbox", name="Email", exact=True).fill("shi@gmail.com")
    page.get_by_role("textbox", name="Subject").click()
    page.get_by_role("textbox", name="Subject").fill("demo")
    page.get_by_role("textbox", name="Your Message Here").click()
    page.get_by_role("textbox", name="Your Message Here").fill("contact us")
    page.keyboard.press("PageDown")
    file_path = Path(r"C:\Users\Vishnu Ram T K\Desktop\demo.txt")
    page.locator("input[type='file']").set_input_files(file_path)
    page.get_by_role("button", name="Submit").click()
    
    try:
      page.once("dialog", lambda dialog: dialog.dismiss())
      print("Alert dismissed successfully.")
    except:
        pass
    try:
        page.get_by_role("button", name="Submit").click(force=True)
        print("Submit button clicked successfully.")
    except:
        print("Submit button not found")
    expect(page.locator("#contact-page")).to_contain_text("Success! Your details have been submitted successfully.")
    expect(page.get_by_role("heading", name="Get In Touch")).to_be_visible()
    page.get_by_role("link", name=" Home").click()
    try:
        page.locator("iframe[name=\"aswift_2\"]").content_frame.get_by_role("button", name="Close ad").click()
    except:
        pass
    expect(page.get_by_text("AutomationExercise Full-").first).to_be_visible()
    page.close()
  