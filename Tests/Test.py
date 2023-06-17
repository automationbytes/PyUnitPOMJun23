import sys
import os


import unittest
import time
from HTMLTestRunner.runner import HTMLTestRunner
#from html_reporter import HTMLTestRunner

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("--start-maximized")
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Pages import loginPage
from Pages import homePage

class saucelabsDemoTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.driver.get("https://www.saucedemo.com/")

    def test_1_login(self):
        login = loginPage.loginPage(self.driver)
        login.enterUsername("standard_user")
        login.enterPassword("secret_sauce")
        login.clickLoginButton()

    def test_2_sorting(self):
        home = homePage.homePage(self.driver)
        home.selectSortFilter("Price (high to low)")

        home.logout()

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='Test report', report_name='report',
                            open_in_browser=True, description="Dev Labs HTML TestReport", tested_by="Vignesh",
                            add_traceback=False)
    # runner = HTMLTestRunner(
    #     report_filepath="my_report.html",
    #     title="My unit test",
    #     description="This demonstrates the report output by HTMLTestRunner.",
    #     open_in_browser=True
    # )

    unittest.main(testRunner=runner)
