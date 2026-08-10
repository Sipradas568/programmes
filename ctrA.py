from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time 
driver = webdriver.Chrome()
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@placeholder = 'Enter Mobile Number']").send_keys("9902363670")
time.sleep(5)
act = ActionChains(driver)
act.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
time.sleep(5)



