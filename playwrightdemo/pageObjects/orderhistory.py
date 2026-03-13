from playwright.sync_api import expect


class OrderHistorypage:
    def __init__(self,page):
        self.page = page

    def orderhistory(self,order_id):
        row = self.page.locator("tr").filter(has_text=order_id)
        row.get_by_text("View").click()
        expect(self.page.locator(".tagline")).to_contain_text("Thank you for Shopping")
