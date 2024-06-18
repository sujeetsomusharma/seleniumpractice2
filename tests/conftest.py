import time
import pytest
import selenium
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    print("Selenium Version you are using =", selenium.__version__)

    # Get the browser name from the command-line option
    browser_name = request.config.getoption("browser")

    # Initialize the WebDriver based on the specified browser
    if browser_name == "chrome":
        driver = webdriver.Chrome()
        time.sleep(5)
    elif browser_name == "safari":
        driver = webdriver.Safari()
        time.sleep(5)
    elif browser_name == "FireFox":
        driver = webdriver.Firefox()
        time.sleep(5)
    else:
        raise ValueError(f"No Driver Available for the specified browser: {browser_name}")

    # Open the target URL
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    print("---Browser is open---")
    time.sleep(2)
    # Maximize the browser window
    #driver.maximize_window()
    driver.set_window_size(1920, 1080)
    print("---Window maximized---")
    time.sleep(2)

    # Print the title and URL of the current page
    print("---The Title of the page is---")
    print("The title is =", driver.title)
    time.sleep(2)

    print("---The URL of the page is---")
    print("The URL of the page is =", driver.current_url)
    time.sleep(2)

    # Assign the driver to the class that uses this fixture
    request.cls.driver = driver

    # Yield to allow test execution and then quit the driver
    yield
    driver.quit()
