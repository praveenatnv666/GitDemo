from selenium.webdriver.common.by import By

from PageObjects.ConfirmationPage import ConfirmationPage


class checkoutPage:
    def __init__(self,driver):
        self.driver = driver
        self.checkout_button = (By.XPATH, "//button[@class='btn btn-success']")


    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()
        confirmation_page = ConfirmationPage(self.driver)
        return confirmation_page