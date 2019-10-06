import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os

# In this class we set up the browser and URL
class BasicSetup(unittest.TestCase):
    def setUp(self):
        baseURL = "https://shop.mercedes-benz.com/en-gb/collection/"
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(4)

if __name__ == '__main__':
    unittest.main()

# Methods to interact with the browser
class ElementActions(BasicSetup):
    def click(self, xpath):
        self.driver.find_element(By.XPATH, xpath).click()

    def click_id(self, id):
        self.driver.find_element(By.ID, id).click()

    def type_id(self, id, text):
        self.driver.find_element(By.ID, id).send_keys(text)

    def type_xpath(self, xpath, text):
        self.driver.find_element(By.XPATH, xpath).send_keys(text)

    def get_by_type(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            return False

    def get_element(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.get_by_type(locatorType)
            element = self.driver.find_element(byType, locator)
        except:
            return element

    def get_text(self, locator="", locatorType="id", element=None, info=""):

        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locatorType)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                text = text.strip()
        except:
            print_stack()
            text = None
        return text

    def is_element_present(self, locator="", locatorType="id", element=None):

        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locatorType)
            if element is not None:
                return True
            else:
                return False
        except:
            print("Element not found")
            return False

    def wait_for_element(self, xpath=''):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        return element

    def wait_for_element_id(self, id=''):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, id)))
        return element

    def web_scroll(self, direction="up"):

        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 200);")

    def guest_email(self, guestEmail='cferraz.prof@gmail.com'):
        return guestEmail

    def day(self, day='11'):
        return day

    def month(self, month='11'):
        return month

    def year(self, year='1980'):
        return year

    def first_name(self, firstName='Miles'):
        return firstName

    def last_name(self, lastName='Davis'):
        return lastName

    def number(self, number='2'):
        return number

    def street(self, street='Dimmer Drive, Wilton'):
        return street

    def town(self, town='Wilton'):
        return town

    def post_code(self, postCode='SP2 0FL'):
        return postCode
