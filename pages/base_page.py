from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from config import base_url, email_url


class BasePage:
    def __init__(self, driver, timeout=60):
        self.driver = driver
        self.base_url = base_url
        self.email_url = email_url
        self.driver.implicitly_wait(timeout)

    def get_main_page(self):
        return self.driver.get(self.base_url)

    def go_to_mail(self):
        self.driver.execute_script("window.open()")
        self.switch_new()
        return self.driver.get(self.email_url)

    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f"not find{locator}")

    def find_elements(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), message=f"not find{locator}")

    def move_to_element(self, locator):
        element = self.find_element(locator)
        return ActionChains(self.driver).move_to_element(element).perform()

    def is_visible(self, locator):
            """ Check is the element visible or not. """
            element = self.find_element(locator)
            if element:
                return element.is_displayed()
            return False

    def switch_to_iframe(self, iframe):
        """ Switch to iframe by it's name. """
        self.driver.switch_to.frame(iframe)

    def switch_new(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])

    def escape(self):
        return webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

    def switch_to_first_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[0])

    def close_current_window(self):
        self.driver.close()
        return self.driver.switch_to.window(self.driver.window_handles[0])

    def save_first_window(self):
        return self.driver.window_handles[0]

    def save_second_window(self):
        return self.driver.window_handles[1]





