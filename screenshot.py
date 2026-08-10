from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import os
driver = webdriver.Chrome()
#driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)
print(os.getcwd())


driver.save_screenshot(os.getcwd()+'\\practice.png')