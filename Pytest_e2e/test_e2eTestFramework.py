import json

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.Login import LoginPage
from PageObjects.Shoppage import ShopPage

test_data_path ='C:\\Users\\prave\\PycharmProjects\\PythonProject\\data\\test_e2eTestFramework.json'
with open(test_data_path) as file:
    test_data = json.load(file)
    test_list = test_data["data"]


@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item",test_list)
def  test_e2e(browserInstance, test_list_item):
    driver = browserInstance

    loginPage = LoginPage(driver)
    print(loginPage.getTitle())
    shopPage=loginPage.login(test_list_item["userEmail"],test_list_item["userPassword"])

    shopPage = ShopPage(driver)
    print(shopPage.getTitle())
    shopPage.add_Product_to_cart(test_list_item["productName"])
    Checkout = shopPage.goTocart()
    confirmation_page = Checkout.checkout()
    confirmation_page.confirmationPage(test_list_item["country"])
    confirmation_page.validateOrder()



