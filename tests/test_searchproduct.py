import re
from playwright.sync_api import Page, expect
import pytest
def get_csv_data() -> list:
    import csv
    data = []
    with open("./test_data/searchproduct.csv", newline='') as csvfile:
        reader = csv.reader(csvfile) # Skip the header row
        for row in reader:
            data.append((row[0]))  # Assuming the CSV has one column: search_term
    return data
@pytest.mark.parametrize("search_term", get_csv_data())

def test_example(page: Page, search_term: str) -> None:
    page.goto("https://www.automationexercise.com/")
    try:
        page.get_by_role("button", name="Consent").click()
    except:
        pass
    #page.get_by_role("button", name="Consent").click()
    page.get_by_role("link", name=" Products").click()
    try:
        page.locator("iframe[name=\"aswift_3\"]").content_frame.get_by_role("button", name="Close ad").click()
    except:
        pass
    expect(page.get_by_role("heading", name="All Products")).to_be_visible()
    page.get_by_role("textbox", name="Search Product").click()
    page.get_by_role("textbox", name="Search Product").fill(search_term)
    page.locator("#submit_search").click()
    # Verify the "SEARCHED PRODUCTS" header appears
    expect(page.get_by_role("heading", name="Searched Products")).to_be_visible()
    # Target the product results container specifically
    features_items = page.locator(".features_items")
    # Check case-insensitively using regex
    expect(features_items).to_contain_text(re.compile(rf"{re.escape(search_term)}", re.IGNORECASE))