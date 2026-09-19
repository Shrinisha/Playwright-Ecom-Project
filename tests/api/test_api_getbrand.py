def test_api_getpost(playwright):
        request = playwright.request.new_context()
        response2=request.get("https://automationexercise.com/api/brandsList")
        assert response2.status==200
        json_data1=response2.json()
        print(json_data1)
        print("Test completed successfully")