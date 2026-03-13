import time

from playwrightdemo.sync_api import Page, expect


def test_PlaywrightBasics(playwright,page):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

#def test_loginPage(page:Page):
    #page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")

    ##### Child Page

    with page.expect_popup() as childpage:
        page.get_by_role("link", name="Free Access").click()
        child = childpage.value
        child.get_by_role("link", name="All Access plan").click()
        child.close()
        page.bring_to_front()

    ## locator tag:" " id:"#" Class:"."
    page.locator("#password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("span.radiotextsty", has_text="User").click()
    page.get_by_role("button", name="Okay").click()
    page.locator(".radiotextsty").filter(has_text="User").click()
    page.get_by_role("button", name="Sign In").click()

    #expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
   ###### Dashboard ######
    product1 = page.locator("app-card").filter(has_text="iphone X")
    product1.get_by_role("button").click()
    page.get_by_text("Checkout").click()

    ##### Checkout #########
    expect(page.locator(".media")).to_have_count(1)
    page.get_by_role("button", name="Checkout").click()
    #page.get_by_label("Please choose your delivery location. ").fill("ind")
    page.locator("#country").type("ind")
    #page.wait_for_selector(".suggestions")
    # page.locator(".suggestions").filter(has_text="India").click()
    #page.locator(".suggestions").get_by_text("India").click()
    page.locator(".suggestions >> text=India").click()
    page.locator("label[for='checkbox2']").click()
    page.get_by_role("button", name="Purchase").click()

    expect(page.locator(".alert-success")).to_contain_text("Success")
    text = page.locator(".alert-success").text_content()
    print(text)
    assert "Success" in text

    #time.sleep(5)