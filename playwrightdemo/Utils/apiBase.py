from playwright.sync_api import Playwright

class ApiBase:

    base_url = "https://rahulshettyacademy.com/"
    Create_url = "api/ecom/order/create-order"
    Create_payload = {"orders": [{"country": "India", "productOrderedId": "6960eac0c941646b7a8b3e68"}]}
    login_url = "api/ecom/auth/login"


    def token(self,playwright:Playwright,user_credentials):
        userEmail = user_credentials['userEmail']
        userPassword = user_credentials['userPassword']
        login_context = playwright.request.new_context(base_url=self.base_url)
        login_response = login_context.post("api/ecom/auth/login",data = {
        "userEmail": userEmail,
        "userPassword": userPassword
    })
        #assert login_response.ok
        js = login_response.json()
        return js["token"]

    def createOrder(self, playwright:Playwright,user_credentials):
        token = self.token(playwright,user_credentials)
        base_context = playwright.request.new_context(base_url=self.base_url)
        response = base_context.post(self.Create_url,
                          data=self.Create_payload,
                          headers={"Content-Type": "application/json", "authorization":token})
        print(response.json())
        response_body=response.json()
        order_id = response_body["orders"][0]
        return order_id