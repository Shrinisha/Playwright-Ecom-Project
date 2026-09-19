
import pytest


def test_api_postsearch(playwright):
    request = playwright.request.new_context()
    response1=request.post("https://automationexercise.com/api/searchProduct")
    @pytest.mark.parametrize("search_term, expected_code", [
    ("top", 200),
    ("tshirt", 200),
    ("jean", 200),
])
    def test_search_product(search_term, expected_code):
        response1=request.post("https://automationexercise.com/api/searchProduct", json={"search_product": search_term})
        assert response1.status==expected_code
        json_data=response1.json()
        print(json_data)
        print("Test completed successfully")