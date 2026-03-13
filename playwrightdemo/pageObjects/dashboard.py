class DashboardPage:

    def __init__(self,page):
        self.page = page

    def ordersNavLink(self):
        self.page.get_by_role("button", name="ORDERS").click()