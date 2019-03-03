import unittest
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException


class BaseTest(unittest.TestCase):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'Untitled'
    driver = None

    def setUp(self):
        self.dc["platformName"] = "Android"
        self.dc["deviceName"] = "Nexus_5X_API_24"
        # self.dc["platformVersion"] = "8.1"
        # self.dc["platformName"] = "Android"
        # self.dc["automationName"] = "uiautomator2"
        self.dc["avd"] = "Nexus_5X_API_24"
        self.dc["app"] = "/Users/salvatore/Downloads/n26/task_2/GnucashAndroid_v2.4.0.apk"
        self.dc["appPackage"] = "org.gnucash.android"
        self.dc["appActivity"] = "org.gnucash.android.ui.account.AccountsActivity"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)

    def tearDown(self):
        self.driver.quit()


class FunctionalTests(BaseTest):

    def testUntitled(self):
        btn_next = self.driver.find_element_by_id("org.gnucash.android:id/btn_save")
        btn_next.click()
        btn_next.click()
        btn_next.clear()
        el3 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.ListView/android.widget.CheckedTextView[1]")
        el3.click()
        btn_next.click()
        btn_next.click()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(FunctionalTests('testUntitled'))
    return suite


if __name__ == '__main__':
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite())
