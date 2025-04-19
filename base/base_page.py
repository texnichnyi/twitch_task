import os

from wait_for import wait_for
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

from base.locator import Locators
from utils.path_helper import get_project_root


class BasePage:
    """
    Class for working with pages
    """

    def __init__(self, driver):
        self.driver = driver
        self.locator_css_selector = Locators.css_selector
        self.locator_xpath = Locators.xpath

    def wait_for_element_by(self, element_locator, timeout=10) -> WebElement:
        """
        :param element_locator: locator of element that we're waiting
        :param timeout: time of waiting
        :return: WebElement
        """
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator=element_locator))

    def wait_for_attribute(self, locator: Locators.Locator, attribute, attribute_value, timeout=20, delay=3):
        """
        :param locator: locator of element that we will work with
        :param attribute: attribute that we will wait to be
        :param attribute_value: value of attribute
        :param timeout: time of waiting on value
        :param delay: delay that we have for function to wait until page load
        """
        element = self.wait_for_element_by(locator)
        wait_for(
            lambda: element.get_attribute(name=attribute) == attribute_value,
            timeout=timeout,
            delay=delay
        )

    def find_element(self, locator: Locators.Locator) -> WebElement:
        return self.driver.find_element(locator.by, locator.value)

    def save_screenshot(self, file_name):
        self.driver.get_screenshot_as_file(os.path.join(get_project_root(), 'result_screenshots', file_name))

    def scroll_down_on_screen_height(self):
        self.driver.execute_script("window.scrollBy(0, (window.innerHeight > 0) ? window.innerHeight : screen.height);")
