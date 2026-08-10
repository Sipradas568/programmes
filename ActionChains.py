from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
import time
import pytest
driver = webdriver.Chrome()
driver.get("https://datatables.net/")
driver.maximize_window()
data = driver.find_element(By.XPATH,'//a[@href="/"]')

act = ActionChains(driver)
act.move_to_element(data).perform()
wait = WebDriverWait(driver,10)
popup = wait.until(ec.visibility_of_element_located((By.XPATH,'//a[@href="/"]/div[@class = "nav-explain"]')))
txt = popup.text
print(txt)
time.sleep(5)
try:
    assert "Advanced interaction" in txt and "features for your table." in txt
    print("PASS")
except AssertionError:
    print("FAIL")





time.sleep(5)