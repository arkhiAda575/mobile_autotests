from fixtures.locators.first_load import FirstLoadLocators
from fixtures.screens.base_screen import BaseScreen


class FirstLoadScreen(BaseScreen):
    def tap_next_button(self):
        self.click_element(FirstLoadLocators.NEXT_BTN)

    def tap_allow_location_access(self):
        self.click_element(FirstLoadLocators.ALLOW_LOCATION_BTN)

    def tap_allow_once_location(self):
        self.click_element(FirstLoadLocators.ALLOW_ONCE_BTN)

    def tap_allow_while_using_location(self):
        self.click_element(FirstLoadLocators.ALLOW_WHILE_USING_BTN)

    def tap_not_allow_location(self):
        self.click_element(FirstLoadLocators.DONT_ALLOW_BTN)

    def tap_select_city(self):
        self.click_element(FirstLoadLocators.SELECT_CITY_BTN)

    def find_city(self, city="Moscow"):
        self.fill_element(FirstLoadLocators.ENTER_CITY, city)
        self.send_enter(FirstLoadLocators.ENTER_CITY)

    def tap_enable_notifications(self):
        self.click_element(FirstLoadLocators.ENABLE_NOTIFICATIONS_BTN)

    def tap_enable_notifications_not_now(self):
        self.click_element(FirstLoadLocators.NOT_NOW_BTN)
