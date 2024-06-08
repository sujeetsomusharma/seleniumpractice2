import time
import selenium
from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver.support.select import Select


class TestOne:
    def test_e2e(self):
        print("Selenium Version you are using = ", selenium.__version__)

        # driver = webdriver.Edge()
        driver = webdriver.Chrome()
        # driver = webdriver.Firefox()
        '''This is for when we have have offline chrome browser and chrome driver if vpn resrticted the driver access 
        other wise we can user direct by using driver = webdriver.Chrome() driver.get("https://www.cricbuzz.com/")
        '''
        # s = Service("C:\Users\sujeet.sharma\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        # driver = webdriver.Chrome(service=s)

        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        print("---Browser is open---")
        time.sleep(2)

        driver.maximize_window()
        print("---Window maximize---")
        time.sleep(2)

        print("---The Title of the page is---")
        print("The tile is = ", driver.title)
        time.sleep(2)

        print("---The url of the page is--- ")
        print("The url of the page is = ", driver.current_url)
        time.sleep(2)
