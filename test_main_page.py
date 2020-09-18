from pages.main_page import MainPage
import pytest
import time


@pytest.mark.parametrize('link', ["http://hrtest.alycedev.com/"])
class TestGrabBtn():
    def test_btn_can_grab_one_apple(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        self.btn_ammount = page.count_buttons_grab()
        for btn_number in range(self.btn_ammount):
            page.refresh_list()
            page.add_apple(btn_number)
            page.should_not_be_alert()
            page.apple_counter_shows_how_many(btn_number)
            page.user_apples_not_in_basket(btn_number)
            page.refresh_list()

    def test_btn_can_grab_all_odd_apple(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.refresh_list()
        self.btn_ammount = page.count_buttons_grab()
        self.odd_apples = page.count_odd_apple_in_basket()
        for btn_number in range(self.btn_ammount):
            for odd_apple_num in range(self.odd_apples):
                page.add_apple(btn_number)
                page.should_not_be_alert()
                page.apple_counter_shows_how_many(btn_number)
                page.user_apples_not_in_basket(btn_number)
            page.all_user_apples_odd(btn_number)
            page.refresh_list()

    def test_btn_can_grab_all_even_apple(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.refresh_list()
        self.btn_ammount = page.count_buttons_grab()
        self.even_apples = page.count_even_apple_in_basket()
        for btn_number in range(self.btn_ammount):
            if btn_number != self.btn_ammount-1:
                page.add_apple(btn_number + 1)
                for odd_apple_num in range(self.even_apples):
                    page.add_apple(btn_number)
                    page.should_not_be_alert()
                    page.apple_counter_shows_how_many(btn_number)
                    page.user_apples_not_in_basket(btn_number)
                page.all_user_apples_even(btn_number)
                page.refresh_list()
            else:
                page.add_apple(btn_number - 1)
                for odd_apple_num in range(self.even_apples):
                    page.add_apple(btn_number)
                    page.should_not_be_alert()
                    page.apple_counter_shows_how_many(btn_number)
                    page.user_apples_not_in_basket(btn_number)
                page.all_user_apples_even(btn_number)
                page.refresh_list()

