

from selenium.webdriver.common.by import By

from PageObjects.Shoppage import ShopPage
from Utils.BrowserUtils import BrowserUtils


class LoginPage:
     def __init__(self, driver):
         super().__init__(driver)
         self.driver = driver
         self.username_input = (By.ID, "username")
         self.password = (By.ID, "password")
         self.sign_button = (By.ID, "signInBtn")


     def login(self,username,password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.sign_button).click()
        shopPage = ShopPage(self.driver) ## calling next class
        return shopPage
