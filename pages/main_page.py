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
        #self.wait_until_button_can_add(number, link)
        MainPageLocators.GRAB_APPLE_BTN_EACH[1] = MainPageLocators.GRAB_APPLE_BTN_EACH[1][
                                                  :-(len(f"[{str(bttn_number+1)}]"))]

    def refresh_list(self):
        link = self.browser.find_element(*MainPageLocators.CLEAN_BTN)
        link.click()

    def should_not_be_alert(self):
        assert self.is_not_element_present(*MainPageLocators.ALERT), \
            "Alert after add present, but should not"

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
            "Apple counter number != number of apples in user list"

    def count_apples_in_basket(self):
        self.amount_of_busket_apples = len(self.browser.find_elements(*MainPageLocators.BASKET_APPLES))
        return(self.amount_of_busket_apples)

    def user_apple_not_in_basket(self, bttn_number):
        for i in range(self.count_user_apples(bttn_number)):
            for j in range(self.count_apples_in_basket()):
                MainPageLocators.USER_ITEMS[1] += f"[{str(bttn_number + 1)}]" \
                                                  + MainPageLocators.USER_APPLES[1] + f"[{str(i + 1)}]"
                MainPageLocators.BASKET_APPLES[1] += f"[{str(j + 1)}]"
                self.user_apple = self.browser.find_element(*MainPageLocators.USER_ITEMS).text
                self.busket_apple = self.browser.find_element(*MainPageLocators.BASKET_APPLES).text
                MainPageLocators.USER_ITEMS[1] = MainPageLocators.USER_ITEMS[1][
                            :-(len(f"[{str(bttn_number + 1)}]" + MainPageLocators.USER_APPLES[1] + f"[{str(i + 1)}]"))]
                MainPageLocators.BASKET_APPLES[1] = MainPageLocators.BASKET_APPLES[1][
                                                    :-(len(f"[{str(j + 1)}]"))]
                assert self.user_apple != self.busket_apple, "User have same apple as in basket"

