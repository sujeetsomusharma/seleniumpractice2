import time

import selenium
from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui, expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from utilities.baseclass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        expected_list = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
        actual_list = []

        self.driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
        time.sleep(5)

        results = self.driver.find_elements(By.XPATH, "//div[@class='products']/div")
        print("The list are = ", results)

        for result in results:
            actual_list.append(result.find_element(By.XPATH, "h4").text)
            result.find_element(By.XPATH, "div/button").click()

        if expected_list == actual_list:
            print("The actual and expected list are same")
        else:
            print("The list in actual and expected are different")

        print("All items are added to cart with 'ber' keyword items")

        print("Add to cart now after product selection")
        self.driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
        print("Click on cart is done")

        print("Proceed to checkout")
        self.driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
        print("Proceed to checkout Done")

        promo_code = "rahulshettyacademy"
        empty_promo_code = ''
        wrong_promo_code = "ahulshettyacademy"

        print("Add Promo Code")

        self.driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys(promo_code)

        print("Promo Code is Filled ... !")
        print("Now Click on Add button to avail the discount")

        self.driver.find_element(By.XPATH, "//button[@class='promoBtn']").click()
        print("Click on Add button is Done")

        wait_explicitly = WebDriverWait(self.driver, 10)
        wait_explicitly.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.promoInfo')))
        print("Explicit Code Applied")
        promo_Info = self.driver.find_element(By.XPATH, "//div/span[@class='promoInfo']").text
        print(promo_Info)

        if promo_Info == "Code applied ..!":
            print(" --The promo code is applied --")
        elif promo_Info == "Invalid code ..!":
            print(" -- The promo code is not a valid code --")
        elif promo_Info == "Empty code ..!":
            print("-- No promo code is applied ---")
        else:
            print(" ---No promo code option is available ---")

        print("Print the sum of the items price")
        prices = self.driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")

        sum_of_price = 0
        for price in prices:
            sum_of_price = sum_of_price + int(price.text)
        print(sum_of_price)

        final_amount = int(self.driver.find_element(By.XPATH, "//span[@class='totAmt']").text)
        print("The final amount of the items is = ₹", final_amount)
        print("Grab the discounted price and check whether it is less than the actual price")

        discounted_price = float(self.driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
        print("The discounted_price = ", discounted_price)

        if discounted_price < final_amount:
            print("Discount Promo Code is applied !!!")
        else:
            print("Discounted Promo Code is Invalid and not Applied")

        print("---EOC---")
        time.sleep(5)
