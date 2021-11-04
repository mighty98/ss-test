import unittest
from Src.Pages.BasePage import BasePage
from Src.Pages.StatisticsPage import StatisticsPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class WebbriverSetup(unittest.TestCase):
    # Setup driver and launch applcation for each test. Framework currently supports chrome
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.app = BasePage(self.driver)
        self.statisticsPage = StatisticsPage(self.driver)
        self.app.launch_app()
 
    # Close the browser after each test
    def tearDown(self):
        if (self.driver != None):
            self.driver.close()
            self.driver.quit()