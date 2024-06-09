from lib2to3.pgen2 import driver

from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, ".search-keyword")

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)
        # driver.find_element(By.CSS_SELECTOR, ".search-keyword")
