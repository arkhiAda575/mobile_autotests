from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseScreen:
    def __init__(self, app):
        self.app = app

    def custom_find_element(self, locator, wait_time=10):
        element = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )
        return element

    def click_element(self, locator, wait_time=10):
        element = self.custom_find_element(locator, wait_time)
        element.click()

    def fill_element(self, locator, text, wait_time=10):
        element = self.custom_find_element(locator, wait_time)
        element.send_keys(text)

    def send_enter(self, locator, wait_time=10):
        element = self.custom_find_element(locator, wait_time)
        element.send_keys(Keys.ENTER)