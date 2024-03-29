import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_add_to_bin(browser):
    browser.implicitly_wait(5)
    element = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    is_button_enable = element.is_enabled()
    assert is_button_enable == True
    element.click()
    browser.implicitly_wait(5)
    browser.execute_script('window.scrollBy(0, 300);')
