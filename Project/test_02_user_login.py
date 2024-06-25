import time

import pytest
from Object.HomePage import Paths
from Utilities.BaseClass import BaseClass
from test_data.testcase_data import *


class TestSignUp(BaseClass):


    def test_login_click(self):
        obj = Paths(self.driver)
        obj.login_button().click()

    def test_login_process(self, getData):
        obj = Paths(self.driver)
        log = self.getLogger()
        print(getData)
        obj.login_username().clear()
        obj.login_username().send_keys(getData["user_name"])
        obj.login_password().clear()
        obj.login_password().send_keys(getData["password"])
        obj.login_click_btn().click()
        time.sleep(3)
        if getData["tag"] == "negative":
            flag = self.alert_check()
            log.info("---- %s ----- %s ---- %s " % (getData["user_name"], getData["password"], flag.text))
            assert "Wrong" in flag.text
            flag.accept()
        else:
            log.info("---- %s ----- %s ----" % (getData["user_name"], getData["password"]))
            assert getData["user_name"] in obj.home_page_text().text

    @pytest.fixture(params=Data.getTestData("login", "../testcases/sign_up.xlsx"))
    def getData(self, request):
        return request.param


    def test_product_display(self):
        obj = Paths(self.driver)
        self.scrolldown_window(0, 400)
        time.sleep(5)
        obj.product_phone_btn().click()
        A = obj.product_phone_list()

        if A.is_displayed():
            print("Is there perfect product")
        else:
            print("It's showing wrong product")

    def test_product_navigate(self):
        obj = Paths(self.driver)
        self.scrolldown_window(0, 400)
        time.sleep(2)
        obj.product_select_phone().click()
        B = obj.product_display_nextpage()

        if B.is_displayed():
            print("Product navigated successfully")
        else:
            print("Navigated is another page")

        obj.home_page_button().click()

    def test_navigate_last_product(self):
        obj = Paths(self.driver)
        self.scrolldown_window(0, 1000)
        time.sleep(2)
        # Navigate to the last page by clicking next
        self.click_next_btn().click()

        # select the last product and add the product to the cart.
        obj.shopping_cart_product().click()
        obj.add_to_cart_product().click()
        time.sleep(3)
        alert = self.alert_check()
        alert.accept()
        obj.home_page_cart_button().click()
        self.delete_button().click()
        time.sleep(3)

    def test_without_adding(self):
        obj = Paths(self.driver)
        C = obj.check_cart_product()

        if C.is_displayed():
            print("Available on product")

        else:
            print("Please select the product")



