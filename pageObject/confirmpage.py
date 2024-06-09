from selenium.webdriver.common.by import By


class Proceed:
    def __init__(self, driver):
        self.driver = driver

    proceed_button = (By.XPATH, "//button[text()='Proceed']")

    def finalPage(self):
        return self.driver.find_element(*Proceed.proceed_button)
        # self.driver.find_element(By.XPATH, "//button[text()='Proceed']").click()
