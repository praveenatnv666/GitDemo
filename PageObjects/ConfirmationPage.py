from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ConfirmationPage:
    def __init__(self,driver):
        self.driver = driver
        self.country = (By.ID, "country")
        self.country_suggestion = (By.CLASS_NAME, "suggestions")
        self.select_Country = (By.XPATH, "//div[@class='suggestions']/ul/li/a[1]")
        self.checkBox = (By.XPATH, "//input[@id='checkbox2']")
        self.purchase = (By.XPATH, "//input[@value='Purchase']")
        self.SuccessMsg = (By.CLASS_NAME, "alert-success")

    def confirmationPage(self,CountryName):

        self.driver.find_element(*self.country).send_keys(CountryName)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located(self.country_suggestion))
        self.driver.find_element(*self.select_Country).click()
        self.driver.find_element(*self.checkBox)
        self.driver.find_element(*self.purchase).click()

    def validateOrder(self):

        success = self.driver.find_element(*self.SuccessMsg).text
        assert "Success!" in success
