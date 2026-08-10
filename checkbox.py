from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
driver = webdriver.Chrome()
#driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

webele = driver.find_element(By.XPATH,'//input[@id="checkBoxOption1"]')
webele.click()
wait = WebDriverWait(driver,10)
wait.until(ec.element_selection_state_to_be(webele,True))
#driver.execute_script("arguments[0].scrollIntoView();",webele)

#time.sleep(10)
driver.close()
