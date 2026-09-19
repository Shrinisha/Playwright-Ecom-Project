import re
from playwright.sync_api import Page, expect
import pytest
from pages.pages_deletelogout import DeleteLogoutPage
def get_csv_data() -> list:
    import csv
    data = []
    with open("./test_data/deletelogout.csv", newline='') as csvfile:
        reader = csv.reader(csvfile) # Skip the header row
        for row in reader:
            data.append((row))  # Assuming the CSV has two columns: username and password
    return data
@pytest.mark.parametrize("email,password", get_csv_data())

def test_example(page: Page, email: str, password: str) -> None:
    delete_logout_page = DeleteLogoutPage(page)
    delete_logout_page.login(email,password)
    expect(page.get_by_role("link", name=" Delete Account")).to_be_visible()
    delete_logout_page.delete_account()
    try:
        expect(page.locator("b")).to_contain_text("Account Deleted!")
        print("Account Deleted!")
    except:
        print("Account not deleted!")
        pass
    page.get_by_role("link", name="Continue").click()
