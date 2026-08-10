from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
driver = webdriver.Chrome()
#driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

time.sleep(5)


def win_handled(driver):
    main = driver.current_window_handle
    windows = driver.window_handles
    for win in windows:
        if win != main:
            driver.switch_to.window(win)
            print(driver.title)
            driver.close()
        driver.switch_to.window(main)
        
    
    

driver.find_element(By.ID,"openwindow").click()
time.sleep(5)
win_handled(driver)
print(driver.title)

driver.find_element(By.ID,"opentab").click()
time.sleep(5)
win_handled(driver)
print(driver.title)



