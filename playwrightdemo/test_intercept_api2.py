import time

from playwrightdemo.sync_api import Page, Playwright, expect

from playwrightdemo.Utils.apiBase import ApiBase


def interceptRequest(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=69aaf18f415d779f9b5decc0")

def test_intercept_api(page:Page):

    page.goto("https://rahulshettyacademy.com/client")
    ## event listener
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",interceptRequest)
    page.get_by_placeholder("email@example.com").fill("rama12321@gmail.com")
    page.locator("#userPassword").type("ram@12345")
    page.get_by_text("Login").click()
    page.get_by_role("button", name="ORDERS").click()
    time.sleep(5)
    page.get_by_role("button", name="View").first.click()
    time.sleep(5)
    text = page.locator(".blink_me").text_content()
    print(text)

def test_session_storage(playwright:Playwright):
    api = ApiBase()
    token = api.token(playwright)
    broswer = playwright.chromium.launch(headless=False)
    context = broswer.new_context()
    page = context.new_page()
    #### script to inject token in session storage
    page.add_init_script(f"""localStorage.setItem("token", '{token}');""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()
