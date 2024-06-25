import inspect
import logging
from telnetlib import EC

import pytest
from selenium.common import NoAlertPresentException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("Invoke_Browser")
class BaseClass:

    def get_url(self):
        return self.driver.current_url

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger

    def alert_check(self):
        alert = self.driver.switch_to.alert
        return alert

    def scrolldown_window(self, a, b):
        self.driver.execute_script("window.scrollBy(arguments[0], arguments[1]);", a, b)

    def product_list(self):
        return self.driver.find_elements(By.XPATH, "//div[@class='col-lg-4 col-md-6 mb-4']")

    def click_next_btn(self):
        return self.driver.find_element(By.XPATH, "//button[@id='next2']")

    def delete_button(self):
        return self.driver.find_element(By.XPATH, "//a[normalize-space()='Delete']")

    # def __init__(self, driver):
    #     self.driver = driver
    #
    # def alert_check_process(self):
    #     try:
    #         # Wait for the alert to be present
    #         WebDriverWait(self.driver, 10).until(EC.alert_is_present())
    #         alert = self.driver.switch_to.alert
    #         return alert
    #     except NoAlertPresentException:
    #         return None
    #     except TimeoutException:
    #         return None