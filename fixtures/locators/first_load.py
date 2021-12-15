from appium.webdriver.common.mobileby import MobileBy

from fixtures.locators.appium_locators import By


class FirstLoadLocators:
    NEXT_BTN = (By.NAME, "Next")
    ALLOW_LOCATION_BTN = (By.ACCESSIBILITY_ID, "Allow location access")
    SELECT_CITY_BTN = (By.ACCESSIBILITY_ID, "Select your city")
    ENABLE_NOTIFICATIONS_BTN = (By.ACCESSIBILITY_ID, "Enable notifications")
    NOT_NOW_BTN = (By.ACCESSIBILITY_ID, "Not now")
    ALLOW_ONCE_BTN = (By.ACCESSIBILITY_ID, "Allow Once")
    ALLOW_WHILE_USING_BTN = (By.ACCESSIBILITY_ID, "Allow While Using App")
    DONT_ALLOW_BTN = (By.ACCESSIBILITY_ID, "Don't Allow")
    ENTER_CITY = (By.IOS_PREDICATE("value == 'Enter your city'"))
