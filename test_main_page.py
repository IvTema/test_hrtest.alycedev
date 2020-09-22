from pages.main_page import MainPage
import pytest
import time


@pytest.mark.parametrize('link', ["http://hrtest.alycedev.com/"])
class TestGrabBtn():
    def test_btn_can_grab_one_apple(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.refresh_list()
        self.btn_ammount = page.count_buttons_grab()
        self.apples_in_basket = page.count_apples_in_basket()
        for btn_number in range(self.btn_ammount):
            page.add_apple(btn_number)
            page.should_not_be_alert()
            page.check_apples_added(btn_number, 0, self.apples_in_basket-1)
            page.apple_counter_shows_how_many(btn_number)
            page.user_apples_not_in_basket(btn_number)
            page.refresh_list()

    def test_btn_can_grab_all_odd_apple(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.refresh_list()
        self.btn_ammount = page.count_buttons_grab()
        self.apples_in_basket = page.count_apples_in_basket()
        self.odd_apples = page.count_odd_apple_in_basket()
        for btn_number in range(self.btn_ammount):
            for odd_apple_num in range(self.odd_apples):
                page.add_apple(btn_number)
                page.should_not_be_alert()
                page.check_apples_added(btn_number, odd_apple_num, self.apples_in_basket - (odd_apple_num+1))
                page.apple_counter_shows_how_many(btn_number)
                page.user_apples_not_in_basket(btn_number)
            page.all_user_apples_odd(btn_number)
            page.refresh_list()

    def test_btn_can_grab_all_even_apple(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.refresh_list()
        self.btn_ammount = page.count_buttons_grab()
        self.apples_in_basket = page.count_apples_in_basket()
        self.even_apples = page.count_even_apple_in_basket()
        for btn_number in range(self.btn_ammount):
            if btn_number != self.btn_ammount-1:
                page.add_apple(btn_number + 1)
                page.check_apples_added(btn_number+1, 0, self.apples_in_basket - 1)
                for even_apple_num in range(self.even_apples):
                    page.add_apple(btn_number)
                    page.should_not_be_alert()
                    page.check_apples_added(btn_number, even_apple_num, self.apples_in_basket - (even_apple_num + 2))
                    page.apple_counter_shows_how_many(btn_number)
                    page.user_apples_not_in_basket(btn_number)
                page.all_user_apples_even(btn_number)
                page.refresh_list()
            else:
                page.add_apple(btn_number - 1)
                page.check_apples_added(btn_number + 1, 0, self.apples_in_basket - 1)
                for even_apple_num in range(self.even_apples):
                    page.add_apple(btn_number)
                    page.should_not_be_alert()
                    page.check_apples_added(btn_number, even_apple_num, self.apples_in_basket - (even_apple_num + 2))
                    page.apple_counter_shows_how_many(btn_number)
                    page.user_apples_not_in_basket(btn_number)
                page.all_user_apples_even(btn_number)
                page.refresh_list()

    def test_alert_cant_add_even_to_user_odd(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.refresh_list()
        self.btn_ammount = page.count_buttons_grab()
        self.apples_in_basket = page.count_apples_in_basket()
        self.odd_apples = page.count_odd_apple_in_basket()
        for btn_number in range(self.btn_ammount):
            for odd_apple_num in range(self.odd_apples):
                page.add_apple(btn_number)
                page.should_not_be_alert()
                page.check_apples_added(btn_number, odd_apple_num, self.apples_in_basket - (odd_apple_num+1))
                page.apple_counter_shows_how_many(btn_number)
                page.user_apples_not_in_basket(btn_number)
            page.all_user_apples_odd(btn_number)
            page.alert_shows_after_try_add_wrong_apple_type(btn_number)
            page.refresh_list()

    def test_alert_cant_add_odd_to_user_even(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.refresh_list()
        self.btn_ammount = page.count_buttons_grab()
        self.apples_in_basket = page.count_apples_in_basket()
        self.even_apples = page.count_even_apple_in_basket()
        for btn_number in range(self.btn_ammount):
            if btn_number != self.btn_ammount-1:
                page.add_apple(btn_number + 1)
                page.check_apples_added(btn_number+1, 0, self.apples_in_basket - 1)
                for even_apple_num in range(self.even_apples):
                    page.add_apple(btn_number)
                    page.should_not_be_alert()
                    page.check_apples_added(btn_number, even_apple_num, self.apples_in_basket - (even_apple_num + 2))
                    page.apple_counter_shows_how_many(btn_number)
                    page.user_apples_not_in_basket(btn_number)
                page.all_user_apples_even(btn_number)
                page.alert_shows_after_try_add_wrong_apple_type(btn_number)
                page.refresh_list()
            else:
                page.add_apple(btn_number - 1)
                page.check_apples_added(btn_number + 1, 0, self.apples_in_basket - 1)
                for even_apple_num in range(self.even_apples):
                    page.add_apple(btn_number)
                    page.should_not_be_alert()
                    page.check_apples_added(btn_number, even_apple_num, self.apples_in_basket - (even_apple_num + 2))
                    page.apple_counter_shows_how_many(btn_number)
                    page.user_apples_not_in_basket(btn_number)
                page.all_user_apples_even(btn_number)
                page.alert_shows_after_try_add_wrong_apple_type(btn_number)
                page.refresh_list()

    def test_alert_cant_add_empty_basket(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.refresh_list()
        self.btn_ammount = page.count_buttons_grab()
        self.apples_in_basket = page.count_apples_in_basket()
        self.odd_apples = page.count_odd_apple_in_basket()
        self.even_apples = page.count_even_apple_in_basket()
        for btn_number in range(self.btn_ammount):
            for odd_apple_num in range(self.odd_apples):
                page.add_apple(btn_number)
                page.should_not_be_alert()
                page.check_apples_added(btn_number, odd_apple_num, self.apples_in_basket - (odd_apple_num + 1))
                page.apple_counter_shows_how_many(btn_number)
                page.user_apples_not_in_basket(btn_number)
            page.all_user_apples_odd(btn_number)
            if btn_number != self.btn_ammount-1:
                for even_apple_num in range(self.even_apples):
                    page.add_apple(btn_number + 1)
                    page.should_not_be_alert()
                    page.check_apples_added(btn_number+1, even_apple_num,
                                            self.apples_in_basket - self.odd_apples - (even_apple_num + 1))
                    page.apple_counter_shows_how_many(btn_number + 1)
                    page.user_apples_not_in_basket(btn_number + 1)
                page.all_user_apples_even(btn_number + 1)
            else:
                for even_apple_num in range(self.even_apples):
                    page.add_apple(btn_number - 1)
                    page.should_not_be_alert()
                    page.check_apples_added(btn_number - 1, even_apple_num,
                                            self.apples_in_basket - self.odd_apples - (even_apple_num + 1))
                    page.apple_counter_shows_how_many(btn_number - 1)
                    page.user_apples_not_in_basket(btn_number - 1)
                page.all_user_apples_even(btn_number - 1)
            page.add_apple(btn_number)
            page.alert_shows_after_try_add_from_empty_basket(btn_number)
            page.refresh_list()