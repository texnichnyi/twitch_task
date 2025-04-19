from base.base_page import BasePage
from pages.stream import Stream


class Categories(BasePage):
    """
    Categories page /directory
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.search_input_locator = self.locator_xpath("//header//input[@type='search']")
        self.search_starcraft_option_locator = self.locator_css_selector("a[href='/directory/category/starcraft-ii']")
        self.starcraft_streamer_locator = self.locator_xpath("//button[contains(@class, 'tw-link')]")
        self.follow_button_locator = self.locator_css_selector("button[data-a-target='game-directory-follow-button'] svg")

    def fill_search_input(self, text):
        search_input = self.find_element(self.search_input_locator)
        search_input.send_keys(text)

    def click_search_option(self):
        search_starcraft_option = self.find_element(self.search_starcraft_option_locator)
        search_starcraft_option.click()
        self.wait_for_element_by(self.follow_button_locator)

    def open_stream(self) -> Stream:
        starcraft_streamer = self.find_element(self.starcraft_streamer_locator)
        starcraft_streamer.click()
        return Stream(driver=self.driver)