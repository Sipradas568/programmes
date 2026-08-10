from selenium import webdriver
from selenium.webdriver.common.by import By
import test_data
import pytest
import time

@pytest.mark.usefixtures("setup")
class Test:

    def test_Dropdown(self,setup):
        self.driver = setup
        self.ctry = test_data.Countries()
        self.driver.find_element(By.XPATH,"//input[@id = 'autocomplete']").send_keys(self.ctry)
        time.sleep(5)


