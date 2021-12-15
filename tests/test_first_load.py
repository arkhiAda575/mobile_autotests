import pytest


class TestFirstLoad:
    # @pytest.mark.parametrize()
    def test_allow_location_access(self, app):
        app.first_load.tap_next_button()
        app.first_load.tap_allow_location_access()
        app.first_load.tap_allow_once_location()

    def test_select_city_by_search(self, app):
        app.first_load.tap_next_button()
        app.first_load.tap_select_city()
        app.first_load.find_city("Казань")

    def test_enable_notifications(self, app):
        app.first_load.tap_next_button()
        app.first_load.tap_allow_location_access()
        app.first_load.tap_allow_once_location()
        app.first_load.tap_enable_notifications()

    def test_enable_notifications_not_now(self, app):
        app.first_load.tap_next_button()
        app.first_load.tap_allow_location_access()
        app.first_load.tap_allow_once_location()
        app.first_load.tap_enable_notifications_not_now()
