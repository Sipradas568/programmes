from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import time
driver = uc.Chrome(version_main=135)
driver.get("https://www.flipkart.com/")
time.sleep(5)
fr = driver.find_element(By.XPATH,"//div[@id='anonCarousel1']//descendant::li[1]/descendant::img").click()
time.sleep(5)
driver.close()
