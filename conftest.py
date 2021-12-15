import logging

import pytest
from appium import webdriver

from fixtures.screens.application import Application

logger = logging.getLogger("uds_app_mobile_autotests")

IOS_UDS_APP = '/Users/user/Library/Developer/Xcode/DerivedData/UDS3-cnymmnmwbgahgjeuodpfpzhpxgre/Build/Products/Debug-iphonesimulator/UDS3.app'


@pytest.fixture()
def app():
    desired_caps = dict(
        platformName='iOS',
        platformVersion='15.0',
        automationName='XCUITest',
        deviceName='iPhone 12 Pro Max',
        app=IOS_UDS_APP,
        newCommandTimeout='12000',
        launchTimeout='500000'
    )
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    logger.info("Start app")
    app = Application(driver)
    yield app
    #app.quit()
