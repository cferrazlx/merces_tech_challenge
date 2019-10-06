from base.config import ElementActions


# Setting up page usage
class ShopPage(ElementActions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Element locators
    _cookies_button = "//button[@class='btn btn-agree']" # XPATH
    _collection_accessories = "//a[@data-testid='dcp-shopnav-main_92412837-4ba7-409a-bde4-62a8d50f9ce5-link']" # XPATH
    _model_cars = "//a[@data-ng-click='selectCategory(category)'][contains(.,'Model cars')]" # XPATH
    _motor_sport = "//a[@data-ng-click='selectCategory(category)'][contains(.,'Motorsport')]" # XPATH
    _formula_1_race_car = \
        "//img[@data-ng-src='/images/2-5-litre-Formula-1-race-car--with-free-standing-wheels--W196--1954-0.png/mba_medienbank/shop_448x448/0003fcad.png']" # XPATH
    _add_to_basket = "//button[@data-testid='pdp-buy-box-add-to-basket-add']" # XPATH
    _go_to_cart = "//button[@data-testid='pdp-buy-box-add-to-basket-got-to-cart']" # XPATH
    _continue_address_delivery = "//button[@data-testid='co-func-header-forward']" # XPATH
    _guest_email = "//input[@id='dcp-login-guest-user-email']" # XPATH
    _place_order_guest = "//button[@data-testid='co-order-process-login-guest-user-cta']" # XPATH
    _mr_radio = "//label[contains(text(),'Mr')]" # XPATH
    _first_name = "co_payment_address-firstName" # ID
    _last_name = "co_payment_address-lastName" # ID
    _number = "co_payment_address-line2" # ID
    _street = "co_payment_address-line1" # ID
    _town = "co_payment_address-town" # ID
    _post_code = "co_payment_address-postalCode" # ID
    _dob_day = "//input[@data-testid='dcp-schema-form-date_dateOfBirth-first']" # XPATH
    _dob_month = "//input[@data-testid='dcp-schema-form-date_dateOfBirth-second']" # XPATH
    _dob_year = "//input[@data-testid='dcp-schema-form-date_dateOfBirth-third']" # XPATH
    _continue_payment = "//button[@data-testid='co-func-footer-forward']" # XPATH
    _select_credit_card = "//strong[contains(.,'Credit Card')]" # XPATH
    _master_card = "//label[contains(.,'MasterCard')]" # XPATH
    _continue_verification_order = "//button[@data-testid='co-func-header-forward']" # XPATH
    _order_now = "//button[@data-testid='co-func-footer-forward']" # XPATH

    def add_to_cart(self):
        self.click(self._cookies_button)
        self.wait_for_element(self._collection_accessories)
        self.click(self._collection_accessories)
        self.wait_for_element(self._model_cars)
        self.click(self._model_cars)
        self.click(self._motor_sport)
        self.wait_for_element(self._formula_1_race_car)
        self.click(self._formula_1_race_car)
        self.click(self._add_to_basket)
        self.click(self._go_to_cart)

    def continue_guest(self):
        self.wait_for_element(self._continue_address_delivery)
        self.click(self._continue_address_delivery)
        self.wait_for_element(self._guest_email)
        self.type_xpath(self._guest_email, self.guest_email())
        self.click(self._place_order_guest)

    def delivery_details(self):
        self.wait_for_element(self._mr_radio)
        self.click(self._mr_radio)
        self.type_id(self._first_name, self.first_name())
        self.type_id(self._last_name, self.last_name())
        self.type_id(self._number, self.number())
        self.type_id(self._street, self.street())
        self.type_id(self._town, self.town())
        self.type_id(self._post_code, self.post_code())
        self.type_xpath(self._dob_day, self.day())
        self.type_xpath(self._dob_month, self.month())
        self.type_xpath(self._dob_year, self.year())
        self.wait_for_element(self._continue_payment)
        self.click(self._continue_payment)

    def payment(self):
        self.wait_for_element(self._select_credit_card)
        self.click(self._select_credit_card)
        self.click(self._master_card)
        self.click(self._continue_verification_order)

    def order(self):
        self.is_element_present(self._order_now, locatorType="xpath")

    def order_formula_1(self):
        self.add_to_cart()
        self.continue_guest()
        self.delivery_details()
        self.payment()
        self.order()

