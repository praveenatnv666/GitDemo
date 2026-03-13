from selenium.webdriver.common.by import By

from PageObjects.checkoutPage import checkoutPage
from Utils.BrowserUtils import BrowserUtils


class ShopPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_link = (By.XPATH, '//a[contains(@href,"shop")]')
        self.product_card = (By.XPATH, '//*[@class="col-lg-3 col-md-6 mb-3"]')
        self.cartIcon = (By.CLASS_NAME, "btn-primary")


    def add_Product_to_cart(self, product_name):

        self.driver.find_element(*self.shop_link).click()
        self.driver.implicitly_wait(5)
        products = self.driver.find_elements(*self.product_card)
        for i in products:
            productName = i.find_element(By.XPATH, "div/div/h4/a").text
            if productName == "product_name":
                i.find_element(By.XPATH, "div/div/button").click()

    def goTocart(self):
        self.driver.find_element(*self.cartIcon).click()
        Checkout = checkoutPage(self.driver)
        return Checkout