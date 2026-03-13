class LoginPage:

    def __init__(self,page):
        self.page = page

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")
    def login(self,userEmail,userPassword):
        self.page.get_by_placeholder("email@example.com").fill(userEmail)
        self.page.locator("#userPassword").type(userPassword)
        self.page.get_by_text("Login").click()


