from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time
driver = webdriver.Chrome()
driver.get("https://www.makemytrip.com/")
time.sleep(5)
fr = driver.find_element(By.XPATH,"//section[@data-cy='CommonModal_2']")

org = driver.current_window_handle
for i in driver.window_handles :
    if i not in org:
        driver.switch_to.window(i)
#driver.find_element(By.XPATH,"//input[@type='text'and @data-cy='userName']").send_keys("900")

#we = driver.find_element(By.XPATH,"//*[@data-cy='MobileCodeDropDown_60']")
wait = WebDriverWait(driver,10)
wait.until(ec.presence_of_element_located((By.XPATH,"//*[@data-cy='MobileCodeDropDown_60']"))).click()
time.sleep(5)
#st = driver.find_element(By.XPATH ,'//span[contains(text(), "United States")]')
wait.until(ec.presence_of_element_located((By.XPATH ,'//span[contains(text(), "United States")]'))).click()
#st.click()
#time.sleep(5)
#obj = Select(dropdown)
#print(len(dropdown))
time.sleep(5)
driver.close()