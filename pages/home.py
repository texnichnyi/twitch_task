from base.base_page import BasePage
from pages.categories import Categories


class Home(BasePage):
    """
    Home page
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.search_icon_locator = self.locator_css_selector("a[href='/directory']")

    def click_search_icon(self) -> Categories:
        search_icon = self.find_element(locator=self.search_icon_locator)
        search_icon.click()
        return Categories(driver=self.driver)
