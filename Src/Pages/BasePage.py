from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

class BasePage(object):
    def __init__(self,driver:WebDriver) -> None:
        self.driver = driver

    # Function to launch site
    def launch_app(self) -> None:
        self.driver.maximize_window()
        self.driver.get('https://mystifying-beaver-ee03b5.netlify.app/')

    # Function to clear and enter text
    def enter_text(self, elem:WebElement, value:str) -> None:
        elem.clear()
        elem.send_keys(value)
        