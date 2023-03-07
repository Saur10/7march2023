import pytest
from selenium import webdriver
#from utilities.Utility import Utils
from Config.config import TestData


@pytest.fixture(params=["chrome"],scope="class")
def setup(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    if request.param == "firefox":
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(TestData.BaseUrl)
    request.cls.driver = driver
    yield
    driver.close()



# @pytest.fixture(scope="class")
# def setup(request, browser):
#     if browser == "chrome":
#         driver = webdriver.Chrome()
#     elif browser == "firefox":
#         driver = webdriver.Firefox()
#     driver.maximize_window()
#     driver.get(TestData.BaseUrl)
#     request.cls.driver = driver
#     yield
#     driver.close()
#
#
# def pytest_addoption(parser):
#     """
#     add browser option to the command
#     """
#     parser.addoption("--browser")
#
#
# @pytest.fixture(scope="class", autouse=True)
# def browser(request):
#     """
#     Retrieve browser name passed as option and return
#     :return: browser name
#     """
#     return request.config.getoption("--browser")