from fixtures.screens.first_load import FirstLoadScreen


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.first_load = FirstLoadScreen(self)

    def quit(self):
        self.driver.quit()
