from typing import List
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from Src.Pages.BasePage import BasePage
from Src.Utils.Utils import is_list_sorted, sanitize_unit_list_to_number_list, sanitize_complexity_list_to_number_list

class StatisticsPage(BasePage):
    def __init__(self, driver:WebDriver) -> None:
        self.driver = driver

    def clear_filter(self):
       elem:WebElement = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,"filter-input")))
       elem.clear()
    
    def filter_statistics(self, value:str):        
        elem:WebElement = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,"filter-input")))
        self.enter_text(elem, value)

    def select_sort_criteria_by_value(self, sort_by:str):
        selectOptions: Select =  Select(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,"sort-select"))))
        selectOptions.select_by_value(sort_by)

    def sort_statistics_by(self, sort_by:str):
        if sort_by.lower() == "name":
            self.select_sort_criteria_by_value("name")
        elif sort_by.lower() == "number of cases":
            self.select_sort_criteria_by_value("cases")
        elif sort_by.lower() == "impact score":
            self.select_sort_criteria_by_value("averageImpact")
        elif sort_by.lower() == "complexity":
            self.select_sort_criteria_by_value("complexity")
        else:
            raise Exception("There is no such option as " + sort_by)

    def verify_filtered_result_for_name(self, key:str):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='table-content']")),"No result found")
        filteredRows: List[WebElement] = self.driver.find_elements(By.XPATH,"//div[contains(@class,'data-name')]")
        for row in filteredRows:
            assert key.lower() in row.text.lower()
        
    
    def verify_sort_statistics(self, sort_by:str):
        if sort_by.lower() == "name":
            names = [el.text for el in self.driver.find_elements(By.XPATH,"//div[contains(@class,'data-name')]")]
            assert is_list_sorted(names) == True
        elif sort_by.lower() == "number of cases":
            cases = [el.text for el in self.driver.find_elements(By.XPATH,"//div[contains(@class,'data-cases')]")]
            sanitized_list = sanitize_unit_list_to_number_list(cases)
            assert is_list_sorted(sanitized_list) == True
        elif sort_by.lower() == "impact score":
            scores = [el.text for el in self.driver.find_elements(By.XPATH,"//div[contains(@class,'data-averageImpact')]")]
            sanitized_list = sanitize_unit_list_to_number_list(scores)
            assert is_list_sorted(sanitized_list) == True
        elif sort_by.lower() == "complexity":
            complexities = [el.text for el in self.driver.find_elements(By.XPATH,"//div[contains(@class,'data-complexity')]")]
            sanitized_list =  sanitize_complexity_list_to_number_list(complexities)
            assert is_list_sorted(sanitized_list) == True
        else:
            raise Exception("There is no such option as " + sort_by)