import re
import pytest
from playwright.sync_api import Page, expect
def get_csv_data() -> list:
    import csv
    data = []
    with open("./test_data/login.csv", newline='') as csvfile:
        reader = csv.reader(csvfile) # Skip the header row
        for row in reader:
            data.append((row))  # Assuming the CSV has two columns: username and password
    return data
@pytest.mark.parametrize("username,password", get_csv_data())
def test_example(page: Page, username,password) -> None:
    page.goto("https://automationexercise.com/")
    try:
        page.get_by_role("button", name="Consent").click()
    except:
        pass
    page.get_by_role("link", name=" Signup / Login").click()
    expect(page.get_by_role("heading", name="Login to your account")).to_be_visible()
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").click()
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").fill(username)
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill(password)
    try:
        page.get_by_role("button", name="Login").click()
        expect(page.locator("b")).to_contain_text("Shrinisha")
        print("Login successful!")
        #page.get_by_role("link", name=" Logout").click()
        try:
                page.get_by_role("link", name=" Logout").click()
                expect(page.get_by_role("heading", name="Login to your account")).to_be_visible()
                print("Logout successful!")
        except:
                print("Logout failed!")
    except:
        expect(page.locator("#form")).to_contain_text("Your email or password is incorrect!")
        print("Login failed!")
    
    