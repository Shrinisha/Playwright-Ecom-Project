def test_api_getpost(playwright):
    request = playwright.request.new_context()
    response1=request.post("https://automationexercise.com/api/brandsList")
    assert response1.status==200
    json_data=response1.json()
    print(json_data)
    assert json_data["responseCode"]==405
    assert json_data["message"]=="This request method is not supported."
    print("Test completed successfully")
    