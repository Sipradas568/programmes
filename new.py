from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest
import time
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

def dropdown(suggestion,op):
    ele = driver.find_element(By.XPATH, "//input[@id = 'autocomplete']")
    if ele.is_enabled():
        ele.send_keys(suggestion)
        
    wait = WebDriverWait(driver, 10)

    lst = wait.until(ec.presence_of_all_elements_located((By.XPATH,"//ul[@id='ui-id-1']//li"))) 
    for i in lst:
        text = i.text.strip()
        print(text)
        if text == op:
            i.click()
            print("this is the op" , text)
            return text
            

@pytest.mark.parametrize("a,b",[("Ind","India")])
def test_prac(a,b):
        obj = dropdown(a,b)
        assert obj==b, "not matching"






