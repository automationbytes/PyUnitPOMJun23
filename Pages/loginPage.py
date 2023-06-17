from selenium.webdriver.common.by import By

from Locators.locators import locators
from  selenium import webdriver


class loginPage():
    def __init__(self,driver):
        self.driver = driver
#        self.driver = webdriver.Chrome()


    def enterUsername(self,username):
        self.driver.find_element(By.NAME,locators.username_inputbox_name).send_keys(username)

    def enterPassword(self, password):
        self.driver.find_element(By.NAME, locators.password_inputbox_name).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(By.ID, locators.login_button_id).click()

