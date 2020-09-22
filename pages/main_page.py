from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from .locators import MainPageLocators
import time


class MainPage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=2):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def open(self):
        self.browser.get(self.url)

    def count_buttons_grab(self):
        self.amount_of_grab_btn = len(self.browser.find_elements(*MainPageLocators.GRAB_APPLE_BTN_ALL))
        return(self.amount_of_grab_btn)

    def add_apple(self, bttn_number):
        MainPageLocators.GRAB_APPLE_BTN_EACH[1] += f"[{str(bttn_number+1)}]"
        link = self.browser.find_element(*MainPageLocators.GRAB_APPLE_BTN_EACH)
        time.sleep(8)
        link.click()
        MainPageLocators.GRAB_APPLE_BTN_EACH[1] = MainPageLocators.GRAB_APPLE_BTN_EACH[1][
                                                  :-(len(f"[{str(bttn_number+1)}]"))]

    def refresh_list(self):
        link = self.browser.find_element(*MainPageLocators.CLEAN_BTN)
        link.click()
        time.sleep(1)

    def should_not_be_alert(self):
        assert self.is_not_element_present(*MainPageLocators.ALERT), \
            "Alert after add present, but should not"   # добавить яблоко, юзера

    def count_user_apples(self, bttn_number):
        MainPageLocators.USER_ITEMS[1] += f"[{str(bttn_number+1)}]" + MainPageLocators.USER_APPLES[1]
        self.count_for_user = len(self.browser.find_elements(*MainPageLocators.USER_ITEMS))
        MainPageLocators.USER_ITEMS[1] = MainPageLocators.USER_ITEMS[1][
                                    :-(len(f"[{str(bttn_number + 1)}]" + MainPageLocators.USER_APPLES[1]))]

        return(self.count_for_user)

    def apple_counter_shows_how_many(self, bttn_number):
        MainPageLocators.APPLE_COUNTER[1] += f"[{str(bttn_number + 1)}]"
        self.counter_number = int(self.browser.find_element(*MainPageLocators.APPLE_COUNTER).text)
        MainPageLocators.APPLE_COUNTER[1] = MainPageLocators.APPLE_COUNTER[1][
                                                  :-(len(f"[{str(bttn_number + 1)}]"))]
        assert self.count_user_apples(bttn_number) == self.counter_number, \
            f"Apple counter number != number of apples in user list for user{bttn_number+1}"

    def count_apples_in_basket(self):
        time.sleep(1)
        self.amount_of_basket_apples = len(self.browser.find_elements(*MainPageLocators.BASKET_APPLES))
        return(self.amount_of_basket_apples)

    def user_apples_not_in_basket(self, bttn_number):
        for i in range(self.count_user_apples(bttn_number)):
            for j in range(self.count_apples_in_basket()):
                MainPageLocators.USER_ITEMS[1] += f"[{str(bttn_number + 1)}]" \
                                                  + MainPageLocators.USER_APPLES[1] + f"[{str(i + 1)}]"
                MainPageLocators.BASKET_APPLES[1] += f"[{str(j + 1)}]"
                self.user_apple = self.browser.find_element(*MainPageLocators.USER_ITEMS).text
                self.basket_apple = self.browser.find_element(*MainPageLocators.BASKET_APPLES).text
                MainPageLocators.USER_ITEMS[1] = MainPageLocators.USER_ITEMS[1][
                            :-(len(f"[{str(bttn_number + 1)}]" + MainPageLocators.USER_APPLES[1] + f"[{str(i + 1)}]"))]
                MainPageLocators.BASKET_APPLES[1] = MainPageLocators.BASKET_APPLES[1][
                                                    :-(len(f"[{str(j + 1)}]"))]
                assert self.user_apple != self.basket_apple, \
                    f"User{bttn_number+1} apple{i+1} same as apple{j+1} in basket"

    def count_odd_apple_in_basket(self):
        self.amount_of_basket_odd_apples = self.count_apples_in_basket() - self.count_apples_in_basket() // 2
        return(self.amount_of_basket_odd_apples)

    def get_all_user_apples_number(self, bttn_number):
        self.all_user_apples = []
        for i in range(self.count_user_apples(bttn_number)):
            MainPageLocators.USER_ITEMS[1] += \
                f"[{str(bttn_number + 1)}]" + MainPageLocators.USER_APPLES[1] + f"[{str(i + 1)}]"
            self.apple_number = self.browser.find_element(*MainPageLocators.USER_ITEMS).text
            self.all_user_apples.append(self.apple_number[5:])
            MainPageLocators.USER_ITEMS[1] = MainPageLocators.USER_ITEMS[1][
                            :-(len(f"[{str(bttn_number + 1)}]" + MainPageLocators.USER_APPLES[1] + f"[{str(i + 1)}]"))]
        return(self.all_user_apples)

    def all_user_apples_odd(self, bttn_number):
        self.all_user_apples_numbers = self.get_all_user_apples_number(bttn_number)
        for i in self.all_user_apples_numbers:
            assert int(i) % 2 != 0, f"Apple{i} for user{bttn_number+1} not odd"

    def count_even_apple_in_basket(self):
        self.amount_of_basket_even_apples = self.count_apples_in_basket() // 2
        return (self.amount_of_basket_even_apples)

    def all_user_apples_even(self, bttn_number):
        self.all_user_apples_numbers = self.get_all_user_apples_number(bttn_number)
        for i in self.all_user_apples_numbers:
            assert int(i) % 2 == 0, f"Apple{i} for user{bttn_number+1} not even"

    def alert_shows_after_try_add_wrong_apple_type(self, bttn_number):
        self.user_apples = self.count_user_apples(bttn_number)
        self.basket_apples = self.count_apples_in_basket()
        self.add_apple(bttn_number)
        assert self.is_element_present(*MainPageLocators.ALERT_WRONG_TYPE), \
            f"Alert not appears after add wrong type for user{bttn_number+1}"
        assert self.user_apples == self.count_user_apples(bttn_number), \
            f"Added apple for user, but should not be because of wrong type for user{bttn_number+1}"
        assert self.basket_apples == self.count_apples_in_basket(), \
            f"Disappeared apple from basket, but should not because of wrong type for user{bttn_number + 1}"

    def check_apples_added(self, bttn_number, apple_number, present_basket_apples_amount):
        assert self.count_apples_in_basket() == present_basket_apples_amount, \
            f"Apple{apple_number+1} not added for user{bttn_number+1}"

    def alert_shows_after_try_add_from_empty_basket(self, bttn_number):
        assert self.is_element_present(*MainPageLocators.ALERT_NONE_IN_BASKET), \
            f"Alert not appears after add from empty basket for user{bttn_number + 1}"
        assert self.count_apples_in_basket() == 0, \
            f"Basket should be empty, but it does not for user{bttn_number+1}"