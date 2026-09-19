import pytest
from playwright.sync_api import APIRequestContext


def test_search_product_api(playwright) -> None:
    # 1. Create an API request context
    api_context: APIRequestContext = playwright.request.new_context()

    # 2. Send the POST request with form parameters
    response = api_context.post(
        "https://automationexercise.com/api/searchProduct",
        data={"search_product": "top"},
    )

    # 3. Assert Response Code is 200
    assert response.status == 200
    #print(f"Response Status Code: {response.status}")

    # 4. Parse the JSON response
    response_body = response.json()

    # 5. Assertions on the JSON structure & content
    assert response_body["responseCode"] == 200
    assert "products" in response_body
    assert isinstance(response_body["products"], list)
    assert len(response_body["products"]) > 0

    # Optional: Verify returned products contain the searched term
    first_product = response_body["products"][0]
    assert "top" in first_product["name"].lower()

    # Clean up context
    api_context.dispose()