from base.base_page import BasePage


class Stream(BasePage):
    """
    Stream page
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.stream_media_player = self.locator_css_selector("div[data-a-target='player-controls']")
        self.loading_spinner = self.locator_css_selector(".tw-loading-spinner")

    def wait_for_stream_loaded(self):
        self.wait_for_element_by(self.loading_spinner)
        self.wait_for_element_invisibility_by(self.loading_spinner)
        self.wait_for_attribute(locator=self.stream_media_player, attribute='data-a-visible', attribute_value='false')
