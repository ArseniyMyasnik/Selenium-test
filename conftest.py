import pytest
from selenium import webdriver
import time



def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help="Choose site language")

@pytest.fixture
def browser(request):
    language = request.config.getoption("language")
    if language is None:
        raise pytest.UsageError("--language is not used")
    browser = webdriver.Chrome()
    browser.get(f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/")
    yield browser
    time.sleep(10)
    browser.quit()