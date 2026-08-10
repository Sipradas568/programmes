from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.get("https://hellobubble.com/?srsltid=AfmBOoodp1z5ogRevTKai15EcWaGrhbGzaaikQ50tyQNWAXN0Cio56ZX")
wait = WebDriverWait(driver,20)

cont  = wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class= 'Avada-CookiesBar_Container']/descendant::div[@class='Avada-CookiesBar__MessageInner']//span")))

print(cont.text)
crs = wait.until(EC.presence_of_element_located((By.XPATH,"//button[@type='button' and @class ='sc-75msgg-0 fvUtOf close-button cw-close']")))
crs.click()
time.sleep(5)