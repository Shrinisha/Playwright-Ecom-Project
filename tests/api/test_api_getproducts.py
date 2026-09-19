def test_api_get(playwright):
    request = playwright.request.new_context()
    response1=request.get("https://automationexercise.com/api/productsList")
    assert response1.status==200
    json_data=response1.json()
    print(json_data)
    print("Test completed successfully")
    