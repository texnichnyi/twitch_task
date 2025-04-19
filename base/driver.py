from appium import webdriver

from utils.json_parser import capabilities_parser


class Driver:
    """
      Class for working with driver
    """
    def __init__(self, platform):
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities_parser(platform=platform))
        self.driver.implicitly_wait(5)
        self.driver.get('http://m.twich.tv/')

    def get_driver(self):
        return self.driver

    def close_driver(self):
        self.driver.quit()
