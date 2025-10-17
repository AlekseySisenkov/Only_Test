import pytest
from selenium import webdriver

from data import HEADER_PAGE_REF
from pages.header_page import HeaderPage


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()

    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def header_page(driver):
    driver.get(HEADER_PAGE_REF)
    return HeaderPage(driver)