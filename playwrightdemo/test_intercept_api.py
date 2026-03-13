from playwrightdemo.sync_api import Page


fakePayloadResponse = {"data":[], "message":"No Orders"}

def intercept_response(route):
    route.fulfill(json = fakePayloadResponse)


def test_intercept_api(page:Page):

    page.goto("https://rahulshettyacademy.com/client")

    ## event listener
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",intercept_response)
    page.get_by_placeholder("email@example.com").fill("rama12321@gmail.com")
    page.locator("#userPassword").type("ram@12345")
    page.get_by_text("Login").click()
    page.get_by_role("button", name="ORDERS").click()
    order_text = page.locator(".mt-4").text_content()
    print(order_text)
