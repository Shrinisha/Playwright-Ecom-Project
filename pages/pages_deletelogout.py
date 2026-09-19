from playwright.sync_api import Page

class DeleteLogoutPage:
    def __init__(self, page: Page):
        self.page = page

    def login(self, email: str, password: str):
        self.page.goto("https://www.automationexercise.com/login")
        try:
            self.page.get_by_role("button", name="Consent").click()
        except:
            pass
        self.page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").click()
        self.page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").fill(email)
        self.page.get_by_role("textbox", name="Password").click()
        self.page.get_by_role("textbox", name="Password").fill(password)
        self.page.get_by_role("button", name="Login").click()

    def logout(self):
        self.page.get_by_role("link", name=" Logout").click()

    def delete_account(self):
        self.page.get_by_role("link", name=" Delete Account").click()
        # Handle the ad iframe if it appears
        try:
            ad_iframe = self.page.locator("iframe[name=\"aswift_3\"]")
            if ad_iframe.is_visible():
                ad_iframe.content_frame.get_by_role("button", name="Close ad").click()
        except:
            pass