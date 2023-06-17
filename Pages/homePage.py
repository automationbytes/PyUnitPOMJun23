from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Locators.locators import locators
from  selenium import webdriver


class homePage():
    def __init__(self,driver):
        self.driver = driver
        #self.driver = webdriver.Chrome()


    def selectSortFilter(self,option):
        dropdown = Select(self.driver.find_element(By.XPATH,locators.sort_select_xpath))
        dropdown.select_by_visible_text(option)

    def logout(self):
        self.driver.find_element(By.XPATH,locators.open_menu_xpath).click()
        self.driver.find_element(By.XPATH,locators.logout_button_xpath).click()
