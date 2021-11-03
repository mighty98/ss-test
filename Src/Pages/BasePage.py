from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

class BasePage(object):
    def __init__(self,driver:WebDriver) -> None:
        self.driver = driver

    def launch_app(self) -> None:
        self.driver.maximize_window()
        self.driver.get('https://mystifying-beaver-ee03b5.netlify.app/')

    def enter_text(self, elem:WebElement, value:str) -> None:
        elem.clear()
        elem.send_keys(value)
        