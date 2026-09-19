import re

import pytest
from pages.pages_viewproducts import ViewProductsPage
from playwright.sync_api import Page, expect
def get_csv_data() -> list:
    import csv
    data = []
    with open("./test_data/viewproducts.csv", newline='') as csvfile:
        reader = csv.reader(csvfile) # Skip the header row
        for row in reader:
            data.append((int(row[0])))  # Assuming the CSV has two columns: username and password
    return data
@pytest.mark.parametrize("no", get_csv_data())

def test_example(page: Page, no: int) -> None:
    view_products_page = ViewProductsPage(page)
    view_products_page.navigate_to_products()
    #page.locator("iframe[name=\"aswift_3\"]").content_frame.get_by_role("button", name="Close ad").click()
    view_products_page.view_product_details(no)
    view_products_page.verify_product_details()
