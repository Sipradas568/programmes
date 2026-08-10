from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
srch = driver.find_element(By.XPATH , '//input[@name="search_query"]')
wait = WebDriverWait(driver,10)
wait.until(EC.element_to_be_clickable ,srch)
srch.send_keys("abc")
ck = driver.find_element(By.XPATH , '//input[@name="search_query"]')
#driver.sleep(5)
driver.close()


ele = driver.find_element(by.xpath, "//input[@id = 'username']")
driver.execute_script("arguments[0].scrollIntoview();", ele)