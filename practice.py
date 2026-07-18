from asyncio import wait

from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect
import time

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False
    )
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://rahulshettyacademy.com/client/#/dashboard/dash")

    print(page.title())

    page.get_by_placeholder("email@example.com").type("rama12321@gmail.com")
    page.locator("#userPassword").fill("ram@12345")
    page.get_by_text("Login").click()
    Addias_price = page.locator(
        "//*[contains(text(),'Add To Cart')]/preceding-sibling::div"
    ).first

    print(Addias_price.text_content())
    page.get_by_role("button", name="Add To Cart").first.click()

    search = page.get_by_placeholder("search").nth(1)
    search.fill("iphone")
    page.wait_for_timeout(2000)
    search.press("Enter")
    page.locator("//*[contains(text(),'iphone')]").wait_for()
    iphone_price = page.locator(
        "//*[contains(text(),'Add To Cart')]/preceding-sibling::div"
    ).nth(0)

    print(iphone_price.text_content())
    page.get_by_role("button", name="Add To Cart").first.click()

    page.get_by_role("button", name="Cart").nth(0).click()

    total = page.locator(
        "//span[text()='Total']/following-sibling::span"
    ).text_content()

    print(total)

    page.get_by_role("button", name="Checkout").click()
    page.locator("select").nth(1).select_option(value="27")
    page.locator("//*[contains(text(),'CVV Code ')]/following-sibling::input").fill("123")
    page.locator("//*[contains(text(),'Name on Card')]/following-sibling::input").type("teja")

    page.get_by_placeholder("Select Country").type("Ind")

    page.wait_for_timeout(3000)

    # page.locator("section.ta-results button").filter(
    #     has_text="India"
    # ).click()

    countries = page.locator("section.ta-results button")

    for i in range(countries.count()):

        country = countries.nth(i).inner_text().strip()

        print(country)

        if country == "India":
            countries.nth(i).click()
            break

    page.get_by_text("Place Order ").click()
    orders_id=page.locator("//label[contains(@class,'ng-star-inserted')]").all_text_contents()

    with page.expect_popup() as childpage:
        page.locator(".blinkingText").click()
    child = childpage.value
    text = child.get_by_text("Signup/Signin").text_content()
    page.wait_for_timeout(2000)
    assert text == "Signup/Signin"
    page.bring_to_front()

    time.sleep(2)

    browser.close()
