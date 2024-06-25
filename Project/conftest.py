import time

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def Invoke_Browser(request):
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument('ignore-certificate-errors')
    options.add_argument("--disable-application-cache")
    service_obj = Service("C:\\chrome_driver\\chromedriver")
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://www.demoblaze.com/")
    driver.implicitly_wait(30)
    driver.maximize_window()
    request.cls.driver = driver
    driver.refresh()
    yield
    time.sleep(2)
    # driver.quit()






