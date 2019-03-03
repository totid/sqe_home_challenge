import unittest
from appium import webdriver
from configuration.DeviceConfiguration import PLATFORM_NAME, DEVICE_NAME, AVD, APP, APP_PACKAGE, APP_ACTIVITY,\
    PLATFORM_VERSION, AUTOMATION_NAME


class BaseTest(unittest.TestCase):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'Untitled'
    driver = None

    def setUp(self):
        self.dc["platformName"] = PLATFORM_NAME
        self.dc["deviceName"] = DEVICE_NAME
        # self.dc["platformVersion"] = PLATFORM_VERSION
        # self.dc["automationName"] = AUTOMATION_NAME
        self.dc["avd"] = AVD
        self.dc["app"] = APP
        self.dc["appPackage"] = APP_PACKAGE
        self.dc["appActivity"] = APP_ACTIVITY
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)

    def tearDown(self):
        self.driver.quit()
