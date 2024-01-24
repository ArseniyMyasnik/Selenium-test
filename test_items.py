import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_bin(browser):
    browser.implicitly_wait(5)
    element = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    element.click()