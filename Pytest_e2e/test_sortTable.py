import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_sortTable(browserInstance):

    driver = browserInstance

    sortedlist = []
    original_veggie_list = []

    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    # click on column header

    driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

    # collect all veggie names -> veggie list

    veggie_list = driver.find_elements(By.XPATH, "//td[1]")

    for veg in veggie_list:
        sortedlist.append(veg.text)

        original_veggie_list = sortedlist.copy()

        sortedlist.sort()

    print("original_veggie_list ", original_veggie_list)

    # Sort this veggie list -> newSorted list

    print("sorted list ", sortedlist)

    # veggie list == new sorted list

    assert original_veggie_list == sortedlist



