# import time
#
# import pytest
# from Object.HomePage import Paths
# from Utilities.BaseClass import BaseClass
# from test_data.testcase_data import *
#
#
# class TestSignUp(BaseClass):
#
#     def test_product_browsing(self):
#         obj = Paths(self.driver)
#         self.scrolldown_window()
#         time.sleep(5)
#         obj.product_phone_btn().click()
#         A = obj.product_phone_list()
#
#         if A.is_displayed():
#             print("Is there perfect product")
#         else:
#             print("It's showing wrong product")
#
#         obj.product_select_phone().click()
#         B = obj.product_display_nextpage()
#
#         if B.is_displayed():
#             print("Product navigated successfully")
#         else:
#             print("Navigated is another page")