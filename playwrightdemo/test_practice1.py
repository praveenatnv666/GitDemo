import time

from playwrightdemo.sync_api import Page, expect


def test_UI(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).not_to_be_visible()
    page.get_by_role("button", name="Show").click()
    time.sleep(3)

    #### Alert ######
    page.on("dialog", lambda dialog: dialog.accept())
    page.locator("#alertbtn").click()
    #page.on("alert", lambda alert: alert.accept())


    page.locator("#checkBoxOption2").click()

    #### New window
    with page.expect_popup() as new_window1:
        page.get_by_text("Open Window").click()
        new1 = new_window1.value
        Title1=new1.title()
        print(Title1)
        new1.close()

    ##### Iframe
    page_frame = page.frame_locator("#courses-iframe")
    page_frame.get_by_role("link", name="All Access plan").click()
    expect(page_frame.locator("body")).to_contain_text(" Happy Subscibers!")

    ##### mouse over
    page.get_by_role("button", name="Mouse Hover").hover()
    page.get_by_role("link", name="Reload").click()

    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
            price_colValue=index
            print("rice:", price_colValue)
            break
    rice_row = page.locator("tr").filter(has_text="Rice")
    expect(rice_row.locator("td").nth(price_colValue)).to_have_text("37")

    time.sleep(2)

