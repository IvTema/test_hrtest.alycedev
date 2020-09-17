from pages.main_page import MainPage
import pytest


@pytest.mark.parametrize('link', ["http://hrtest.alycedev.com/"])
class TestGrabBtn():
    def test_btn_can_grab_one_apple(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        for btn_number in range(page.count_buttons_grab()):
            page.refresh_list()
            page.add_apple(btn_number)
            page.should_not_be_alert()
            page.apple_counter_shows_how_many(btn_number)
            page.user_apple_not_in_basket(btn_number)
            page.refresh_list()

    def test_btn_can_grab_all_odd_apple(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        for btn_number in range(page.count_buttons_grab()):
            page.refresh_list()
            for