from selenium.webdriver.common.by import By


class MainPageLocators():
    GRAB_APPLE_BTN_ALL = (By.CSS_SELECTOR, ".grab-apple")
    GRAB_APPLE_BTN_EACH = ([By.XPATH, "(//button[contains(@class, 'grab-apple')])"])
    CLEAN_BTN = (By.CSS_SELECTOR, ".free-apples")
    APPLE_COUNTER = ([By.XPATH, "(//span[contains(@class, 'badge-pill')])"])
    ALERT = (By.CSS_SELECTOR, ".alert-danger")
    USER_ITEMS = ([By.XPATH, "(//li[@class='list-group-item']"])  # missed ")", only + USER_APPLES
    USER_APPLES = ([By.XPATH, "//li[contains(text(), 'Apple')])"])  # missed "(", only + USER_ITEMS
    BASKET_APPLES = ([By.XPATH, "(//ul[contains(@class, 'basket')]//span[contains(text(), 'Apple')])"])
    NAVBAR = (By.CSS_SELECTOR, ".navbar-header")
    ALERT_WRONG_TYPE = (By.XPATH, "(//div[contains(@class, 'col-12 alerts')]//div["
                                  "contains(text(), 'You cant have apples with both odd and even ids, try again')])")
    ALERT_NONE_IN_BASKET = (By.XPATH, "(//div[contains(@class, 'col-12 alerts')]//div["
                                  "contains(text(), 'Apple basket is empty')])")