from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import os
driver = webdriver.Chrome()
#driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
webele = driver.find_element(By.NAME, "show-hide")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",webele)
time.sleep(5)
#wait = WebDriverWait(driver,10)
#wait.until(ec.presence_of_element_located((By.XPATH,"//legend[text()='Element Displayed Example']")))
if driver.find_element(By.NAME, "show-hide").is_displayed():
    driver.find_element(By.XPATH,'//input[@id ="hide-textbox"]').click()
    time.sleep(3)
    dir = os.getcwd()
    path = os.path.join(dir,"osrahul.png")
    driver.get_screenshot_as_file(path)
    driver.find_element(By.ID,'show-textbox').click()

time.sleep(5)

