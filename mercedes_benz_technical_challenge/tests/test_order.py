from base.config import ElementActions
from base.config import BasicSetup
import unittest
from pages.shop_page import ShopPage

class LoginPageTest(ShopPage, ElementActions, BasicSetup):
    def test_order_flow(self):
        try:
            print("Installing Chromedriver")
            self.order_formula_1()


            self.test_result = 'pass'
            print("Test passed - 'Order Now' button is present")

        except AssertionError:

            self.test_result = 'fail'

            raise
if __name__ == '__main__':
    unittest.main()