import time
from playwright.sync_api import Playwright, expect
from playwrightdemo.Utils.apiBase import ApiBase


def test_Api(playwright:Playwright):
   browser = playwright.chromium.launch(headless = False)
   context = browser.new_context()
   page = context.new_page()

   #################### Create Order using API
   api = ApiBase()
   order_id = api.createOrder(playwright)

   ################### login

   page.goto("https://rahulshettyacademy.com/client")
   page.get_by_placeholder("email@example.com").fill("rama12321@gmail.com")
   page.locator("#userPassword").type("ram@12345")
   page.get_by_text("Login").click()

   ############### order history

   page.get_by_role("button",name="ORDERS").click()
   row = page.locator("tr").filter(has_text=order_id)
   row.get_by_text("View").click()
   expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping")
   time.sleep(2)





