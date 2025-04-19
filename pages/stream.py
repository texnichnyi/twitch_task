from base.base_page import BasePage


class Stream(BasePage):
    """
    Stream page
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.stream_media_player = self.locator_css_selector("div[data-a-target='player-controls']")

    def wait_for_stream_loaded(self):
        self.wait_for_attribute(locator=self.stream_media_player, attribute='data-a-visible', attribute_value='false')
