import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.checkoutpage import CheckoutPage
from pageObject.confirmpage import Proceed
from pageObject.homepage import HomePage
from utilities.baseclass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        log.info("Starting end-to-end test")

        expected_list = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
        actual_list = []

        homePage = HomePage(self.driver)
        homePage.shopItems().send_keys("ber")
        time.sleep(5)  # Should ideally be replaced with explicit wait for element visibility

        results = self.driver.find_elements(By.XPATH, "//div[@class='products']/div")
        log.info("Getting all the card results")

        for result in results:
            actual_list.append(result.find_element(By.XPATH, "h4").text)
            result.find_element(By.XPATH, "div/button").click()

        if expected_list == actual_list:
            log.info("The actual and expected list are the same")
        else:
            log.warning("The list in actual and expected are different")

        log.info("All items are added to cart with 'ber' keyword items")

        self.driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
        log.info("Click on cart is done")

        checkout_items = CheckoutPage(self.driver)
        checkout_items.checkoutItems().click()
        time.sleep(5)
        log.info("Proceed to checkout done")

        promo_code = "rahulshettyacademy"
        empty_promo_code = ''
        wrong_promo_code = "ahulshettyacademy"
        self.driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys(promo_code)
        time.sleep(5)
        log.info("Promo code is filled")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@class='promoBtn']").click()
        log.info("Click on apply promo code button is done")
        time.sleep(5)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.promoInfo')))
        promo_info = self.driver.find_element(By.CSS_SELECTOR, ".promoInfo").text
        log.info(f"Promo info: {promo_info}")

        if promo_info == "Code applied ..!":
            log.info("Promo code applied successfully")
        elif promo_info == "Invalid code ..!":
            log.warning("Invalid promo code")
        elif promo_info == "Empty code ..!":
            log.warning("No promo code applied")
        else:
            log.error("Unexpected promo code response")

        prices = self.driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
        sum_of_price = sum(int(price.text) for price in prices)
        log.info(f"Sum of the item prices: {sum_of_price}")

        final_amount = int(self.driver.find_element(By.XPATH, "//span[@class='totAmt']").text)
        log.info(f"Final amount of the items: ₹{final_amount}")

        discounted_price = float(self.driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
        log.info(f"Discounted price: {discounted_price}")

        if discounted_price < final_amount:
            log.info("Discount promo code applied successfully")
        else:
            log.warning("Discounted promo code is invalid and not applied")

        place_order_items = CheckoutPage(self.driver)
        place_order_items.PlaceOrder().click()
        log.info("Place order button clicked")
        time.sleep(2)
        
        self.driver.find_element(By.XPATH, "//select[@style='width: 200px;']").click()
        self.driver.find_element(By.XPATH, "//option[@value='India']").click()
        log.info("Selected country: India")
        time.sleep(2)

        self.driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']").click()
        log.info("Accepted terms and conditions")
        time.sleep(2)

        final_proceed = Proceed(self.driver)
        final_proceed.finalPage().click()
        log.info("Proceed button clicked")
        time.sleep(2)

        log.info("--- End of Test ---")
        time.sleep(5)  # For demonstration purposes only
