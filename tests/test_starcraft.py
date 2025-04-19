def test_open_starcraft_stream(get_home_page):
    categories_page = get_home_page.click_search_icon()
    categories_page.fill_search_input('StarCraft II')
    categories_page.click_search_option()
    categories_page.scroll_down_on_screen_height()
    categories_page.scroll_down_on_screen_height()
    stream_page = categories_page.open_stream()
    stream_page.wait_for_stream_loaded()
    stream_page.save_screenshot('starcraft_stream.png')
