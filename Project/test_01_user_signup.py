import time

import pytest
from Object.HomePage import Paths
from Utilities.BaseClass import BaseClass
from test_data.testcase_data import *

class TestSignUp(BaseClass):

    def test_check_url(self):
        log = self.getLogger()
        log.info("----- %s -----" % self.get_url())
        assert "https://www.demoblaze.com/" == self.get_url()

    def test_sign_up_click(self):
        obj = Paths(self.driver)
        obj.signup_button().click()

    def test_signup_process(self, getData):
        obj = Paths(self.driver)
        log = self.getLogger()
        obj.signup_username().clear()
        obj.signup_username().send_keys(getData["user_name"])
        obj.signup_password().clear()
        obj.signup_password().send_keys(getData["password"])
        obj.signup_click_btn().click()
        time.sleep(3)
        if getData["tag"] == "negative":
            flag = self.alert_check()
            log.info("---- %s ----- %s ---- %s " % (getData["user_name"], getData["password"], flag.text))
            assert "already exist" in flag.text
            flag.accept()
        else:
            flag = self.alert_check()
            assert "successful" in flag.text



    @pytest.fixture(params=Data.getTestData("signup", "../testcases/sign_up.xlsx"))
    def getData(self, request):
        return request.param



