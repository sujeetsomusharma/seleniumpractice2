from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    checkout = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")
    placeorder = (By.XPATH, "//button[text()='Place Order']")

    def checkoutItems(self):
        return self.driver.find_element(*CheckoutPage.checkout)
        # driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

    def PlaceOrder(self):
        return self.driver.find_element(*CheckoutPage.placeorder)
